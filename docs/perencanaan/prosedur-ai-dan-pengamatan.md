# LLD AI dan prosedur pengamatan CCTV

| Identitas | Nilai |
|---|---|
| Tim / sprint / minggu | KELOMPOK-10 / S01 / 3 |
| Tugas / PIC | W03-T04 / Rizky Bintang Fadillah |
| Versi / tanggal | 0.1 / 29 Oktober 2026 |
| Status | Prosedur lengkap untuk review; sumber/ROI/model/data aktual ditetapkan pada tahap pelaksanaan |
| Lokasi | `KELOMPOK-10/docs/perencanaan/prosedur-ai-dan-pengamatan.md` |

## 1. Acuan, cakupan dan keluaran

Proposal sempro `FINAL INI A(1).docx` Subbab 4.2–4.6, 5.3 dan Bab 6, SRS Bagian 4/8, serta HLD Bagian 4.1/4.4 menjadi acuan. Tiga CCTV dari lokasi berbeda dipetakan ke fase virtual A/B/C. Pengamatan pagi, siang, sore mengikuti keterlihatan kendaraan/garis henti. Malam di luar pengujian visual. Sistem adalah prototipe, sehingga siklus lampu jalan pada rekaman dan siklus LED ESP32 adalah dua pengamatan berbeda.

YOLO mendeteksi empat kelas: `car` (mobil), `motorcycle` (sepeda motor), `bus`, dan `truck`. Varian, bobot, ukuran input, confidence, NMS, pustaka dan perangkat komputasi dipilih saat implementasi. Setiap kendaraan bernilai satu unit, termasuk yang berhenti atau bergerak. Tidak ada konversi SMP/PCE.

## 2. Penyiapan sumber dan konfigurasi per kamera

| Data konfigurasi | Cara menetapkan / validasi |
|---|---|
| camera_id, source_id, lokasi dan phase | Satu sumber jelas per fase virtual; catat alamat akses privat terpisah dari contoh publik |
| Dimensi/FPS/format dan pembacaan | Periksa frame aktual dari sumber; simpan karakteristik serta batas decoding |
| Pendekat / garis henti | Pilih jalan lurus searah menuju garis henti yang dapat diamati |
| Poligon ROI | Koordinat piksel frame asli; area meliputi lajur searah terpilih, tidak mencampur arus berlawanan |
| Panjang L_m dan jumlah lajur m | Cocokkan patokan awal/akhir gambar dengan Google Maps; simpan bukti ukur/sumber/tanggal; L_m >0, m integer >0 dan panjang antarlajur setara |
| frame_source_ts dan frame_received_ts | Catat terpisah. Bila timestamp sumber tidak tersedia, gunakan null dan jelaskan keterbatasan umur gambar |
| Umur frame dan batas | Tetapkan dasar/ambang sesuai kemampuan sumber; buffer residence di server tidak membuktikan umur sejak perekaman |
| Versi | config_version/roi_version untuk koordinat, panjang, lajur, dimensi, dan pemetaan |

Konfigurasi kamera aktual ditulis pada pekerjaan minggu 6. Panjang/lajur/ambang di control.example.json hanya fixture format; tidak dipakai sebagai hasil survei. Jika dimensi sumber berubah, jangan memakai ROI lama tanpa transformasi yang terdefinisi atau validasi ulang.

## 3. Rancangan modul dan kontrak internal

| Modul rancangan | Masukan | Keluaran / perilaku |
|---|---|---|
| Reader per kamera | Koneksi sumber dan konfigurasi | Buffer frame terakhir berhasil didekode beserta ID, dimensi, waktu dan status; pembaruan thread-safe |
| Snapshot selector | camera_id dan pemicu unik | Salinan frame utuh beserta snapshot konfigurasi versinya; buffer reader tidak diubah oleh inferensi |
| Validator | Frame dan konfigurasi | Valid atau alasan invalid; mencakup sumber/decoding, dimensi, ROI, L/lajur dan umur yang terukur |
| Detector YOLO | Frame utuh dan model yang dimuat sekali | Bounding box, kelas dan confidence; koordinat dikembalikan ke frame asli |
| ROI counter | Deteksi empat kelas dan poligon | Hitungan per kelas/total dari satu frame |
| Density calculator | N, L_m, m | k kendaraan/km/lajur, atau invalid bila masukan tidak sah |
| Measurement adapter | Hasil dan identitas sasaran | Objek internal backend sesuai field measurement, kemudian salinan metadata ke MQTT/log |

