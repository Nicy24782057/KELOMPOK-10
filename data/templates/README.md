# Panduan template kalibrasi dan pengujian

| Identitas | Nilai |
|---|---|
| Tim / sprint / minggu | KELOMPOK-10 / S01 / 3 |
| Tugas / PIC | W03-T05 / Ikrom Safei |
| Versi / tanggal | 0.1 / 29 Oktober 2026 |
| Status | Dua template header kosong; belum memuat pengamatan aktual |
| Lokasi | `KELOMPOK-10/data/templates/README.md` |

## 1. Berkas dan aturan pengisian

`KELOMPOK-10/data/templates/kalibrasi.csv` dan `KELOMPOK-10/data/templates/pengujian.csv` memakai header identik. Salin ke lokasi data kerja saat pengamatan; pertahankan template kosong sebagai format. Satu baris merepresentasikan satu siklus satu kamera. Jangan menambahkan baris demonstrasi ke dataset aktual.

CSV memakai UTF-8, delimiter koma, titik desimal, satu header, tanpa baris judul di atas. Kutip teks yang mengandung koma, kutip atau newline sesuai CSV; kutip ganda di dalam field digandakan. Nilai tidak tersedia dibiarkan kosong, berbeda dari angka 0. Boolean ditulis true/false. Timestamp RFC3339 ber-offset; tanggal YYYY-MM-DD. Jangan memasukkan token/kredensial ke kolom rujukan sumber.

Rencana setiap kamera: 15 kalibrasi (5 pagi/5 siang/5 sore) dan 15 uji pada hari berbeda dengan pembagian sama. Total 45+45=90 siklus. Catat jumlah/kategori aktual dan kebutuhan tambahan; jumlah rencana tidak membuktikan kecukupan kategori.

## 2. Kamus kolom

