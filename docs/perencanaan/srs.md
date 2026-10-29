# Spesifikasi Kebutuhan Sistem

## Identitas dokumen

| Keterangan | Isi |
|---|---|
| Proyek | Estimasi Kepadatan Kendaraan dari CCTV untuk Pengendalian Lampu Lalu Lintas Adaptif pada Prototipe IoT |
| Tim | KELOMPOK-10 |
| PIC penyusunan | Nicy Putra Pratama — Project Lead dan System Analyst |
| Kode pekerjaan | S01, minggu 1, W01-T01 |
| Versi dokumen | 0.1 |
| Tanggal penyusunan draf | 29 Oktober 2026 |
| Status | Draf untuk pemeriksaan |
| Lokasi pengumpulan | `KELOMPOK-10/docs/perencanaan/srs.md` |
| Acuan utama | Proposal sempro `FINAL INI A(1).docx` yang diberikan pengguna |

Dokumen ini menetapkan kebutuhan prototipe, sumber daya, data, antarmuka, waktu pengembangan, jasa, dan maintenance sebagai dasar perancangan serta pengujian. Kode KF, KNF, dan KJ dipertahankan dari proposal sempro agar kebutuhan dapat ditelusuri ke pekerjaan dan kasus uji. Pilihan implementasi yang belum ditentukan serta bagian naskah yang belum konsisten dicatat pada daftar keputusan terbuka.

## 1. Tujuan dan acuan

### 1.1 Tujuan

SRS digunakan oleh anggota tim untuk menyusun HLD/LLD, mengembangkan modul, merakit perangkat, mengintegrasikan sistem, menyusun pengujian, dan menyiapkan pemeliharaan. Dosen pembimbing/penguji serta pengguna prototipe dapat menggunakannya untuk menilai kesesuaian hasil terhadap ruang lingkup proyek.

### 1.2 Sumber kebutuhan

| Bagian proposal sempro | Penggunaan dalam SRS ini |
|---|---|
| Sampul dan Bab 1 | Identitas, tujuan, ruang lingkup, batasan, dan manfaat prototipe. |
| Subbab 2.1–2.4 | Peran tim, jadwal, sumber daya, cakupan jasa, RAB, dan maintenance. |
| Bab 4 | KF-01–KF-11, KNF-01–KNF-12, KJ-01–KJ-10, perangkat, server, software, antarmuka, dan data. |
| Bab 5, khususnya Subbab 5.3 | Penjelasan operasional ROI, kalibrasi, waktu layanan, kategori, durasi, dan pengendalian. |
| Bab 6 | Verifikasi kebutuhan dan kriteria hasil pengujian. |

Judul pada identitas mengikuti sampul proposal yang dilampirkan. Referensi teknis dan daftar pustaka yang mendasari proposal tetap merujuk naskah sempro tersebut. Perbedaan judul pada bagian tertentu dicatat pada keputusan terbuka; dokumen sumber tidak diubah melalui penyusunan SRS ini.

**Identitas berkas sumber:** SHA-256 `455b591d246bc375a5fefe5ba834ebebb7e38d695a5f8c5d87e61a7bc5b90f15`.

### 1.3 Istilah utama

| Istilah | Pengertian |
|---|---|
| SRS | System Requirements Specification; spesifikasi kebutuhan sistem. |
| KF / KNF / KJ | Kebutuhan Fungsional / Kebutuhan Nonfungsional / Kebutuhan Jasa. |
| HLD / LLD / STP | High-Level Design / Low-Level Design / System Test Plan. |
| YOLO | You Only Look Once; keluarga model deteksi objek. Varian dipilih saat implementasi. |
| ROI | Region of Interest; area pengamatan dan penyaringan objek pada frame. |
| Frame / bounding box | Satu gambar video / kotak koordinat hasil deteksi objek. |
| Fase virtual A/B/C | Tiga giliran prototipe yang masing-masing dipetakan ke sumber CCTV dari lokasi berbeda. |
| MQTT / QoS | Protokol publish–subscribe / Quality of Service pada pengiriman pesan. |
| ACK aplikasi | Pesan penerimaan atau penolakan kandidat rencana pada tingkat aplikasi. |
| Statis cadangan | Pengendalian dengan durasi tetap yang tersimpan pada ESP32. |
| Merah bersama | Interval perpindahan ketika semua fase berwarna merah. |
| MAE / E_N | Rata-rata kesalahan absolut / galat absolut ternormalisasi hitungan kendaraan. |
| K-means / P90 | Pengelompokan kepadatan kalibrasi / persentil ke-90 waktu layanan lengkap. |

## 2. Deskripsi umum dan ruang lingkup

### 2.1 Tujuan produk

Prototipe menggunakan informasi kendaraan pada CCTV untuk mengestimasi kepadatan sesaat dan menyiapkan durasi hijau fase berikutnya. Hasil pengembangan dievaluasi terhadap hitungan manual, kategori acuan, kecukupan durasi layanan, waktu respons, serta pelaksanaan pengendalian pada perangkat.

Kondisi acuan adalah pengendalian menggunakan durasi tetap. Kebutuhan yang ditangani adalah penggunaan informasi kendaraan pada area pengamatan untuk memperbarui rencana durasi hijau setiap giliran prototipe.

### 2.2 Pembagian fungsi sistem

| Komponen | Fungsi yang dibutuhkan |
|---|---|
| Tiga sumber CCTV | Menyediakan video tiga lokasi yang dipetakan ke fase virtual A, B, dan C. |
| Modul AI pada satu server | Membaca CCTV, memilih frame, mendeteksi kendaraan menggunakan YOLO, menghitung objek dalam ROI, dan menghitung kepadatan. |
| Backend pada server yang sama | Menggunakan parameter kalibrasi untuk kategori/durasi, memvalidasi pengukuran dan identitas, serta bertukar pesan dengan perangkat. |
| ESP32 | Mengirim pemicu, menerima rencana, menjalankan urutan/timer lampu, mengunci keputusan, menyediakan statis cadangan, dan mengirim status. |
| Sembilan LED dan OLED | Menampilkan keadaan tiga fase dan informasi pengendalian. |
| Mosquitto | Menyediakan broker MQTT. |
| Node-RED dan InfluxDB | Mengalirkan dan menyimpan data pengukuran, rencana, ACK, mode, serta status secara persisten. |