Satu pemicu unik menghasilkan satu measurement_id. Deduplikasi trigger dikelola backend; callback ulang tidak memulai AI kedua. Model tidak dimuat ulang setiap pemicu. Pembacaan tiga video tetap memperbarui buffer, sedangkan penghitungan hanya pada snapshot yang dipilih. Tidak ada jendela akumulasi kendaraan 60 detik atau penjumlahan antarframe.

```text
init: validasi konfigurasi, muat model satu kali, mulai reader A/B/C
measure(target):
  pilih kamera dari fase sasaran yang tervalidasi
  salin frame terakhir + metadata + konfigurasi versinya secara konsisten
  bila frame/config gagal: kembalikan valid=false, count/k=null, reason
  inferensi satu frame utuh; petakan koordinat hasil ke frame asli
  saring kelas car, motorcycle, bus, truck
  hitung objek dengan bottom-center dalam/pada batas ROI
  hitung k=1000*N/(L_m*m)
  kembalikan identitas, versi, count/k, valid=true, reason=null
```

## 4. Aturan ROI dan kepadatan

Untuk bbox `(x1,y1,x2,y2)`, titik acuan `p=((x1+x2)/2,y2)`. Hitung bila p di dalam **atau tepat pada batas** poligon. Bbox yang hanya beririsan dengan ROI tetapi p di luar tidak dihitung. Lakukan pemeriksaan setelah mengembalikan koordinat resize/letterbox ke bidang frame asli. Hasil hitungan integer; pembulatan k hanya untuk tampilan, sementara kategori memakai nilai hitung sebelum pembulatan tampilan.

`N = N_car + N_motorcycle + N_bus + N_truck` dan `k = 1000 × N / (L_m × m)`.

Contoh aritmetika demonstrasi: N=6, L_m=100, m=2 menghasilkan k=30 kendaraan/km/lajur. Frame valid kosong menghasilkan N=0 dan k=0. Frame gagal atau masukan panjang/lajur tidak sah menghasilkan valid=false dan nilai null; tidak dianggap lengang.

Penghitungan manual menggunakan frame, dimensi, kelas, ROI dan aturan titik yang sama. Kualitas anotasi yang tidak memungkinkan manual pasti dicatat dan diperiksa ulang, bukan diisi nol.

## 5. Rencana sampel dan pemisahan data

| Kamera | Kalibrasi | Pengujian terpisah | Total rencana |
|---|---|---|---|
| A | 5 pagi + 5 siang + 5 sore =15 | 5 pagi + 5 siang + 5 sore =15 | 30 |
| B | 15 dengan pembagian sama | 15 dengan pembagian sama | 30 |
| C | 15 dengan pembagian sama | 15 dengan pembagian sama | 30 |
| Jumlah | 45 | 45 | 90 siklus |

Satu baris template adalah satu siklus pengamatan satu kamera, bukan satu kendaraan. Hari pengambilan **uji berbeda dari kalibrasi** untuk kamera bersangkutan; catat tanggal rekaman, bukan sekadar tanggal anotasi. Rekaman lanjutan untuk kelompok yang sama tetap satu sampel/split, tidak dipecah menjadi sampel uji baru.

Periksa jumlah kategori rendah/sedang/tinggi per kamera setelah ambang kalibrasi terbentuk. Rencana 15 sampel tidak menjamin setiap kategori cukup. Tambahkan data kalibrasi bila kelompok tidak kosong/pusat berbeda/keterwakilan belum terpenuhi. Catat tambahan dan alasannya. Bila sebuah siklus tidak layak untuk hitungan manual, simpan alasan dan kumpulkan pengganti; jangan menghapus jejak data gagal atau menukar split diam-diam.

Pemilihan model/setting menggunakan data pengembangan/kalibrasi, kemudian bekukan sebelum uji. Jika data uji dipakai tuning, tandai sebagai pengembangan versi baru dan sediakan data uji lain yang tetap terpisah. Identitas dataset, model, inferensi, pengamatan dan parameter membedakan versi evaluasi.

## 6. Langkah pengamatan satu siklus

