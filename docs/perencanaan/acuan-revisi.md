# Acuan revisi proposal dan pelaksanaan

| Keterangan | Nilai |
|---|---|
| Versi dan tanggal | 1.0 / 25 November 2026 |
| Proposal yang diperiksa | FINAL INI A(2).docx |
| SHA-256 berkas proposal | 5b8306b6f8a05c18b547316dc017b716ad4a72870cae9c1b3bf08c0ae72aab2b |
| Basis repositori | a6a8b504d1bad1282e23751621bf2c28c34e8c18 |
| Acuan utama | Subbab 4.6, 5.2.1–5.2.3, 5.3, Tabel 5.4–5.6, dan UJI-32 |

Proposal disimpan terpisah dari kode. Hash mengidentifikasi berkas yang diperiksa, bukan berkas Word yang kemudian disunting di komputer lain. Versi metode yang digunakan paket ini adalah revisi 25 November 2026. Jika naskah sumber disimpan ulang, catat nama/versi/hash baru beserta perubahan substansinya.

## Frame dan kelompok pada dataset rekaman

1. Pilih frame kepadatan sekitar lima detik sebelum hijau aktual pendekat yang diamati. Catat offset frame, awal hijau, selang aktual, dan dasar waktu yang sama. Batas selang yang diterima ditetapkan sebelum pengamatan terkait.
2. Hitung manual mobil, sepeda motor, bus, dan truk yang titik tengah sisi bawah bounding box-nya berada di dalam atau pada batas ROI. Kendaraan berhenti maupun bergerak bernilai satu.
3. Tetapkan kelompok awal dari kendaraan acuan manual pada frame yang sama. Tandai identitas/anggota dan lajur. Pada frame valid dengan anotasi sah, initial_queue_count = manual_total. Hitungan AI dievaluasi terhadap acuan ini dan dapat berbeda.
4. Pertahankan keanggotaan. Kendaraan yang masuk setelah waktu snapshot tidak ditambahkan, termasuk yang datang sebelum hijau mulai.
5. Mulai pengukuran layanan saat hijau aktual menyala. Ikuti anggota yang sama sampai anggota terakhir melewati garis henti. Penelusuran dapat dilanjutkan lintas hijau selama identitas masih dapat dipastikan; hanya interval hijau dijumlahkan.
6. Kelompok kosong pada frame sah mempunyai waktu layanan nol. Identitas hilang, rekaman putus, atau penyelesaian nonhijau tidak diisi sebagai waktu selesai hijau. Catat status dan informasi parsial. Sampel layanan berkategori sah dengan penyelesaian belum pasti tetap masuk penyebut cakupan dan bukan keberhasilan terverifikasi.

Nama kolom CSV initial_queue_count dipertahankan untuk kompatibilitas dan menyatakan jumlah anggota kelompok snapshot. Data yang dibuat memakai definisi antrean saat awal hijau perlu diberi versi dan ditinjau atau dianotasi ulang sebelum digabungkan. Dua template CSV pada repositori masih berisi header tanpa data aktual.

## Snapshot ketika prototipe beroperasi

Pembaca ketiga CCTV terus memperbarui buffer. ESP32 mengirim pemicu fase berikutnya saat hijau aktif tersisa satu detik. Ketika backend menangani pemicu unik yang sah, ambil satu salinan tetap frame utuh terbaru dari kamera tujuan beserta konfigurasi dan metadata. Validasi masukan sebelum YOLO. Catat frame_id, frame_received_ts, frame_selected_ts, dan frame_source_ts bila tersedia. Hasil antarframe tidak dijumlahkan; pemicu duplikat memakai hasil penanganan yang sama.

Terbaru berarti frame terakhir yang berhasil didekode dalam buffer pada waktu pemilihan. Waktu penerimaan server tidak membuktikan umur gambar sejak perekaman; dasar umur dan ambangnya ditetapkan per sumber. Tiga CCTV berasal dari lokasi berbeda dan tidak dikendalikan LED prototipe. Snapshot operasional tidak otomatis berada lima detik sebelum hijau aktual pada CCTV.

## Timing dan keputusan pengendalian

| Waktu nominal sejak pemicu | Kejadian |
|---|---|
| 0 detik | Hijau aktif tersisa satu detik; pemicu meminta fase berikutnya |
| 1 detik | Hijau aktif selesai dan kuning mulai |
| Paling lama 3 detik | Target plan valid sudah diterima ESP32 |
| Sekitar 4 detik | Lock sebelum merah bersama; tanpa kandidat valid gunakan statis lokal sah |
| Sekitar 5 detik | Merah bersama satu detik selesai; hijau fase berikutnya dimulai |

Rencana valid yang tiba setelah tiga detik tetapi sebelum lock dapat dipakai dengan pelanggaran target respons dicatat. Rencana baru setelah lock ditolak. Hijau aktif tidak dipotong oleh plan baru. Angka nominal dan target masih memerlukan pengukuran pada perangkat.

Kepadatan k = 1000 N / (L_m m). K-means satu dimensi dilakukan offline per kamera pada data manual. Ambang K1/K2 dan durasi dibekukan sebelum evaluasi terpisah. Durasi usulan menggunakan Persamaan (4.5), lalu dibatasi melalui (4.6). Contoh parameter bukan hasil kalibrasi.

## Pemetaan pin proposal

| Fase | Merah | Kuning | Hijau |
|---|---:|---:|---:|
| A | 25 | 26 | 27 |
| B | 14 | 18 | 19 |
| C | 23 | 32 | 33 |

OLED SDA21, SCL22, suplai 3,3 V dan GND bersama. Gunakan satu resistor 330 ohm untuk setiap LED sesuai rancangan. Pemetaan yang sama ada pada configs/pins.example.json, perakitan.md, dan skema-rangkaian.svg. Kecocokan papan serta rangkaian aktual diperiksa sebelum digunakan.

## Batas kesiapan

Paket ini menyelaraskan berkas repositori. Bukti S02 menunjukkan laporan layanan lokal dan pemuatan kandidat YOLO pada CPU; inventaris fisik, firmware, reader CCTV, parameter hasil kalibrasi, dan integrasi penuh masih mengikuti pelaksanaan sprint. Pemeriksaan berkas tidak menjadi bukti alat telah berfungsi.

KT-06 tetap mencatat perbedaan rumusan pembanding non-YOLO antarbagian proposal; paket tidak menambahkan pekerjaan eksperimen baru. KT-07 mencatat keseragaman judul naskah. Penomoran metrik Subbab 6.4 perlu penyuntingan sumber. Hal-hal itu dicatat untuk review tim sebelum evaluasi/dokumen akhir, tanpa mengganti hasil yang belum diperoleh dengan angka contoh.