AI dan backend berjalan langsung pada Ubuntu. Mosquitto, Node-RED, dan InfluxDB dijalankan melalui Docker pada server tersebut. Server dapat ditempatkan pada cloud atau lingkungan pengguna. Rancangan antarmodul dan pin diperinci pada HLD/LLD.

### 2.3 Ruang lingkup dan batasan

- Produk merupakan prototipe untuk riset, demonstrasi, dan uji coba dengan sembilan LED serta tiga fase virtual. Ketiga CCTV berasal dari lokasi berbeda.
- Pengamatan visual dilakukan pada pagi, siang, dan sore dengan pencahayaan yang memungkinkan identifikasi kendaraan dan acuan manual. Pengamatan malam hari berada di luar cakupan pengujian.
- Setiap sumber mengamati pendekat lurus dengan arus searah menuju garis henti. ROI mencakup bagian jalan yang terlihat dan dapat diamati, dari sekitar garis henti ke arah belakang.
- Area belok, putar balik, arus berlawanan, jalan melengkung, dan area konflik persimpangan dikeluarkan dari ROI. Panjang pengamatan dan lajur ditetapkan per kamera.
- Deteksi menggunakan YOLO untuk mobil, sepeda motor, bus, dan truk. Varian, bobot, serta konfigurasi inferensi ditentukan saat implementasi berdasarkan ketepatan hitungan, waktu, dan sumber daya.
- Setiap kendaraan yang memenuhi aturan ROI dihitung satu, baik berhenti maupun bergerak, tanpa pembobotan SMP/PCE dan tanpa akumulasi hitungan antarframe.
- Penyesuaian berlaku pada durasi hijau. Urutan A–B–C–A, kuning nominal tiga detik, dan merah bersama nominal satu detik dipertahankan.
- Pengujian prototipe menilai pengolahan serta pelaksanaan pengendalian. Penerapan langsung pada persimpangan jalan umum berada di luar lingkup; dampak penurunan kemacetan, waktu tunggu, atau peningkatan keselamatan nyata belum menjadi hasil yang dapat disimpulkan dari evaluasi ini.
- Kualitas gambar, pencahayaan, sudut pandang, kendaraan yang saling menutupi, keterlambatan stream, jaringan, dan ketersediaan daya menjadi kondisi yang dicatat dalam pengujian.

### 2.4 Pengguna dan tanggung jawab tim

Pengguna prototipe mengamati keluaran lampu, durasi, kepadatan, serta mode untuk kegiatan riset/demonstrasi/uji coba. Teknisi menyiapkan konfigurasi, memeriksa data, menguji sistem, dan melakukan maintenance sesuai tanggung jawab modul.

| Anggota | Tanggung jawab kebutuhan/implementasi |
|---|---|
| Nicy Putra Pratama | Analisis kebutuhan, koordinasi, penyelarasan rancangan, pemantauan, dan pemeriksaan kesesuaian hasil. |
| Rizky Bintang Fadillah | CCTV, ROI, YOLO, hitungan, kepadatan, dan evaluasi AI. |
| Putu Radit Ardika | Kalibrasi kategori/durasi, backend, MQTT, statis cadangan, dan integrasi. |
| Ramdhani / Dhani | Rangkaian, ESP32, lampu, OLED, firmware, dan pelaksanaan pengendalian. |
| Ikrom Safei | Data/acuan manual, pencatatan, skenario pengujian, bukti, dan laporan. |

Pembagian tugas, keluaran, minggu pelaksanaan, serta ketergantungannya diperinci melalui pekerjaan W01-T02 pada `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md`.

## 3. Kebutuhan fungsional

### 3.1 Daftar kebutuhan

Kode dan substansi berikut mempertahankan Tabel 4.3 proposal sempro. Penjelasan berikutnya merinci ketentuan yang sudah dijabarkan pada Bab 4–6 sumber.

| Kode | Kebutuhan | Spesifikasi |
|---|---|---|
| KF-01 | Pembacaan CCTV | Membaca tiga sumber dan menyediakan frame terbaru. Kegagalan pembacaan dibedakan dari kondisi tanpa kendaraan. |
| KF-02 | Konfigurasi pengamatan | Mendukung konfigurasi sumber, pemetaan fase, ROI, panjang pengamatan, dan jumlah lajur. |
| KF-03 | Deteksi dan penghitungan | Menjalankan YOLO pada satu frame utuh saat pemicu. Kendaraan dihitung apabila titik tengah sisi bawah bounding box berada di dalam atau tepat pada batas ROI. |
| KF-04 | Perhitungan kepadatan | Modul AI menghitung kepadatan sesaat rata-rata per lajur dari jumlah kendaraan dalam ROI, panjang pengamatan, dan jumlah lajur searah, dengan satuan kendaraan /km/ lajur. |
| KF-05 | Kategori dan durasi | Backend menentukan kategori rendah, sedang, atau tinggi dan durasi hijau berdasarkan parameter kalibrasi serta batas minimum– maksimum. |
| KF-06 | Pemicu dan rencana | ESP32 mengirim pemicu saat hijau aktif tersisa satu detik. Server memproses CCTV fase berikutnya dan mengirim rencana melalui MQTT. |
| KF-07 | Urutan lampu | Menjalankan A–B–C–A, kuning tiga detik, dan merah bersama satu detik. Paling banyak satu fase berwarna hijau. |
| KF-08 | Informasi OLED | Menampilkan fase, kondisi lampu, sisa waktu, jumlah kendaraan, kepadatan, kategori, dan mode pengendalian. |
| KF-09 | Pencatatan | Mencatat pengukuran, kategori, rencana, ACK aplikasi, mode, dan status. Node-RED mengalirkan data ke InfluxDB. |
| KF-10 | Statis cadangan | Menggunakan durasi statis lokal ketika rencana adaptif valid tidak tersedia saat penguncian, dengan urutan dan transisi tetap. |
| KF-11 | Validasi | Memeriksa konfigurasi, frame, sesi, giliran, dan fase tujuan. Pesan duplikat tidak mengulang pengendalian atau mereset waktu. |