1. Ikrom/Rizky menetapkan sample_id, dataset_group, kamera, sumber/rekaman, tanggal dan periode. Pastikan video memuat garis henti dan keadaan sinyal pendekat yang dapat ditentukan; bila hijau aktual tidak dapat diidentifikasi, catat keterbatasannya dan cari bahan yang layak untuk analisis layanan.
2. Tentukan awal hijau aktual dari rekaman pendekat tersebut. Ambil frame utuh sekitar **5 detik sebelumnya**. Catat offset frame, offset awal hijau dan selisih aktual; jangan menyatakan tepat 5 detik bila kenyataannya berbeda.
3. Hitung manual empat kelas pada frame kepadatan dengan ROI yang disepakati. Jalankan AI pada frame yang sama dengan versi beku untuk pembandingan. Simpan frame/anotasi, jumlah per kelas, total, panjang/lajur, dan k manual/AI.
4. Pada awal hijau aktual, tandai kendaraan yang **sudah mengantre di dalam ROI**. Beri initial_group_id dan catat initial_queue_count terpisah dari jumlah frame sebelumnya. Kendaraan yang datang setelah penandaan tidak ditambahkan. Untuk beberapa lajur, ikuti seluruh anggota kelompok awal.
5. Ikuti kelompok sampai anggota terakhir melewati garis henti. Catat interval hijau lengkap dan offset penyelesaian. Jika belum selesai pada hijau pertama, lanjutkan hijau berikutnya hanya selama identitas kelompok yang sama masih dapat dipastikan. Kuning/merah tidak masuk akumulasi.
6. Tentukan status penyelesaian dan batas informasi. Simpan bukti, green_segments_json dan hasil layanan. Jika identitas hilang/rekaman putus, waktu selesai tetap kosong dan statusnya tidak dianggap berhasil.
7. Reviewer memeriksa frame, anotasi, sinyal, identitas kelompok, perhitungan dan split. Perubahan manual dicatat; angka asli tidak diganti tanpa jejak alasan.

Langkah di atas untuk dataset rekaman. Pada operasi prototipe, pemilihan frame dipicu ESP32 saat sisa hijau virtual 1 detik; hijau berikutnya nominal sekitar 5 detik sesudah pemicu. Kesesuaian saat runtime diperiksa lewat ID/time ESP32, bukan menganggap tiga CCTV berbeda mengikuti LED fisik.

## 7. Waktu layanan dan ketidakpastian

Jika selesai pada hijau ke-r, `T_i = jumlah durasi hijau penuh sebelum r + waktu dari awal hijau r sampai kendaraan terakhir lewat`. Waktu awal bergerak sudah tercakup dalam pengamatan, sehingga tidak ditambah ulang.

Contoh demonstrasi: kelompok memakai hijau pertama 20 detik dan selesai pada detik 7 hijau kedua. T=27 detik; interval merah/kuning di antaranya dikeluarkan. Seluruh interval dan titik selesai dirujuk ke rekaman yang sama atau rangkaian rekaman yang identitas/waktunya jelas.

| completion_status | service_time_s | Perlakuan cakupan |
|---|---|---|
| `complete_green` | Akumulasi hijau terverifikasi sampai selesai | Berhasil bila T_i ≤ g evaluasi |
| `empty_verified` | 0 hanya bila kelompok awal memang kosong dan teramati | Berhasil pada g sah |
| `incomplete_observed` | Kosong; batas bawah diketahui bila dapat diukur | Tetap penyebut, belum terverifikasi berhasil |
| `untraceable` | Kosong | Tetap penyebut, bukan berhasil |
| `recording_interrupted` | Kosong | Tetap penyebut, bukan berhasil |
| `completed_non_green` | Kosong; peristiwa kuning/merah dicatat | Tidak membuat waktu selesai hijau; belum terverifikasi berhasil |
| `unobserved` | Kosong, sebabnya dicatat | Tetap penyebut sampel layanan yang dipilih dan berkategori sah |

`observed_green_sum_s` dan `service_lower_bound_s` dapat merekam informasi parsial; keduanya tidak menjadi T_i lengkap. Siklus dengan kategori manual sah yang dipilih untuk analisis layanan tetap dipertahankan saat penyelesaian belum pasti. Baris yang tidak memiliki hitungan/frame manual sah tidak mempunyai kategori acuan; dilaporkan terpisah beserta alasan/pengganti, tidak diklaim sebagai sampel kategori tertentu.