| Kolom | Tipe / satuan | Aturan pengisian |
|---|---|---|
| `sample_id` | Teks unik | Identitas satu siklus satu kamera; tidak dipakai ulang. |
| `dataset_group` | kalibrasi / pengujian | Sesuai nama CSV dan split yang dibekukan. |
| `camera_id` | Teks | cctv-A/B/C aktual sesuai konfigurasi. |
| `phase` | A / B / C | Pemetaan fase virtual kamera. |
| `source_id` | Teks | Identitas sumber CCTV; alamat berkredensial disimpan privat. |
| `recording_id` | Teks | Identitas rekaman; segmen lanjutan tetap satu sample_id. |
| `recording_date` | YYYY-MM-DD | Tanggal rekaman lokal; hari uji berbeda dari kalibrasi. |
| `period` | pagi / siang / sore | Periode pengamatan; batas jam dicatat konsisten pada metadata sumber. |
| `observer` | Teks | Pelaksana anotasi/pengamatan aktual. |
| `recording_path` | Path/rujukan | Lokasi rekaman yang dapat ditemukan reviewer. |
| `frame_path` | Path/rujukan | Frame utuh yang sama untuk AI/manual. |
| `frame_width_px` | Integer positif | Lebar frame asli piksel. |
| `frame_height_px` | Integer positif | Tinggi frame asli piksel. |
| `frame_offset_s` | Detik ≥0 | Posisi frame pada rekaman yang dirujuk. |
| `green_start_offset_s` | Detik ≥0 | Awal hijau aktual pada rekaman yang sama. |
| `frame_source_ts` | RFC3339 atau kosong | Timestamp sumber bila tersedia; tidak diganti waktu anotasi. |
| `frame_received_ts` | RFC3339 atau kosong | Waktu penerimaan server bila tersedia; bukan waktu sumber. |
| `green_start_source_ts` | RFC3339 atau kosong | Awal hijau aktual bila jam sumber diketahui. |
| `frame_to_green_s` | Detik | green_start_offset_s − frame_offset_s pada dasar waktu sama, target sekitar 5. |
| `time_basis` | source_timestamp / recording_offset | Dasar interval; jangan kurangi jam yang tidak sebanding. |
| `config_version` | Teks | Versi konfigurasi sumber/panjang/lajur. |
| `roi_version` | Teks | Versi poligon dan bidang koordinat. |
| `length_m` | Angka >0 | Panjang pengamatan meter, patokan dan bukti ukur pada metadata. |
| `lanes` | Integer >0 | Jumlah lajur searah dengan panjang setara. |
| `frame_valid` | true / false | Kelayakan frame untuk pasangan manual/AI; alasan wajib bila false. |
| `invalid_reason` | Teks atau kosong | Kegagalan sumber/decoding/dimensi/umur/config/anotasi. |
| `manual_car` | Integer ≥0 | Mobil pada frame dengan aturan ROI. |
| `manual_motorcycle` | Integer ≥0 | Sepeda motor pada frame dengan aturan ROI. |
| `manual_bus` | Integer ≥0 | Bus pada frame dengan aturan ROI. |
| `manual_truck` | Integer ≥0 | Truk pada frame dengan aturan ROI. |
| `manual_total` | Integer ≥0 | Jumlah empat hitungan manual. |
| `ai_valid` | true / false / kosong | Status AI; false memerlukan ai_reason dan seluruh nilai AI kosong. |
| `ai_reason` | Teks atau kosong | Sebab inferensi/pengukuran tidak sah; tidak diubah menjadi nol. |
| `ai_car` | Integer ≥0 atau kosong | Hitungan mobil dari AI pada frame yang sama. |
| `ai_motorcycle` | Integer ≥0 atau kosong | Hitungan motor dari AI pada frame yang sama. |
| `ai_bus` | Integer ≥0 atau kosong | Hitungan bus dari AI pada frame yang sama. |
| `ai_truck` | Integer ≥0 atau kosong | Hitungan truk dari AI pada frame yang sama. |
| `ai_total` | Integer ≥0 atau kosong | Jumlah empat kelas AI jika ai_valid=true. |
| `manual_density_k` | Angka ≥0 atau kosong | 1000*manual_total/(length_m*lanes). |
| `ai_density_k` | Angka ≥0 atau kosong | 1000*ai_total/(length_m*lanes) jika AI sah. |
| `density_unit` | kendaraan/km/lajur | Satuan yang sama dengan kontrak pesan. |
| `model_version` | Teks atau kosong | Varian/bobot model aktual yang diuji; bukan label YOLO demo. |
| `inference_version` | Teks atau kosong | Setting inferensi/pustaka/device yang dapat ditelusuri. |
| `parameter_version` | Teks atau kosong | Versi ambang/durasi beku; kosong sebelum kalibrasi, jangan menebak kategori. |
| `manual_category` | rendah / sedang / tinggi / kosong | Dari k manual dan ambang versi yang dicatat. |
| `ai_category` | rendah / sedang / tinggi / kosong | Dari k AI dan ambang yang sama. |
| `initial_group_id` | Teks atau kosong | Identitas kelompok yang sudah antre pada awal hijau aktual. |
| `initial_queue_count` | Integer ≥0 atau kosong | Jumlah kelompok awal terpisah dari manual_total/ai_total frame sebelumnya. |
| `initial_queue_note` | Teks | Penandaan anggota/lajur dan aturan membedakan pendatang baru. |
| `green_segments_json` | JSON array atau kosong | Daftar interval hijau dan batas yang diamati/digunakan, lihat contoh di bawah. |
| `observed_green_sum_s` | Detik ≥0 atau kosong | Akumulasi hijau teramati, dapat parsial; bukan waktu selesai otomatis. |
| `completion_status` | Enum status | complete_green, empty_verified, incomplete_observed, untraceable, recording_interrupted, completed_non_green, unobserved. |
| `completion_green_index` | Integer ≥1 atau kosong | Urutan hijau penyelesaian, hanya complete_green. |
| `completion_offset_s` | Detik ≥0 atau kosong | Offset rekaman saat anggota terakhir lewat; konteks sinyal dijelaskan. |
| `service_time_s` | Detik ≥0 atau kosong | T_i lengkap, hanya complete_green atau empty_verified; kosong bila belum pasti. |
| `service_lower_bound_s` | Detik ≥0 atau kosong | Batas bawah yang benar-benar didukung pengamatan parsial; bukan T_i pasti. |
| `observation_limit_reason` | Teks atau kosong | Sebab keterbatasan/hilang identitas/sinyal tidak diketahui; jangan membuat selesai fiktif. |
| `evaluated_green_s` | Integer positif atau kosong | Durasi akhir kategori setelah pengurutan/clamp, dari parameter_version. |
| `completion_within_evaluated_green` | true / false / kosong | True hanya selesai terverifikasi dan T_i≤g; unknown=false untuk cakupan, kosong jika g/kategori belum tersedia. |
| `service_evidence_path` | Path/rujukan | Video/anotasi yang mendukung seluruh interval dan penyelesaian/status. |
| `annotation_path` | Path/rujukan | Anotasi frame, identitas kelompok dan jejak koreksi manual. |
| `reviewer` | Teks atau kosong | Pemeriksa aktual, tidak diisi sebelum memeriksa. |
| `review_status` | belum_direview / diperiksa / perlu_perbaikan | Status aktual pencatatan, bukan status lulus sistem. |
| `notes` | Teks | Catatan kondisi/kasus sulit, alasan pengganti dan keterwakilan kategori. |