### 3.2 Pengambilan frame dan penghitungan ROI

Untuk memenuhi KF-01–KF-04 serta KF-06:

1. Pembaca menyediakan frame terbaru untuk setiap sumber beserta identitas dan informasi waktunya.
2. Pemicu menentukan sumber kamera fase berikutnya. Satu pemicu yang sah menghasilkan satu pengukuran dari satu frame utuh.
3. Frame/config diperiksa sebelum inferensi: keberhasilan dekode, keberadaan gambar, kesesuaian dimensi dengan ROI, panjang/lajur positif, serta aturan umur frame.
4. Model YOLO dimuat ketika aplikasi disiapkan dan digunakan kembali pada pemicu berikutnya. Pilihan varian/bobot/konfigurasi dicatat sesuai hasil implementasi.
5. Deteksi disaring untuk mobil, sepeda motor, bus, dan truk. Koordinat hasil deteksi serta ROI berada pada bidang frame asli yang sama; perubahan ukuran selama pemrosesan harus diperhitungkan saat pengembalian koordinat.
6. Titik acuan objek adalah tengah sisi bawah bounding box. Objek diterima bila titik tersebut berada di dalam atau tepat pada batas ROI. Irisan bounding box saja tidak cukup jika titik acuannya di luar.

```text
p_x = (x1 + x2) / 2
p_y = y2
```

Jumlah N merupakan kendaraan yang lolos aturan kelas dan ROI pada frame tersebut. Frame valid tanpa kendaraan menghasilkan N = 0. Masukan tidak tersedia/tidak valid ditandai sebagai pengukuran gagal dengan alasan. Jumlah/kepadatan yang tidak tersedia dibedakan dari nol yang sah; representasinya dapat berupa null atau penghilangan field sesuai kontrak LLD, sebagaimana dijelaskan pada sumber.

### 3.3 Perhitungan kepadatan

Untuk memenuhi KF-04, kepadatan sesaat rata-rata per lajur dihitung sebagai berikut:

```text
k = N / (L_km × m)
k = 1000 × N / (L_m × m)
```

N adalah jumlah kendaraan pada satu frame yang memenuhi aturan ROI; L_km atau L_m adalah panjang fisik area pengamatan dalam kilometer atau meter; m adalah jumlah lajur searah. Satuan k adalah kendaraan/km/lajur. Panjang dan jumlah lajur harus positif, serta panjang pengamatan antarlajur yang dihitung bersama harus setara.

### 3.4 Kalibrasi kategori per kamera

Untuk memenuhi KF-05, kalibrasi menggunakan kepadatan yang dihitung dari acuan manual data kalibrasi setiap kamera. K-means satu dimensi membentuk tiga kelompok. Ketiga kelompok harus tidak kosong dan pusatnya berbeda, lalu diurutkan menjadi mu_1 < mu_2 < mu_3.

```text
K1 = (mu_1 + mu_2) / 2
K2 = (mu_2 + mu_3) / 2

Rendah : 0 <= k < K1
Sedang : K1 <= k < K2
Tinggi : k >= K2
```

Pengaturan K-means, identitas dataset, anggota/pusat/rentang kelompok, dan ambang dicatat. Kecukupan serta keterwakilan data diperiksa sebelum parameter dibekukan. Kategori yang belum didukung data memadai dinyatakan belum tervalidasi. Pada operasi per pemicu, backend memakai K1/K2 yang sudah disimpan; K-means dijalankan pada tahap kalibrasi.

### 3.5 Penetapan durasi hijau

Durasi kategori ditetapkan dari pengamatan waktu layanan kelompok antrean awal, terpisah untuk setiap kamera dan kategori. Prosedur pengamatan pada Bagian 8.3 mengatur frame kepadatan, penandaan kelompok awal, akumulasi waktu hijau, dan kepastian penyelesaian.

Jika seluruh waktu layanan kategori diketahui dan jumlah sampel lebih dari nol, gunakan P90 dengan nearest-rank: urutkan waktu, ambil peringkat ceil(0,90 × n), lalu ambil waktu pada peringkat tersebut. Jika ada penyelesaian belum pasti, nilai cakupan terverifikasi; sampel belum pasti tetap berada pada penyebut dan tidak dihitung berhasil.

Pilih kandidat durasi terkecil yang dapat dibuktikan mencapai cakupan sedikitnya 90%. Kategori tanpa sampel belum mempunyai durasi tervalidasi. Apabila sasaran belum dapat dibuktikan, lengkapi pengamatan kalibrasi dan catat status parameter sebelum pembekuan.

Durasi kategori harus tidak menurun dari rendah ke sedang ke tinggi. Untuk operasi, waktu dasar menggunakan durasi kategori rendah dan tambahan kategori merupakan selisih durasi kategori terhadap waktu dasar.

```text
g_usulan = g_dasar + tambahan_kategori
g_akhir  = min(g_maks, max(g_min, g_usulan))
0 < g_min <= g_maks
```

Cakupan dinilai kembali pada durasi akhir setelah pengurutan kategori dan pembatasan minimum–maksimum. Nilai minimum, maksimum, durasi dasar/tambahan, dan statis cadangan ditetapkan serta dicatat melalui proses yang direncanakan, kemudian dibekukan sebelum evaluasi terpisah.