## 8. Kalibrasi kategori dan durasi — antarmuka ke Putu

1. Per kamera, hitung k manual pada split kalibrasi saja. Jalankan K-means 1D dengan k=3; simpan versi dataset, setting seed/n_init/max_iter/tol, label anggota, pusat, jumlah dan rentang kelompok.
2. Syarat: ketiga kelompok tidak kosong dan pusat berbeda. Urutkan μ1<μ2<μ3. Tetapkan K1=(μ1+μ2)/2 dan K2=(μ2+μ3)/2. Bila data tidak memenuhi, lengkapi kalibrasi, bukan membuat ambang perkiraan seolah hasil ukur.
3. Kategori rendah: 0≤k<K1; sedang: K1≤k<K2; tinggi: k≥K2. Kategori acuan uji menggunakan k manual dan **ambang beku yang sama** dengan sistem.
4. Per kamera/kategori dengan semua T_i lengkap, urutkan T; r=ceil(0,90×n); kandidat detik penuh `g_raw=ceil(T_(r))`. Bila ada penyelesaian belum pasti, jangan menghitung P90 hanya dari sampel lengkap lalu mengabaikan yang lain.
5. Untuk kandidat g, cakupan=100×jumlah sampel terverifikasi selesai dengan T_i≤g / seluruh sampel layanan kategori tersebut. Sampel belum pasti tetap penyebut. Pilih kandidat detik penuh terkecil yang terbukti ≥90%; bila tidak terbukti, tambah pengamatan kalibrasi dan beri status belum tervalidasi.
6. Susun `g_rendah=g_raw_rendah`, `g_sedang=max(g_raw_sedang,g_rendah)`, `g_tinggi=max(g_raw_tinggi,g_sedang)`. Tetapkan base=g_rendah dan tambahan kategori=selisih dari base, lalu clamp ke min/max yang disepakati. Periksa kembali cakupan pada **durasi akhir**, karena batas maksimum dapat menurunkannya.
7. Bekukan versi hasil, termasuk durasi statis lokal terverifikasi. Operasi hanya membaca ambang/parameter; tidak mengulang K-means/P90 tiap pemicu. Cakupan kalibrasi dan uji dilaporkan terpisah per kamera/kategori. Kategori tanpa sampel diberi belum dapat dinilai.

## 9. Evaluasi dan keluaran pekerjaan

MAE dan E_N dihitung per kamera pada frame uji yang sama; E_N memakai jumlah selisih absolut per frame, bukan selisih total yang saling meniadakan. Target E_N ≤10%. Jika total manual nol, E_N tidak terdefinisi dan dilaporkan bersama MAE/kesesuaian nol. Laporkan confusion matrix, akurasi kategori dan jumlah per kategori; tidak ada ambang akurasi baru dalam LLD. Cakupan final dibandingkan sasaran ≥90% per kamera/kategori dengan ketidakpastian tetap terlihat.

| Keluaran / lokasi penuh | PIC / tahap |
|---|---|
| `KELOMPOK-10/data/templates/kalibrasi.csv`, `pengujian.csv` dan `README.md` | Ikrom; format minggu 3, data aktual saat pengamatan |
| `KELOMPOK-10/configs/cameras.example.json`, `docs/operasional/konfigurasi-kamera.md` | Rizky; konfigurasi aktual minggu 6 |
| `KELOMPOK-10/models/manifest.csv` dan bukti pemilihan YOLO | Rizky; lingkungan/implementasi |
| Parameter beku dan laporan kalibrasi | Putu bersama Rizky/Ikrom; kalibrasi sebelum evaluasi |
| `KELOMPOK-10/docs/pengujian/rencana-uji.md` | Ikrom; UJI-02–UJI-11 dan UJI-29–UJI-34 |

Dokumen sumber masih mengandung instruksi editorial pada Subbab 5.3 dan perbedaan istilah jumlah frame/kelompok awal. Prosedur ini merinci operasionalnya tanpa mengubah berkas minggu 1/2; Nicy mencatat penyelarasan naskah dan ruang lingkup pembanding detektor pada indeks/tindak lanjut.