## 3. Interval hijau dan layanan

`green_segments_json` menyimpan daftar interval hijau. `start_offset_s`/`end_offset_s` adalah batas hijau penuh pada rekaman; `used_until_offset_s` adalah batas sampai selesai atau sampai observasi terputus. Urutan harus meningkat dan start ≤ used_until ≤ end. Jika batas akhir hijau tidak terlihat, `end_offset_s` boleh null disertai alasan; jangan membuat batas akhir rekaan.

Contoh **demonstrasi**, tidak terdapat dalam CSV kosong:

```json
[
  {"green_index": 1, "start_offset_s": 100, "end_offset_s": 120, "used_until_offset_s": 120},
  {"green_index": 2, "start_offset_s": 160, "end_offset_s": 180, "used_until_offset_s": 167}
]
```

Jika anggota terakhir terverifikasi lewat saat offset 167 pada hijau kedua, T=20+7=27 detik, completion_status=complete_green. Merah/kuning antara 120–160 tidak dijumlahkan. Jika kelompok hilang pada offset 165, T lengkap kosong; observed_green_sum dapat 25 detik dan status untraceable, dengan batas bawah hanya bila benar-benar dapat disimpulkan dari pengamatan.

Kelompok kosong yang terverifikasi pada awal hijau memakai empty_verified, initial_queue_count=0 dan service_time_s=0. Count frame lima detik sebelumnya tetap diisi berdasarkan frame; tidak otomatis disalin ke initial_queue_count. Penyelesaian saat kuning/merah memakai completed_non_green, service_time_s kosong, dan alasan/peristiwa dicatat.

## 4. Validasi data sebelum analisis

1. sample_id unik; kamera/fase/versi cocok; tanggal rekaman uji berbeda dari kalibrasi. Rekaman lanjutan kelompok yang sama tidak menjadi sampel baru/split lain.
2. Jika frame_valid=true, dimensi/ROI/panjang/lajur serta manual_total sah. manual_total sama jumlah empat kelas. Frame tidak layak tidak menjadi nol; alasan dicatat dan pengganti ditautkan.
3. ai_valid=true memerlukan empat kelas/total/density dan versi; ai_valid=false mengosongkan nilai AI dan menyimpan alasan. Baris gagal AI tetap dilaporkan agar metrik tidak menyembunyikan kegagalan inferensi.
4. Kepadatan memakai rumus yang sama dan kategori memakai K1/K2 beku yang sama. Jangan mengisi parameter/kategori sebelum hasil tersedia; tambahkan hasil pada salinan analisis berversi sambil mempertahankan catatan mentah.
5. Interval, awal hijau, frame, completion dan bukti memakai dasar waktu yang sama. frame_to_green_s dicatat aktual; batas selang yang dapat diterima ditetapkan sebelum pengamatan/uji, bukan sesudah melihat hasil.
6. service_time_s hanya untuk complete_green/empty_verified. Penyelesaian belum pasti tidak diisi batas bawah sebagai waktu selesai. Sampel layanan berkategori sah tetap masuk penyebut cakupan; data tidak layak kategori dilaporkan terpisah, bukan diam-diam dihapus.
7. completion_within_evaluated_green merupakan hasil analisis: true hanya bila T lengkap ≤g final, false bila T>g atau completion belum pasti, kosong bila g/kategori belum tersedia. Kategori tanpa sampel tidak memperoleh 100%.
8. Reviewer mengisi nama/status setelah pemeriksaan aktual. Simpan riwayat koreksi, rujukan bukti dan keterbatasan di notes/annotation_path.

## 5. Perhitungan dan hubungan dokumen

E_N per kamera = 100×Σ|N_AI−N_manual|/ΣN_manual; MAE=Σ|N_AI−N_manual|/n untuk pasangan valid yang dilaporkan bersama jumlah kegagalan AI/data. Total manual nol membuat E_N tidak terdefinisi. Cakupan per kamera/kategori =100×jumlah complete_green/empty_verified dengan T≤g final / seluruh sampel layanan berkategori sah yang dipilih. Unknown tetap penyebut, bukan keberhasilan.

Rincian observasi/kalibrasi: `KELOMPOK-10/docs/perencanaan/prosedur-ai-dan-pengamatan.md`. Skenario dan bukti UJI-06/UJI-29–UJI-34: `KELOMPOK-10/docs/pengujian/rencana-uji.md`. Template tidak mengandung formula Excel agar tetap data mentah yang mudah diimpor; perhitungan analisis berikutnya harus menyimpan rumus/kode dan versi yang dapat diaudit.