### 3.6 Pemicu, penerimaan rencana, dan penguncian

Untuk memenuhi KF-06, KF-07, KF-10, dan KF-11:

- ESP32 mengirim pemicu fase berikutnya ketika hijau aktif tersisa satu detik, disertai identitas pengendali/sesi/giliran/fase yang diperlukan.
- Server menargetkan rencana valid telah diterima ESP32 paling lama tiga detik sejak pemicu dikirim. Waktu respons diukur dari jam lokal ESP32 pada pengujian terkait.
- Setelah hijau aktif selesai, perangkat menjalankan kuning tiga detik. Durasi, mode, dan data rencana fase berikutnya dikunci sebelum interval merah bersama satu detik dimulai.
- Selang nominal pemicu sampai hijau berikutnya adalah lima detik, tetapi penguncian terjadi sebelum merah bersama, sekitar empat detik dari pemicu. Titik penguncian aktual dicatat pada implementasi.
- Rencana valid yang datang melewati tiga detik namun masih sebelum lock dapat menjadi kandidat giliran sasaran; target respons tetap dicatat tidak terpenuhi.
- Rencana baru yang datang setelah lock ditolak untuk giliran tersebut. Hijau aktif, durasi/mode yang telah dikunci, dan timer tidak dipotong oleh rencana berikutnya.
- Jika kandidat adaptif valid tidak tersedia saat lock, gunakan durasi statis lokal yang sudah diverifikasi. Urutan dan transisi lampu dipertahankan selama ESP32 tetap berfungsi serta mendapat daya.
- Pemulihan adaptif berlaku pada giliran berikutnya yang memenuhi syarat.

### 3.7 Validasi, duplikasi, ACK, dan status

Frame/config, identitas pengendali/sesi/giliran/fase, versi parameter, isi pesan, dan batas durasi harus konsisten untuk satu pemrosesan giliran. Konfigurasi diperiksa terhadap panjang/lajur positif, kesesuaian ROI/dimensi, pemetaan fase, K1 < K2, durasi kategori tidak menurun, dan batas durasi sah.

Pemicu identik yang sedang diproses tidak memulai pemrosesan kedua. Pemicu yang sudah selesai ditangani memakai hasil penanganan sebelumnya; jika rencana tersedia, rencana yang sama dapat dikirim ulang. Rencana identik yang telah ditangani tidak mengubah kandidat, lock, atau timer; respons ACK sebelumnya digunakan kembali sesuai kontrak.

ACK aplikasi menyatakan kandidat diterima atau ditolak beserta alasannya. Status perangkat mencatat rencana, mode, dan fase yang benar-benar dilaksanakan. Penerimaan ACK dan pelaksanaan harus dapat ditelusuri secara terpisah.

### 3.8 Pencatatan dan independensi kendali

Pemicu/pengukuran, kategori, versi parameter, rencana, ACK aplikasi, mode, serta status pelaksanaan dihubungkan melalui identitas dan waktu kejadian. Node-RED mengalirkan data ke InfluxDB. Penyimpanan menggunakan media persisten. Gangguan pencatatan tidak menghalangi urutan lampu ketika jalur pengendalian masih tersedia.

## 4. Kebutuhan nonfungsional

### 4.1 Daftar kebutuhan

Kode dan substansi berikut mempertahankan Tabel 4.5 proposal sempro.

| Kode | Aspek | Kebutuhan |
|---|---|---|
| KNF-01 | Respons | Target penerimaan rencana paling lama tiga detik sejak pemicu ESP32; dibuktikan saat implementasi. |
| KNF-02 | Validitas frame | Menerapkan ambang umur frame yang dapat dikonfigurasi berdasarkan karakteristik sumber. |
| KNF-03 | Evaluasi penghitungan | Membandingkan hitungan sistem dengan manual pada frame yang sama sesuai kriteria Bagian 6. |
| KNF-04 | Konsistensi | Durasi berlaku pada giliran berikutnya; pesan duplikat tidak mereset waktu. |
| KNF-05 | Keandalan cadangan | ESP32 yang tetap berfungsi menjalankan durasi statis lokal ketika rencana valid tidak tersedia. |
| KNF-06 | Keamanan | Menggunakan autentikasi dan TLS serta memisahkan kredensial dari berkas publik. |
| KNF-07 | Ketertelusuran | Menghubungkan pengukuran, rencana, ACK, dan pelaksanaan melalui identitas serta waktu kejadian. |
| KNF-08 | Penyimpanan | Menggunakan penyimpanan persisten untuk data dan konfigurasi penting. |
| KNF-09 | Sumber daya | Mengevaluasi CPU, RAM, GPU, dan penyimpanan ketika seluruh komponen server berjalan bersama. |
| KNF-10 | Reproduksi instalasi | Mencatat versi model, dependensi, layanan, dan konfigurasi. |
| KNF-11 | Kemandirian pengendalian | Kegagalan pencatatan tidak menghambat urutan lampu ketika jalur pengendalian tersedia. |
| KNF-12 | Dokumentasi | Menyediakan panduan konfigurasi, instalasi, penggunaan, integrasi, dan hasil pengujian. |

### 4.2 Kriteria evaluasi yang sudah ditetapkan

| Aspek | Kebutuhan dan ketentuan penilaian |
|---|---|
| Hitungan kendaraan | Hitungan AI dibandingkan dengan manual pada frame/ROI yang sama. Laporkan MAE dan E_N per kamera, jumlah frame valid, serta alasan data tidak dapat dibandingkan. Target E_N <=10% per kamera. |
| Penyebut nol | Bila total hitungan manual nol, E_N tidak dihitung; periksa MAE dan kesesuaian nol. Bila tidak ada frame valid yang dapat dibandingkan, metrik dinyatakan belum dapat dihitung. |
| Kategori | Bandingkan kategori dari kepadatan AI dan manual menggunakan ambang beku kamera yang sama. Laporkan akurasi, matriks kebingungan, serta jumlah sampel setiap kategori per kamera. |
| Layanan kelompok awal | Sasaran cakupan penyelesaian terverifikasi >=90% pada durasi akhir per kamera dan kategori. Pisahkan hasil kalibrasi dan pengujian. Sampel belum pasti tetap pada penyebut dan tidak dihitung berhasil. Kategori tanpa sampel belum dapat dinilai. |
| Respons | Rencana valid diterima paling lama tiga detik sejak pemicu dikirim. Pemicu tanpa rencana valid dalam batas tersebut dilaporkan tidak memenuhi target respons. |
| Fungsi | Hasil aktual harus memenuhi kondisi yang dipersyaratkan kasus terkait, termasuk urutan, lock, validasi, duplikasi, cadangan, pemulihan, OLED, pencatatan, dan keamanan. |
| Timing dan umur frame | Toleransi pengukuran interval dan ambang umur frame ditetapkan sebelum pengujian terkait berdasarkan rancangan serta karakteristik sumber. |
| Sumber daya | CPU, RAM, GPU, penyimpanan, serta respons dicatat ketika tiga pembaca CCTV, AI, backend, dan layanan pendukung berjalan bersama. |

Rumus evaluasi hitungan untuk n frame valid yang dapat dibandingkan:

```text
MAE = jumlah(abs(N_AI_i - N_manual_i)) / n
E_N = 100 × jumlah(abs(N_AI_i - N_manual_i)) / jumlah(N_manual_i)
```

MAE memakai satuan kendaraan per frame. E_N memakai persen dan dinilai per kamera terhadap target. Kesalahan absolut dihitung per frame sebelum dijumlahkan agar lebih dan kurang hitung tidak saling menghilangkan.

Keberhasilan statis cadangan dan kegagalan target respons adaptif dilaporkan menurut aspek masing-masing. Kriteria yang tidak tercapai, data yang belum cukup, serta kategori yang belum diuji tetap dinyatakan pada laporan.

## 5. Kebutuhan sumber daya

### 5.1 Hardware prototipe

Spesifikasi dan jumlah mengikuti Tabel 4.9 proposal sempro. Status ketersediaan/kondisi aktual diperiksa dalam inventaris pada tahap persiapan komponen.

| Perangkat | Spesifikasi dan jumlah | Fungsi |
|---|---|---|
| ESP32 | 1 ESP32-DevKitC V4 dengan ESP32-WROOM-32D | Pengendalian dan komunikasi perangkat. |
| LED dan resistor | Masing-masing 3 LED merah, kuning, dan hijau; 9 resistor 330 Ω, ¼ W | Keluaran tiga fase dan pembatas arus setiap LED. |
| OLED | 1 SSD1306 I²C, 0,96 inci, 128 × 64, mendukung suplai 3,3 V | Informasi pengendalian. |
| Breadboard dan jumper | 1 breadboard 830 titik; 40 pcs female-to-male dan 40 pcs male-to-male | Perakitan dan sambungan. |
| Kabel dan adaptor | 1 kabel USB data; 1 adaptor 5 V DC, 2 A | Pemrograman dan catu daya. |

Pemetaan GPIO, sambungan I2C, resistor, dan skema catu daya diperinci dalam LLD. Rangkaian menggunakan satu sumber catu daya pada satu waktu sesuai rancangan papan. Kemampuan penyediaan arus adaptor dan beban aktual diperiksa pada implementasi.

### 5.2 Server

Kebutuhan awal mengikuti Tabel 4.6 proposal sempro.

| Komponen | Kebutuhan awal |
|---|---|
| Jumlah dan penempatan | Satu server pada layanan cloud atau lingkungan pengguna. |
| Sistem operasi | Ubuntu Server 24.04 LTS. |
| Prosesor dan RAM | Kapasitas setara 4 vCPU dan RAM 16 GiB. |
| GPU | NVIDIA T4 dengan VRAM 16 GB atau GPU NVIDIA berkemampuan sebanding yang mendukung CUDA. |
| Penyimpanan | Minimum 100 GB SSD persisten. |
| Ketersediaan | Tersedia selama prototipe dioperasikan. |
| Acuan layanan | AWS EC2 g4dn.xlarge; biaya mengikuti RAB Bagian 2. |

Acuan kapasitas server menjadi dasar penyiapan lingkungan; kecukupannya diperiksa melalui pengujian beban gabungan, ketepatan penghitungan, dan respons. Penempatan aktual cloud atau lingkungan pengguna ditetapkan dan dicatat sebelum integrasi. Acuan layanan dan biaya mengikuti RAB proposal; pengadaan/penggunaan aktual dicatat tersendiri.

### 5.3 Software dan penempatan

Penempatan mengikuti Tabel 4.7 proposal sempro.

| Penempatan | Komponen | Fungsi |
|---|---|---|
| Host Ubuntu | Driver NVIDIA, pustaka GPU, Python, dan modul AI YOLO | Pembacaan CCTV, deteksi, penghitungan, dan kepadatan. |
| Host Ubuntu | Backend | Kategori, durasi, validasi, dan pertukaran rencana. |
| Host Ubuntu | Docker Engine dan Docker Compose | Pengelolaan container layanan. |
| Container Docker | Mosquitto, Node-RED, dan InfluxDB OSS | Broker MQTT, aliran pencatatan, dan penyimpanan persisten. |
| ESP32 | Firmware | Komunikasi, urutan lampu, OLED, dan statis cadangan. |

Versi Python, model/bobot, pustaka AI/CCTV, driver/CUDA, firmware, container, konfigurasi, dan parameter dicatat sesuai KNF-10. Kompatibilitas serta kemampuan aktual diverifikasi pada lingkungan implementasi.

## 6. Kebutuhan waktu jasa dan maintenance

### 6.1 Daftar kebutuhan layanan

Kode dan substansi berikut mempertahankan Tabel 4.8 proposal sempro.

| Kode | Aspek | Kebutuhan |
|---|---|---|
| KJ-01 | Pengembangan | Pelaksanaan 16 minggu dengan alokasi 958 jam-orang. |
| KJ-02 | Jasa teknis | Analisis, perancangan, pengembangan, perakitan, integrasi, pengujian, perbaikan, dan dokumentasi. |
| KJ-03 | Serah terima | Prototipe, kode, konfigurasi terkait, panduan, dan laporan pengujian. |
| KJ-04 | Periode maintenance | Satu paket layanan 12 bulan setelah serah terima. |
| KJ-05 | Pekerjaan terjadwal | Alokasi 12 jam-orang per bulan untuk pemeriksaan preventif dan administrasi. |
| KJ-06 | Korektif | Alokasi 8 jam-orang per bulan untuk seluruh tim, digunakan sesuai gangguan. |
| KJ-07 | Respons awal | Maksimal satu hari kerja; perkiraan penyelesaian diberikan setelah diagnosis. |
| KJ-08 | Pelaporan | Laporan bulanan memuat pemeriksaan, temuan, tindakan, jam kerja, dan hasil perbaikan. |
| KJ-09 | Pekerjaan tambahan | Pekerjaan di luar cakupan atau alokasi korektif memerlukan estimasi dan kesepakatan tambahan. |
| KJ-10 | Biaya terpisah | Penggantian hardware, penyediaan server, listrik, dan internet diperhitungkan di luar paket maintenance. |

### 6.2 Periode pengembangan

| Tahap | Minggu pengembangan |
|---|---|
| Analisis kebutuhan dan perancangan | 1–3 |
| Persiapan komponen dan lingkungan server | 4 |
| Perakitan prototipe | 5 |
| CCTV, AI, pengamatan, kalibrasi, dan parameter | 6–9 |
| Integrasi pengendalian, pencatatan, dan OLED | 10–11 |
| Pengujian sistem dan evaluasi data terpisah | 12–14 |
| Perbaikan dan pengujian ulang | 15 |
| Dokumentasi dan serah terima | 16 |

Alokasi pekerjaan jasa pengembangan adalah 958 jam-orang selama 16 minggu sesuai proposal. Pelaksanaan aktual dan perubahan rencana dicatat melalui pemantauan progres.

### 6.3 Lingkup maintenance

Layanan 12 bulan dimulai setelah serah terima dan merupakan periode terpisah dari pengembangan. Setiap bulan dialokasikan 12 jam-orang untuk pemeriksaan terjadwal/administrasi serta 8 jam-orang korektif gabungan seluruh tim, digunakan menurut kejadian gangguan.

Pemeriksaan meliputi server/backend, komunikasi, ROI/hasil penghitungan, pencatatan, perangkat fisik, dan statis cadangan. Respons awal maksimal satu hari kerja; estimasi penyelesaian diberikan setelah diagnosis. Laporan memuat pemeriksaan, temuan, tindakan, penggunaan jam, serta verifikasi setelah perbaikan.

Perubahan di luar cakupan atau alokasi korektif memerlukan estimasi dan kesepakatan tambahan. Penggantian hardware, server, listrik, dan internet diperhitungkan terpisah. Rincian biaya layanan serta penyediaan server mengikuti Subbab 2.4 proposal.

## 7. Kebutuhan antarmuka

### 7.1 Antarmuka pengguna

OLED harus menampilkan fase aktif, kondisi lampu, sisa waktu, jumlah kendaraan, kepadatan, kategori, mode, dan satuan kepadatan sesuai kebutuhan KF-08. Susunan akhir disesuaikan dengan layar 128 × 64 piksel.

Data kendaraan mengikuti pengukuran yang digunakan pada rencana giliran aktif. Tampilan merupakan informasi pengendalian dari pengukuran terkait, sedangkan fase/timer menunjukkan keadaan aktual. Data yang tidak tersedia diberi penanda dan dibedakan dari nol kendaraan yang valid. Teknisi meninjau konfigurasi dan catatan melalui perangkat lunak yang tersedia pada server.

### 7.2 Antarmuka fisik

ESP32 mengendalikan sembilan LED melalui GPIO dan terhubung dengan OLED melalui I2C. Koneksi, pemrograman, dan suplai mengikuti spesifikasi hardware pada Bagian 5. Skema/pin serta hasil pemeriksaan sambungan diperinci pada dokumen perangkat dan LLD.

### 7.3 Antarmuka jaringan

- ESP32 menggunakan Wi-Fi 2,4 GHz. Koneksi server dapat melalui jaringan lokal atau internet sesuai penempatan.
- Video CCTV dibaca melalui koneksi sumber video. Protokol/format stream aktual, resolusi, FPS, dan keterlambatan dicatat saat pemeriksaan sumber.
- Pemicu, pengukuran, rencana, ACK aplikasi, dan status menggunakan MQTT dengan payload JSON.
- Rencana dan ACK aplikasi memakai QoS 1; pesan rencana memakai retain false. Sistem menangani kemungkinan duplikasi sesuai KF-11.
- MQTT menggunakan autentikasi dan TLS. Kredensial operasional disimpan terpisah dari berkas publik.
- Nama topic, struktur field, format identitas, versi, dan aturan validasi rinci ditetapkan melalui LLD/kontrak komunikasi pada minggu 3.

Jaringan yang diperlukan disediakan pengguna; tim menangani konfigurasi dan pengujian integrasi sesuai ruang lingkup layanan.

## 8. Kebutuhan data

### 8.1 Kelompok data

Kelompok data mempertahankan Tabel 4.10 proposal sempro. Field terperinci dan struktur penyimpanan dijabarkan melalui LLD.

| Kelompok | Data utama | Bentuk atau satuan |
|---|---|---|
| Konfigurasi pengamatan | Identitas dan alamat CCTV, fase, koordinat ROI, patokan, panjang pengamatan, dan jumlah lajur | Teks, koordinat, meter, bilangan bulat |
| Parameter pengendalian | Batas kategori, waktu dasar, tambahan kategori, batas minimum– maksimum, durasi statis, dan ambang umur frame | Kendaraan/km/lajur dan satuan waktu |
| Hasil pengukuran | Identitas CCTV, waktu frame dan pengukuran, jumlah kendaraan, kepadatan, serta status validitas | Timestamp, kendaraan, kendaraan/km/lajur, status |
| Rencana dan pelaksanaan | Identitas sesi dan giliran, fase tujuan, kategori, durasi, ACK aplikasi, mode, kondisi lampu, dan waktu kejadian | Identitas, kategori, detik, status, timestamp |
| Pengamatan dan kalibrasi | Identitas CCTV dan siklus, panjang ROI, lajur, durasi lampu aktual, jumlah kendaraan awal, waktu layanan kelompok awal, kondisi pengamatan, serta kelompok kalibrasi atau pengujian | Identitas, meter, kendaraan, detik, dan keterangan |

Selain kelompok di atas, identitas versi model, konfigurasi inferensi, konfigurasi pengamatan, dataset, pengaturan K-means, dan parameter pengendalian harus dapat ditelusuri. Catatan pengukuran dan rencana dihubungkan dengan ACK serta status pelaksanaan melalui identitas dan waktu.

### 8.2 Validitas waktu frame

Waktu frame sumber dan waktu penerimaan server dicatat terpisah bila timestamp sumber tersedia. Waktu penerimaan server tidak otomatis menyatakan umur gambar sejak direkam. Dasar pengukuran umur frame dan batas penerimaannya didokumentasikan menurut kemampuan sumber, lalu digunakan konsisten saat pengujian.

### 8.3 Pengamatan kalibrasi dan pengujian

- Rencana pengamatan adalah 30 siklus per kamera: 15 kalibrasi dan 15 pengujian terpisah. Tiga kamera menghasilkan rencana 45 kalibrasi + 45 uji = 90 siklus.
- Masing-masing kelompok data per kamera mencakup lima siklus pagi, lima siang, dan lima sore. Hari pengujian dibedakan dari kalibrasi. Keterwakilan kategori diperiksa; jumlah rencana bukan jaminan kecukupan data setiap kondisi.
- Frame kepadatan dipilih sekitar lima detik sebelum hijau aktual pendekat dimulai. Catat waktu frame, awal hijau, dan selang aktual; hitungan manual memakai frame/ROI yang sama dengan sistem.
- Ketika hijau aktual dimulai, tandai kelompok yang sudah mengantre di dalam ROI. Jumlah kelompok ini dicatat terpisah dari jumlah pada frame kepadatan. Kendaraan yang datang kemudian tidak ditambahkan.
- Ikuti kelompok hingga kendaraan terakhir melewati garis henti. Pada beberapa lajur, gunakan kendaraan terakhir dari seluruh kelompok yang ditandai.
- Jika kelompok belum selesai pada satu hijau, lanjutkan penelusuran pada hijau berikutnya selama identitas kelompok masih dapat dipastikan. Jumlahkan waktu hijau yang digunakan; interval kuning dan merah dikeluarkan dari akumulasi.
- Kelompok tidak terlacak, rekaman terputus, atau penyelesaian tidak pasti diberi status sesuai informasi yang tersedia. Waktu selesai tidak dibuat tanpa dukungan pengamatan. Pada evaluasi cakupan kategori, sampel belum pasti tetap diperhitungkan sebagai tidak terverifikasi berhasil.
- Frame kepadatan, kelompok awal, akumulasi waktu layanan, serta status penyelesaian merupakan data berbeda yang dihubungkan oleh identitas siklus.

Rancangan prosedur di atas mengikuti rincian Subbab 5.3 dan kasus UJI-32–UJI-34. Perbedaan istilah jumlah kendaraan awal pada bagian lain dicatat sebagai penyelarasan naskah pada Bagian 9.

### 8.4 Pembekuan dan pemisahan versi

Model, konfigurasi inferensi/pengamatan, K1/K2, durasi, batas, dan statis cadangan dibekukan sebelum evaluasi akhir. Parameter kategori/durasi ditentukan menggunakan data kalibrasi. Data uji versi tersebut dipertahankan terpisah dari tuning.

Jika data uji dipakai menentukan perubahan, statusnya dicatat sebagai data pengembangan. Evaluasi akhir versi perubahan memakai data uji yang tetap terpisah. Hasil kalibrasi dan pengujian dilaporkan terpisah per kamera/kategori, termasuk jumlah aktual, keterwakilan, data gagal, dan keterbatasan.

## 9. Asumsi ketergantungan dan keputusan terbuka

### 9.1 Asumsi operasional

Sumber CCTV harus dapat diakses server; patokan fisik dan jumlah lajur dapat diidentifikasi. Jaringan, daya, layanan, serta perangkat diperlukan sebelum integrasi terkait. Parameter pengendalian yang sah dan statis lokal terverifikasi tersedia sebelum pengujian operasionalnya. Kondisi tersedia/belum tersedia dicatat pada inventaris dan laporan lingkungan aktual.

### 9.2 Keputusan atau data yang masih perlu dilengkapi

Penanda KT berikut merupakan daftar tindak lanjut dalam draf ini, bukan pengganti kode KF/KNF/KJ pada proposal.

| ID | Hal yang perlu ditetapkan/diselaraskan | PIC tindak lanjut | Waktu penetapan |
|---|---|---|---|
| KT-01 | Varian/bobot YOLO, ukuran input, confidence, NMS, pustaka, dan dukungan komputasi berdasarkan ketepatan, waktu, dan sumber daya. | Rizky; Nicy memeriksa kesesuaian lingkup. | Saat implementasi AI; dicatat sebelum evaluasi akhir. |
| KT-02 | Sumber/pemetaan CCTV, ROI, patokan panjang, lajur, resolusi/FPS/format, timestamp, umur frame, dan ambang validitas. | Rizky; Ikrom mencatat metadata. | Pemeriksaan sumber dan konfigurasi, sebelum pengujian terkait. |
| KT-03 | Pengaturan K-means, kecukupan data, K1/K2, durasi kategori, batas, serta statis cadangan terverifikasi. | Putu; Rizky/Ikrom menyediakan data; Ramdhani memeriksa pelaksanaan statis. | Kalibrasi sebelum pembekuan parameter dan evaluasi terpisah. |
| KT-04 | Pin, rangkaian/catu daya, kontrak topic/field/identitas, serta toleransi pengukuran timing. | Ramdhani dan Putu sesuai modul; Ikrom menyusun verifikasi. | LLD dan penyelesaian implementasi, sebelum pengujian terkait. |
| KT-05 | Penempatan server aktual, versi lingkungan, kondisi jaringan, status ketersediaan hardware, dan kecukupan spesifikasi. | Putu/Rizky/Ramdhani sesuai komponen; Nicy mengoordinasikan. | Persiapan dan pengujian beban/integrasi terkait. |
| KT-06 | Ruang lingkup pembanding non-YOLO berbeda: Subbab 2.1, 4.1.2, dan BMC menyebut perbandingan dengan sekurangnya satu detektor non-YOLO pada frame/perangkat sama; Tabel 1.3 dan Subbab 6.1 menyebut kajian literatur dengan implementasi berfokus pada YOLO. Rumusan perlu diselaraskan sebelum ditetapkan sebagai beban uji. | Nicy bersama Rizky dan tim. | Pemeriksaan kebutuhan sebelum memfinalkan ruang lingkup evaluasi detektor. |
| KT-07 | Judul pada sampul berbeda dari penamaan pada Subbab 4.1.1. Draf ini menggunakan judul sampul; keseragaman judul sumber perlu diperiksa. | Nicy. | Pemeriksaan dokumen kebutuhan/naskah. |
| KT-08 | Subbab 5.3 masih memuat instruksi editorial untuk mempertahankan paragraf lama. Penjelasan penyelesaian belum pasti dan pengaruh batas durasi perlu ditulis lengkap pada naskah. Istilah jumlah kendaraan frame dan kelompok awal pada Subbab 4.6 juga perlu diselaraskan dengan prosedur rinci 5.3. | Nicy bersama Putu, Rizky, dan Ikrom sesuai isi. | Sebelum prosedur pengamatan dan kalibrasi dibekukan. |

Keputusan aktual, dasar, tanggal, dan versi perubahannya dicatat setelah disepakati. Daftar ini tidak menetapkan varian model, angka ambang, atau hasil pengamatan yang belum diperoleh.

## 10. Verifikasi dan kelengkapan dokumen

### 10.1 Penelusuran kebutuhan ke pengujian

Bab 6 proposal, termasuk UJI-01–UJI-34 dan Tabel 6.3, menjadi dasar penyusunan matriks kebutuhan pada W01-T03. Matriks menghubungkan kode kebutuhan, sumber, PIC implementasi, cara verifikasi, kasus uji, kriteria hasil, serta status penetapan.

Kriteria pengujian pada SRS ini merupakan sasaran yang akan dibuktikan. Bukti pelaksanaan berupa frame/hitungan manual, catatan waktu, hasil evaluasi, log MQTT, status/data tersimpan, foto, dan rekaman perangkat dikumpulkan sesuai pekerjaan pengujian terkait.

### 10.2 Checklist pemeriksaan W01-T01

- [ ] Judul, lingkup, dan sumber kebutuhan diperiksa oleh Nicy.
- [ ] KF-01–KF-11, KNF-01–KNF-12, dan KJ-01–KJ-10 lengkap serta sesuai proposal sempro.
- [ ] Perangkat, software, server, antarmuka, data, jadwal, dan maintenance telah tercakup.
- [ ] YOLO ditulis sebagai keluarga model; varian yang belum dipilih tercatat statusnya.
- [ ] Kalibrasi kategori/durasi, batas kategori, target evaluasi, serta pemisahan data konsisten dengan bagian operasional proposal.
- [ ] Keputusan terbuka dan perbedaan rumusan sumber memiliki PIC serta waktu tindak lanjut.
- [ ] Hasil pemeriksaan, temuan, dan tindak lanjut dicatat pada `KELOMPOK-10/evidence/S01/README.md`, bagian Minggu 1.

### 10.3 Lokasi hasil dan pelaporan

| Path lengkap | Kegunaan |
|---|---|
| `KELOMPOK-10/docs/perencanaan/srs.md` | Hasil W01-T01 berupa draf spesifikasi kebutuhan ini. |
| `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md` | Dokumen pendamping yang disusun pada W01-T02. |
| `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md` | Dokumen pendamping penelusuran/verifikasi pada W01-T03. |
| `KELOMPOK-10/evidence/S01/README.md` | Ringkasan hasil minggu 1, pemeriksaan, kendala/tindak lanjut, serta commit pelaporan. |
| `KELOMPOK-10/evidence/S01/log-aktivitas.md` | Aktivitas aktual pelaksana sesuai tanggal dan ID tugas. |

Pesan commit pekerjaan untuk dokumen ini:

```text
S01-W01: susun SRS sistem
```

URL commit aktual dicatat setelah perubahan di-push. Pencatatan pada README dan penutupan tugas mengikuti hasil pemeriksaan yang benar-benar dilakukan.
