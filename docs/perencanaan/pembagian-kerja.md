# Pembagian Pekerjaan Tim

| Keterangan | Isi |
|---|---|
| Proyek | Estimasi Kepadatan Kendaraan dari CCTV untuk Pengendalian Lampu Lalu Lintas Adaptif pada Prototipe IoT |
| Tim | KELOMPOK-10 |
| Penyusun | Nicy Putra Pratama |
| Kode pekerjaan | S01-W01 / W01-T02 |
| Versi / tanggal | 0.1 / 29 Oktober 2026 |
| Status | Draf untuk pemeriksaan |
| Lokasi | `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md` |

## 1. Tujuan dan acuan

Dokumen ini membagi pelaksanaan pengembangan 16 minggu ke setiap anggota, dengan hasil, lokasi pengumpulan, dan ketergantungan yang jelas. Acuan kebutuhan adalah proposal sempro `FINAL INI A(1).docx`, yang telah dituangkan pada `KELOMPOK-10/docs/perencanaan/srs.md`. Rincian tugas, ID, jadwal, dan path mengikuti Kanban Sprint 01–08 versi 29 Oktober 2026. Dokumen ini merupakan rencana penugasan; status selesai dan hasil aktual dicatat pada bukti pelaksanaan.

Model ditulis **YOLO**. Varian, bobot, dan konfigurasi dipilih saat implementasi. Ruang lingkup pembanding detektor yang masih berbeda antarbagian proposal perlu diselaraskan Nicy sebelum menjadi pekerjaan uji wajib. Parameter yang menunggu kalibrasi tidak diperlakukan sebagai nilai final.

## 2. Peran anggota

| Nama | Peran | Tanggung jawab |
|---|---|---|
| Nicy Putra Pratama | Project Lead dan System Analyst | Kebutuhan, pembagian tugas, penyelarasan rancangan, koordinasi, pemeriksaan, dan serah terima. |
| Rizky Bintang Fadillah | AI dan Computer Vision Engineer | CCTV, ROI, YOLO, hitungan kendaraan, kepadatan, dan evaluasi AI. |
| Putu Radit Ardika | Backend dan Integration Engineer | Kategori/durasi, backend, MQTT, lingkungan server, dan integrasi. |
| Ramdhani / Dhani | Embedded dan IoT Engineer | Rangkaian, firmware ESP32, timer/urutan lampu, OLED, dan statis cadangan lokal. |
| Ikrom Safei | Data dan Testing Engineer | Acuan manual, metadata/sampel, Node-RED/InfluxDB, skenario/bukti uji, dan laporan. |

Putu/Radit dan Rizky/Bintang masing-masing menunjuk orang yang sama. Pada tabel tugas digunakan nama pendek. Seluruh penyusunan dokumen minggu 1 menjadi pekerjaan Nicy; PIC teknis melaksanakan penugasannya sesuai minggu yang tercantum.

## 3. Pembagian pekerjaan per minggu

### S01 — Minggu 1: Menyusun kebutuhan sistem, ruang lingkup, dan pembagian pekerjaan

**Ketergantungan dan urutan kerja:** Proposal sempro dan SRS; bagian yang belum ditetapkan dicatat sebagai keputusan terbuka.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W01-T01 | Nicy | Menyusun kebutuhan fungsi dan batasan dari proposal sempro FINAL INI A(1).docx: CCTV, YOLO tanpa menetapkan varian terlebih dahulu, hitungan, kepadatan, kategori/durasi, pengendalian, pencatatan, dan OLED. Melengkapi hardware, software, waktu, jasa, server, serta maintenance. | SRS yang dapat ditelusuri ke kebutuhan KF, KNF, dan KJ proposal sempro; pilihan implementasi yang belum ditetapkan diberi statusnya. | `KELOMPOK-10/docs/perencanaan/srs.md` |
| W01-T02 | Nicy | Membagi pekerjaan setiap anggota, hasil yang harus dikumpulkan, minggu pelaksanaan, dan ketergantungan antarpekerjaan. | Tabel nama anggota, tugas, hasil, minggu, dan ketergantungan. | `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md` |
| W01-T03 | Nicy | Memetakan KF, KNF, dan KJ ke cara verifikasi serta UJI terkait pada Bab 6. Mencatat parameter yang belum ditentukan dan ketidakkonsistenan ruang lingkup pembanding detektor untuk diselaraskan. | Matriks ID kebutuhan, sumber, cara verifikasi, kriteria, dan status penetapan; daftar keputusan/perbaikan naskah yang masih diperlukan. | `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S01/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S01/README.md`, bagian **Minggu 1**.

### S01 — Minggu 2: Menyusun rancangan tingkat tinggi atau HLD

**Ketergantungan dan urutan kerja:** SRS dan pembagian pekerjaan minggu 1; Nicy menyatukan bagian HLD anggota.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W02-T01 | Nicy | Menyusun diagram keseluruhan tiga sumber CCTV, satu server, ESP32, lampu, dan OLED. Menyatukan kontribusi HLD anggota menjadi satu rancangan. | Diagram arsitektur dan pembagian fungsi server/perangkat; HLD gabungan. | `KELOMPOK-10/docs/perencanaan/hld.md` |
| W02-T02 | Rizky | Menjelaskan alur CCTV, pengambilan gambar, YOLO, penghitungan kendaraan, dan kepadatan beserta masukan/keluaran modul AI. | Diagram alur AI dan uraian fungsi setiap tahap. | `KELOMPOK-10/docs/perencanaan/hld.md` |
| W02-T03 | Putu | Menjelaskan penerimaan pengukuran, penentuan kategori/durasi, pengiriman rencana melalui MQTT, dan hubungan backend dengan ESP32. | Diagram alur pengendalian serta masukan/keluaran backend dan MQTT. | `KELOMPOK-10/docs/perencanaan/hld.md` |
| W02-T04 | Ramdhani | Menjelaskan fungsi ESP32 dalam penerimaan rencana, urutan lampu, penghitung waktu, OLED, dan statis cadangan lokal. | Diagram blok perangkat dan penjelasan tanggung jawab ESP32. | `KELOMPOK-10/docs/perencanaan/hld.md` |
| W02-T05 | Ikrom | Menjelaskan pencatatan pengukuran, rencana, ACK, status pelaksanaan, dan kegagalan melalui Node-RED ke InfluxDB. Memisahkan alur pencatatan dari kelangsungan pengendalian. | Diagram alur pencatatan dan daftar kelompok data yang disimpan. | `KELOMPOK-10/docs/perencanaan/hld.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S01/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S01/README.md`, bagian **Minggu 2**.

### S01 — Minggu 3: Menyusun rancangan terperinci atau LLD dan prosedur pengamatan

**Ketergantungan dan urutan kerja:** SRS dan HLD; kontrak Putu menjadi acuan antarmuka AI, ESP32, dan pencatatan.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W03-T01 | Ramdhani | Merancang sambungan ESP32, sembilan LED, resistor, OLED, dan catu daya. Menentukan pin, urutan A–B–C–A, serta perilaku statis cadangan lokal. | Skema rangkaian, tabel pin, dan tabel urutan lampu; rancangan awal sebelum perakitan. | `KELOMPOK-10/docs/perangkat/perakitan.md` |
| W03-T02 | Putu | Merinci pemicu, pengukuran, rencana, ACK, dan status: topik MQTT, arah, field, satuan, identitas, versi, validitas, duplikasi, dan pesan terlambat. Menetapkan autentikasi/TLS, plan dan ACK QoS 1, serta plan retain false. | Kontrak komunikasi dan contoh JSON untuk lima jenis pesan. | `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md`; `KELOMPOK-10/configs/mqtt/trigger.example.json`; `KELOMPOK-10/configs/mqtt/measurement.example.json`; `KELOMPOK-10/configs/mqtt/plan.example.json`; `KELOMPOK-10/configs/mqtt/ack.example.json`; `KELOMPOK-10/configs/mqtt/status.example.json` |
| W03-T03 | Putu | Menyusun struktur parameter fase, kategori, durasi, dan statis cadangan. Merinci pemicu sisa hijau satu detik, target respons tiga detik, kuning tiga detik, merah bersama satu detik, dan penguncian sebelum merah bersama. | Contoh konfigurasi dan penjelasan parameter; nilai yang menunggu pengamatan ditandai sementara. | `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md`; `KELOMPOK-10/configs/control.example.json` |
| W03-T04 | Rizky | Merinci YOLO dengan varian yang dipilih saat implementasi, empat kelas, ROI, hitungan, dan kepadatan. Menyusun pengamatan pagi/siang/sore, snapshot sebelum hijau aktual, penandaan kelompok awal, akumulasi layanan hijau, serta data kalibrasi/uji pada hari berbeda. | Rancangan AI dan prosedur pengamatan/pengambilan sampel. | `KELOMPOK-10/docs/perencanaan/prosedur-ai-dan-pengamatan.md` |
| W03-T05 | Ikrom | Membuat kolom identitas CCTV/sampel, waktu frame/awal hijau, periode/hari, hitungan frame manual/AI, jumlah kelompok awal terpisah, panjang/lajur, kepadatan, akumulasi waktu hijau, status penyelesaian, serta batas informasi pengamatan. | Template CSV kalibrasi dan pengujian beserta panduan pengisian. | `KELOMPOK-10/data/templates/kalibrasi.csv`; `KELOMPOK-10/data/templates/pengujian.csv`; `KELOMPOK-10/data/templates/README.md` |
| W03-T06 | Ikrom | Menyusun skenario fungsi, komunikasi, respons, dan kegagalan menurut UJI-01–UJI-34. Memasukkan MAE, E_N <=10% per kamera, kategori/matriks kebingungan, cakupan layanan >=90%, serta parameter/toleransi yang masih perlu ditetapkan sebelum pengujian. | Rencana uji yang dapat dijalankan dan dilengkapi berdasarkan data/parameter berikutnya. | `KELOMPOK-10/docs/pengujian/rencana-uji.md` |
| W03-T07 | Nicy | Memeriksa konsistensi SRS, HLD, rangkaian, komunikasi, AI, dan rencana uji. Menentukan PIC untuk perbedaan atau kekurangan yang ditemukan. | Indeks SRS/HLD/LLD dan sumber dokumen; catatan review, temuan, PIC, dan tindak lanjut. | `KELOMPOK-10/docs/perencanaan/indeks-perencanaan.md`; `KELOMPOK-10/evidence/S01/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S01/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S01/README.md`, bagian **Minggu 3**.

### S02 — Minggu 4: Menyiapkan komponen dan lingkungan pengembangan server

**Ketergantungan dan urutan kerja:** Kebutuhan sumber daya dan rancangan minggu 1–3; inventaris Ramdhani serta kesiapan lingkungan Putu/Rizky.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W04-T01 | Putu | Menyiapkan Ubuntu/lingkungan backend dan Docker untuk Mosquitto, Node-RED, serta InfluxDB. Mengatur jaringan, autentikasi/TLS, volume persisten, dan variabel konfigurasi. | Konfigurasi layanan, contoh variabel lingkungan tanpa rahasia, dan panduan menjalankan server. | `KELOMPOK-10/infra/compose.yaml`; `KELOMPOK-10/.env.example`; `KELOMPOK-10/infra/lingkungan-server.md` |
| W04-T02 | Rizky | Menyiapkan Python, pustaka CCTV/AI, dan bobot kandidat YOLO untuk pengujian implementasi. Memeriksa pemuatan model dan kondisi GPU NVIDIA/CUDA atau CPU aktual; varian belum dianggap final sebelum dinilai terhadap kebutuhan. | Daftar dependensi, manifest model, catatan versi lingkungan, dan keluaran pemeriksaan aktual. | `KELOMPOK-10/ai/requirements.txt`; `KELOMPOK-10/models/manifest.csv`; `KELOMPOK-10/infra/lingkungan-ai.md`; `KELOMPOK-10/evidence/S02/lingkungan-ai.txt` |
| W04-T03 | Ramdhani | Memeriksa jumlah, jenis, dan kondisi ESP32, sembilan LED, resistor, OLED, kabel, breadboard, serta catu daya. Mencatat komponen yang belum tersedia. | Inventaris kebutuhan/ketersediaan komponen beserta kekurangan dan tindak lanjut. | `KELOMPOK-10/docs/perangkat/inventaris.md` |
| W04-T04 | Putu | Menjalankan layanan dan memeriksa koneksi MQTT serta akses Node-RED/InfluxDB. Mencatat hasil berhasil/gagal dan kendalanya. | Keluaran pemeriksaan layanan dan langkah perbaikan lingkungan bila diperlukan. | `KELOMPOK-10/infra/lingkungan-server.md`; `KELOMPOK-10/evidence/S02/status-layanan.txt` |
| W04-T05 | Ikrom | Merekap bukti lingkungan server, AI, dan inventaris dari pelaksana. Mencatat perbedaan lingkungan sementara dengan target implementasi. | Rekap kesiapan komponen/lingkungan, versi, kendala, PIC, dan status tindak lanjut. | `KELOMPOK-10/evidence/S02/README.md` |
| W04-T06 | Nicy | Memeriksa kesiapan terhadap kebutuhan S01 dan menentukan penyelesaian kekurangan yang menghambat perakitan/pengembangan. | Catatan review kesiapan serta tindak lanjut sebelum S03. | `KELOMPOK-10/evidence/S02/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S02/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S02/README.md`, bagian **Minggu 4**.

### S03 — Minggu 5: Merakit ESP32, LED, resistor, OLED, dan catu daya

**Ketergantungan dan urutan kerja:** Skema/pin minggu 3 dan komponen minggu 4; Ikrom memerlukan rangkaian/firmware aktual untuk merekam bukti.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W05-T01 | Ramdhani | Merakit ESP32, sembilan LED/resistor, OLED, dan catu daya. Memeriksa sambungan, pemetaan pin, dan kestabilan catu daya sesuai rancangan. | Rangkaian aktual dan dokumentasi sambungan/pin yang diperbarui. | `KELOMPOK-10/docs/perangkat/perakitan.md`; `KELOMPOK-10/evidence/S03/rangkaian.jpg` |
| W05-T02 | Ramdhani | Membuat program dasar fase A–B–C–A, maksimal satu hijau, kuning tiga detik, dan merah bersama satu detik. Mencatat durasi hijau sementara untuk uji dasar. | Firmware dasar dan tabel durasi uji yang digunakan. | `KELOMPOK-10/docs/perangkat/perakitan.md`; `KELOMPOK-10/firmware/esp32/` |
| W05-T03 | Ramdhani | Menambahkan tampilan dasar fase, keadaan lampu, dan sisa waktu pada OLED. Memeriksa kecocokan tampilan dengan keluaran lampu. | Program tampilan OLED dan foto kondisi yang benar-benar ditampilkan. | `KELOMPOK-10/firmware/esp32/`; `KELOMPOK-10/evidence/S03/oled.jpg` |
| W05-T04 | Ikrom | Mendokumentasikan pemeriksaan urutan fase, interval transisi, OLED, dan catu daya bersama pelaksana perangkat. | Rekaman pengujian dasar dan tabel hasil aktual/temuan. | `KELOMPOK-10/evidence/S03/urutan-lampu.mp4`; `KELOMPOK-10/evidence/S03/pemeriksaan-dasar.csv` |
| W05-T05 | Nicy | Memeriksa kesesuaian rangkaian/firmware dengan LLD dan menindaklanjuti temuan yang menghambat integrasi. | Catatan penerimaan hasil perakitan dan daftar perbaikan. | `KELOMPOK-10/evidence/S03/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S03/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S03/README.md`, bagian **Minggu 5**.

### S04 — Minggu 6: Memeriksa sumber CCTV dan menetapkan area pengamatan

**Ketergantungan dan urutan kerja:** Prosedur pengamatan dan template minggu 3 serta akses sumber CCTV; Rizky menetapkan ROI, Ikrom mencatat metadata.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W06-T01 | Rizky | Membuat pembaca tiga sumber CCTV dari lokasi berbeda dan memetakannya ke fase virtual A, B, dan C. Menangani kegagalan baca/decoding, umur frame, dan waktu frame. | Modul pembaca CCTV dan hasil pemeriksaan keterbacaan setiap sumber. | `KELOMPOK-10/ai/cctv_reader.py`; `KELOMPOK-10/evidence/S04/pemeriksaan-sumber.csv` |
| W06-T02 | Rizky | Menentukan pendekat lurus searah menuju garis henti, ROI pada frame asli, panjang pengamatan meter, dan jumlah lajur searah tiap sumber. Mencocokkan patokan gambar dengan pengukuran Google Maps serta mencatat sumbernya; panjang/lajur harus positif. | Konfigurasi kamera dan uraian dasar penetapan ROI, panjang, serta lajur. | `KELOMPOK-10/configs/cameras.example.json`; `KELOMPOK-10/docs/operasional/konfigurasi-kamera.md` |
| W06-T03 | Ikrom | Mencatat identitas sumber/rekaman, dimensi frame, lokasi, waktu, dan pemetaan fase. Mengarsipkan gambar ROI yang disiapkan Rizky. | Metadata sumber dan tiga gambar ROI yang dapat ditelusuri. | `KELOMPOK-10/data/metadata/sumber-rekaman.csv`; `KELOMPOK-10/evidence/S04/roi-A.jpg`; `KELOMPOK-10/evidence/S04/roi-B.jpg`; `KELOMPOK-10/evidence/S04/roi-C.jpg` |
| W06-T04 | Nicy | Memeriksa kelengkapan ketiga sumber, dasar ukuran area/lajur, dan konsistensi pemetaan kamera dengan fase virtual. | Catatan review sumber/area dan tindak lanjut jika sumber atau ukuran belum layak. | `KELOMPOK-10/evidence/S04/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S04/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S04/README.md`, bagian **Minggu 6**.

### S04 — Minggu 7: Mengembangkan deteksi dan penghitungan kendaraan menggunakan YOLO

**Ketergantungan dan urutan kerja:** Sumber/ROI minggu 6, lingkungan AI minggu 4, dan kontrak pesan minggu 3; Ikrom menyediakan pembanding manual.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W07-T01 | Rizky | Mengimplementasikan YOLO untuk mobil, sepeda motor, bus, dan truk; memilih serta mencatat varian/bobot/konfigurasi berdasarkan ketepatan hitungan, waktu, dan sumber daya pada lingkungan implementasi. Model dimuat sekali saat inisialisasi. | Modul deteksi, manifest varian/bobot/konfigurasi aktual, serta alasan pemilihan yang didukung hasil pemeriksaan. | `KELOMPOK-10/ai/deteksi_kendaraan.py`; `KELOMPOK-10/models/manifest.csv` |
| W07-T02 | Rizky | Menghitung objek bila titik tengah sisi bawah bounding box berada di dalam/pada batas ROI. Menggunakan satu snapshot per pemicu; setiap kendaraan satu unit tanpa akumulasi antarframe. | Modul penghitungan ROI dan gambar hasil deteksi untuk tiga sumber. | `KELOMPOK-10/ai/penghitungan_roi.py`; `KELOMPOK-10/evidence/S04/deteksi-A.jpg`; `KELOMPOK-10/evidence/S04/deteksi-B.jpg`; `KELOMPOK-10/evidence/S04/deteksi-C.jpg` |
| W07-T03 | Ikrom | Menghitung kendaraan manual pada frame dan ROI yang sama dengan AI. Mencatat identitas gambar, hasil per kelas/total, dan kasus yang sulit diamati. | Tabel pembanding manual dengan rujukan frame yang jelas. | `KELOMPOK-10/evidence/S04/perbandingan-manual.csv` |
| W07-T04 | Rizky | Mengisi hasil AI pada tabel pembanding dan menjelaskan perbedaan hitungan, termasuk objek di batas ROI dan hasil nol kendaraan yang valid. | Perbandingan AI/manual dan catatan keterbatasan deteksi. | `KELOMPOK-10/evidence/S04/perbandingan-manual.csv`; `KELOMPOK-10/docs/pengujian/pemeriksaan-awal-ai.md` |
| W07-T05 | Nicy | Memeriksa kecocokan model, kelas, aturan ROI, dan frame pembanding terhadap rancangan. | Catatan review modul deteksi/penghitungan dan tugas perbaikannya. | `KELOMPOK-10/evidence/S04/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S04/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S04/README.md`, bagian **Minggu 7**.

### S04 — Minggu 8: Melengkapi data kalibrasi

**Ketergantungan dan urutan kerja:** ROI, prosedur, template, dan modul hitungan; Rizky/Putu memerlukan data manual serta pengamatan layanan yang dicatat Ikrom.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W08-T01 | Rizky | Memilih rencana 15 siklus kalibrasi per kamera: lima pagi, lima siang, lima sore. Menentukan frame sekitar lima detik sebelum hijau aktual dan mencatat selang aktual; menghitung kendaraan pada frame, ROI, panjang, serta lajur. Hari kalibrasi dibedakan dari data uji. | Data frame, jumlah kendaraan, dan identitas siklus untuk 15 siklus per CCTV. | `KELOMPOK-10/data/kalibrasi/observasi.csv`; `KELOMPOK-10/data/metadata/sumber-rekaman.csv` |
| W08-T02 | Putu | Menandai kelompok yang sudah mengantre di ROI saat hijau aktual dimulai dan mencatat jumlahnya terpisah dari hitungan frame. Menelusuri sampai anggota terakhir melewati garis henti, termasuk hijau berikutnya bila masih dikenali; menjumlahkan waktu hijau saja dan mencatat penyelesaian belum pasti. | Jumlah kelompok awal, penelusuran layanan lintas hijau bila diperlukan, akumulasi waktu layanan, dan status kepastian pengamatan. | `KELOMPOK-10/data/kalibrasi/observasi.csv` |
| W08-T03 | Ikrom | Menggabungkan hasil Rizky/Putu; memeriksa identitas, kolom, sumber, serta rencana 15 siklus per kamera/45 total. Memeriksa lima pagi, lima siang, lima sore, pemisahan hari uji, dan kecukupan variasi untuk tiga kategori. | Dataset kalibrasi gabungan, panduan kolom, dan rekap kekurangan data. | `KELOMPOK-10/data/kalibrasi/observasi.csv`; `KELOMPOK-10/data/kalibrasi/README.md`; `KELOMPOK-10/evidence/S04/rekap-kalibrasi.csv` |
| W08-T04 | Ikrom | Mencatat daftar sampel kalibrasi dan pembagian data agar siklus uji berikutnya terpisah. Menjelaskan variasi kondisi dan keterbatasan cakupan sampel. | Daftar pembagian sampel dan keterlacakan data kalibrasi/uji. | `KELOMPOK-10/data/metadata/pembagian-sampel.csv` |
| W08-T05 | Nicy | Memeriksa jumlah, keterlacakan, prosedur waktu layanan, dan pemisahan sampel sebelum data dipakai menentukan parameter. | Catatan review kelengkapan 45 siklus kalibrasi serta tindak lanjut. | `KELOMPOK-10/evidence/S04/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S04/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S04/README.md`, bagian **Minggu 8**.

### S04 — Minggu 9: Mengembangkan perhitungan kepadatan, kategori, dan durasi lampu

**Ketergantungan dan urutan kerja:** Data kalibrasi minggu 8, hitungan/kepadatan Rizky, dan acuan manual; Putu menetapkan parameter, Ramdhani memakai statis lokal yang disepakati.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W09-T01 | Rizky | Mengimplementasikan k = 1000 × jumlah kendaraan / (panjang meter × jumlah lajur), satuan kendaraan/km/lajur. Menolak input tidak sah; membedakan nol valid dari data tidak tersedia. | Modul kepadatan dan contoh hasil benar/nol/tidak valid. | `KELOMPOK-10/ai/estimasi_kepadatan.py`; `KELOMPOK-10/evidence/S04/pemeriksaan-kepadatan.csv` |
| W09-T02 | Putu | Mengkalibrasi tiga kelompok kepadatan manual per kamera dengan K-means satu dimensi, mencatat pengaturan/anggota/pusat, dan menghitung K1/K2 dari titik tengah pusat terurut. Menetapkan durasi dari P90 nearest-rank bila waktu lengkap atau penilaian cakupan bila belum pasti; memeriksa sasaran >=90% pada durasi akhir setelah batas. Membekukan parameter yang sudah didukung data. | Kode K-means/penetapan durasi, pusat/anggota/ambang, status cakupan per kategori, konfigurasi berversi, dan dasar parameter statis cadangan. | `KELOMPOK-10/backend/kalibrasi/`; `KELOMPOK-10/docs/kalibrasi/hasil-kalibrasi.md`; `KELOMPOK-10/configs/control.json` |
| W09-T03 | Putu | Mengimplementasikan kategori rendah 0 <= k < K1, sedang K1 <= k < K2, tinggi k >= K2. Memakai ambang/durasi yang dibekukan, mengurutkan durasi kategori agar tidak menurun, menerapkan waktu dasar/tambahan serta batas minimum–maksimum, dan memeriksa ulang cakupan pada durasi akhir. | Modul kategori/durasi, contoh keluaran, dan pemeriksaan batas K1/K2/minimum/maksimum. | `KELOMPOK-10/backend/aturan_durasi.py`; `KELOMPOK-10/evidence/S04/pemeriksaan-aturan.csv` |
| W09-T04 | Ramdhani | Menyiapkan konfigurasi statis lokal ESP32 dari parameter yang disepakati dan memeriksa pelaksanaannya pada perangkat. | Konfigurasi statis lokal dan bukti pemeriksaan durasi cadangan. | `KELOMPOK-10/firmware/esp32/`; `KELOMPOK-10/evidence/S04/pemeriksaan-statis-lokal.csv` |
| W09-T05 | Ikrom | Memeriksa versi/dataset, tiga kelompok tidak kosong dan pusat terurut, titik tengah K1/K2, P90 untuk waktu lengkap, serta perhitungan cakupan dengan penyelesaian belum pasti tetap pada penyebut. Menyamakan rencana uji dengan target Bab 6 dan mencatat parameter yang masih perlu ditetapkan. | Rekap pemeriksaan parameter dan rencana uji yang sudah memuat kriteria penilaian atau tindak lanjut penetapannya. | `KELOMPOK-10/evidence/S04/rekap-parameter.csv`; `KELOMPOK-10/docs/pengujian/rencana-uji.md` |
| W09-T06 | Nicy | Meninjau dasar parameter, konsistensi AI/backend/ESP32, dan kesiapan kriteria pengujian. Meminta penyelesaian nilai yang masih sementara sebelum digunakan sebagai konfigurasi final. | Catatan review hasil kalibrasi dan kesiapan integrasi. | `KELOMPOK-10/evidence/S04/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S04/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S04/README.md`, bagian **Minggu 9**.

### S05 — Minggu 10: Mengintegrasikan backend, MQTT, dan ESP32

**Ketergantungan dan urutan kerja:** Kontrak pesan, modul AI/backend, parameter, broker, dan firmware dasar; pengujian memerlukan ESP32 aktual untuk membuktikan penerimaan/pelaksanaan.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W10-T01 | Rizky | Menghubungkan permintaan kamera/fase dari backend dengan pemilihan frame dan satu pengukuran AI. Mengembalikan identitas, hitungan, kepadatan, serta alasan kegagalan bila ada. | Antarmuka pengukuran yang sesuai kontrak dan contoh keluaran aktual. | `KELOMPOK-10/ai/`; `KELOMPOK-10/evidence/S05/keluaran-ai.json` |
| W10-T02 | Putu | Menghubungkan pemicu, pengukuran, kategori/durasi, dan rencana melalui MQTT. Memvalidasi sesi, giliran, fase, versi, isi, serta masa penerimaan; menangani duplikat tanpa inferensi/keputusan berulang. | Backend/MQTT terintegrasi dengan validasi, identitas pesan, dan pengaturan autentikasi/TLS. | `KELOMPOK-10/backend/`; `KELOMPOK-10/configs/mqtt/`; `KELOMPOK-10/docs/pengujian/integrasi-mqtt.md` |
| W10-T03 | Ramdhani | Mengirim pemicu pada sisa hijau satu detik, menerima kandidat rencana, dan mengunci keputusan sebelum merah bersama. Menolak rencana baru setelah penguncian; menjaga hijau aktif dan timer saat duplikat datang. | Firmware penerimaan/penguncian rencana, urutan fase, dan penanganan duplikasi. | `KELOMPOK-10/firmware/esp32/` |
| W10-T04 | Ramdhani | Menggunakan statis lokal terverifikasi ketika kandidat sah tidak tersedia saat penguncian. Memulihkan adaptif pada giliran berikutnya yang memenuhi syarat; menerbitkan ACK penerimaan dan status pelaksanaan. | Firmware cadangan/pemulihan dan status yang membedakan kandidat diterima dari rencana dijalankan. | `KELOMPOK-10/docs/pengujian/integrasi-mqtt.md`; `KELOMPOK-10/firmware/esp32/` |
| W10-T05 | Ikrom | Mencatat alur pemicu sampai pelaksanaan. Memeriksa identitas rencana/perangkat, penerimaan dan penguncian, serta perilaku ketika tidak ada kandidat sah. | Pesan MQTT aktual, rekaman durasi perangkat, dan rekap pemeriksaan integrasi. | `KELOMPOK-10/evidence/S05/mqtt-pemicu-rencana.txt`; `KELOMPOK-10/evidence/S05/integrasi-durasi.mp4`; `KELOMPOK-10/evidence/S05/rekap-integrasi.csv` |
| W10-T06 | Nicy | Memeriksa bahwa rencana benar-benar dijalankan pada fase/giliran yang tepat, termasuk cadangan dan pemulihan, lalu menentukan tindak lanjut integrasi. | Catatan review alur AI–backend–MQTT–ESP32. | `KELOMPOK-10/evidence/S05/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S05/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S05/README.md`, bagian **Minggu 10**.

### S05 — Minggu 11: Mengintegrasikan pencatatan data dan keluaran OLED

**Ketergantungan dan urutan kerja:** Jalur pengendalian minggu 10 dan format status; Ikrom memakai pesan aktual, Ramdhani memakai data/status yang sama untuk OLED.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W11-T01 | Ramdhani | Menghubungkan OLED dengan fase, keadaan lampu, sisa waktu, hitungan, kepadatan, kategori, dan mode aktual. Menampilkan penanda data gagal/tidak tersedia. | Firmware OLED sesuai keadaan perangkat dan foto tampilan aktual. | `KELOMPOK-10/firmware/esp32/`; `KELOMPOK-10/evidence/S05/oled-status.jpg` |
| W11-T02 | Putu | Menerbitkan peristiwa pengukuran, rencana, ACK, dan pelaksanaan dengan ID/waktu/versi yang konsisten, termasuk alasan penolakan atau cadangan. | Keluaran peristiwa backend yang dapat ditelusuri ke pengukuran dan pelaksanaan. | `KELOMPOK-10/backend/`; `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md` |
| W11-T03 | Ikrom | Menyusun alur Node-RED untuk memvalidasi dan menyimpan peristiwa ke InfluxDB. Memeriksa hubungan data pengukuran, rencana, ACK, dan status aktual. | Flow Node-RED, definisi data tersimpan, dan contoh hasil pencatatan. | `KELOMPOK-10/backend/node-red/flow.json`; `KELOMPOK-10/docs/pengujian/pencatatan-data.md`; `KELOMPOK-10/evidence/S05/pemeriksaan-pencatatan.csv` |
| W11-T04 | Putu | Memeriksa volume persisten InfluxDB dan pengaturan layanan agar dapat dijalankan ulang sesuai panduan. | Konfigurasi penyimpanan persisten dan langkah menjalankan ulang layanan. | `KELOMPOK-10/infra/compose.yaml`; `KELOMPOK-10/infra/lingkungan-server.md` |
| W11-T05 | Ikrom | Memeriksa data setelah layanan dijalankan ulang dan saat Node-RED/InfluxDB terganggu. Mencatat bukti bahwa pengendalian tetap berjalan ketika jalur kendalinya tersedia. | Hasil pemeriksaan persistensi, gangguan pencatatan, dan kelangsungan lampu. | `KELOMPOK-10/docs/pengujian/pencatatan-data.md`; `KELOMPOK-10/evidence/S05/pemeriksaan-pencatatan.csv` |
| W11-T06 | Nicy | Memeriksa konsistensi OLED, data tersimpan, identitas, dan keadaan aktual sebelum sistem masuk tahap pengujian gabungan. | Catatan review integrasi pencatatan/OLED dan tindak lanjut. | `KELOMPOK-10/evidence/S05/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S05/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S05/README.md`, bagian **Minggu 11**.

### S06 — Minggu 12: Menguji beban gabungan pada server

**Ketergantungan dan urutan kerja:** Integrasi minggu 10–11 dan seluruh layanan pada satu server; hasil menjadi dasar penilaian spesifikasi dan waktu respons.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W12-T01 | Rizky | Mengukur pengambilan frame, prapemrosesan, inferensi, serta penghitungan/kepadatan ketika tiga pembaca CCTV dan layanan lain berjalan bersama; inferensi tetap per pemicu. | Instrumen pengukuran dan data waktu tiap tahap AI pada beban gabungan. | `KELOMPOK-10/tests/performance/`; `KELOMPOK-10/evidence/S06/waktu-ai.csv` |
| W12-T02 | Putu | Menjalankan beban gabungan AI/backend/MQTT/Node-RED/InfluxDB dan mengukur waktu backend sampai pengiriman rencana. Mencatat versi, konfigurasi, kondisi jaringan, dan jumlah percobaan. | Skenario beban, data waktu backend, dan catatan kondisi pengujian. | `KELOMPOK-10/tests/performance/`; `KELOMPOK-10/evidence/S06/waktu-backend.csv`; `KELOMPOK-10/evidence/S06/kondisi-pengujian.md` |
| W12-T03 | Ramdhani | Mengukur respons pemicu sampai plan diterima menggunakan jam lokal ESP32. Mencatat target tiga detik, waktu penguncian, keterlambatan/tidak diterima, dan tindakan aktual perangkat. | Data respons total dan status adaptif/cadangan per percobaan. | `KELOMPOK-10/firmware/esp32/`; `KELOMPOK-10/evidence/S06/respons-esp32.csv` |
| W12-T04 | Ikrom | Merekam CPU, RAM, GPU, penyimpanan, kondisi jaringan, dan menggabungkan hasil waktu dari pelaksana. Menilai hasil terhadap kriteria yang sudah ditetapkan. | Data sumber daya dan laporan beban/respons beserta hasil gagal dan keterbatasan. | `KELOMPOK-10/evidence/S06/sumber-daya.csv`; `KELOMPOK-10/docs/pengujian/hasil-beban-respons.md` |
| W12-T05 | Nicy | Memeriksa kecukupan spesifikasi server berdasarkan hasil beban gabungan serta menentukan PIC untuk hambatan kinerja. | Catatan review kinerja dan daftar tindak lanjut. | `KELOMPOK-10/evidence/S06/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S06/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S06/README.md`, bagian **Minggu 12**.

### S06 — Minggu 13: Melaksanakan pengujian menggunakan sampel terpisah

**Ketergantungan dan urutan kerja:** Parameter/model/konfigurasi dibekukan dan sampel uji terpisah tersedia; Ikrom menjaga metadata dan rekap independensi sampel.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W13-T01 | Ikrom | Menyiapkan 15 siklus uji per CCTV/45 total: lima pagi, lima siang, lima sore pada hari berbeda dari kalibrasi. Mengisi acuan manual/frame, kelompok awal, waktu/status layanan, metadata, dan versi beku yang dinilai. | Dataset uji terpisah dan daftar pembagian sampel/versi yang dievaluasi. | `KELOMPOK-10/data/uji/observasi.csv`; `KELOMPOK-10/data/uji/README.md`; `KELOMPOK-10/data/metadata/pembagian-sampel.csv` |
| W13-T02 | Rizky | Menjalankan versi AI beku tanpa tuning pada sampel uji. Membandingkan hitungan pada frame/ROI yang sama, menghitung MAE dan E_N per kamera terhadap target <=10%, serta memeriksa kepadatan. Jika total manual nol, E_N tidak dihitung dan hasil nol diperiksa melalui MAE. | Kode evaluasi dan hasil hitungan/kepadatan, MAE, E_N atau alasan tidak dapat dihitung, serta jumlah frame valid per kamera. | `KELOMPOK-10/tests/evaluation/`; `KELOMPOK-10/evidence/S06/evaluasi-sampel.csv` |
| W13-T03 | Putu | Mengevaluasi kategori terhadap kepadatan manual menggunakan ambang beku yang sama; melaporkan akurasi, matriks kebingungan, serta jumlah sampel kategori per kamera. Menilai cakupan layanan durasi akhir terhadap sasaran >=90%; sampel belum pasti tetap pada penyebut dan kategori tanpa sampel dinyatakan belum dapat dinilai. | Evaluasi kategori dan cakupan layanan per kamera/kategori, terpisah dari hasil kalibrasi, beserta jumlah sampel dan status kepastian. | `KELOMPOK-10/tests/evaluation/`; `KELOMPOK-10/evidence/S06/evaluasi-sampel.csv` |
| W13-T04 | Ikrom | Menggabungkan hasil AI/backend, jumlah sampel, kriteria tercapai/tidak tercapai, variasi kondisi, dan keterbatasan pengamatan. | Laporan evaluasi 45 siklus uji dan rekap hasil terhadap kriteria. | `KELOMPOK-10/evidence/S06/evaluasi-sampel.csv`; `KELOMPOK-10/docs/pengujian/evaluasi-data-uji.md` |
| W13-T05 | Nicy | Memeriksa pemisahan sampel, konsistensi versi, dan kesesuaian kesimpulan terhadap data aktual. | Catatan review evaluasi dan temuan yang perlu diperbaiki. | `KELOMPOK-10/evidence/S06/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S06/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S06/README.md`, bagian **Minggu 13**.

### S06 — Minggu 14: Menguji fungsi, komunikasi, dan kondisi kegagalan

**Ketergantungan dan urutan kerja:** Integrasi lengkap, rencana uji, serta kriteria/toleransi yang ditetapkan sebelum uji; pemilik modul menyediakan keluaran aktual untuk rekap Ikrom.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W14-T01 | Rizky | Menguji nol kendaraan valid, sumber/decoding gagal, frame kedaluwarsa, ROI tidak sah, dan pengukuran tidak tersedia/tidak valid. | Kasus uji AI dan bukti nilai nol sah atau null beserta alasan kegagalan. | `KELOMPOK-10/tests/integration/`; `KELOMPOK-10/evidence/S06/kasus-ai.csv` |
| W14-T02 | Putu | Menguji identitas sesi/fase/giliran salah, isi pesan tidak sah, duplikasi, plan tidak diterima, dan gangguan jaringan/server. Memeriksa autentikasi/TLS serta penolakan kredensial tidak sah. | Kasus komunikasi/keamanan dan pesan aktual hasil pengujian. | `KELOMPOK-10/tests/integration/`; `KELOMPOK-10/evidence/S06/kasus-mqtt.csv` |
| W14-T03 | Ramdhani | Menguji A–B–C–A, maksimal satu hijau, kuning tiga detik, merah bersama satu detik, batas durasi, dan timer saat duplikat. Membedakan plan melewati tiga detik tetapi sebelum lock dari plan baru setelah lock; menguji cadangan/pemulihan. | Hasil timing, penguncian, duplikasi, cadangan, dan pemulihan pada perangkat aktual. | `KELOMPOK-10/tests/integration/`; `KELOMPOK-10/evidence/S06/kasus-esp32.csv`; `KELOMPOK-10/evidence/S06/fallback-pemulihan.mp4` |
| W14-T04 | Ikrom | Menguji kecocokan OLED, persistensi data setelah layanan penyimpanan dijalankan ulang, dan kelangsungan pengendalian ketika Node-RED/InfluxDB terganggu. | Hasil uji pencatatan/OLED dan bukti lampu tetap berjalan pada gangguan pencatatan. | `KELOMPOK-10/evidence/S06/kasus-pencatatan-oled.csv` |
| W14-T05 | Ikrom | Menyatukan hasil kasus AI, MQTT, perangkat, pencatatan, dan pemeriksaan kalibrasi/evaluasi UJI-01–UJI-34. Mengisi hasil harapan/aktual, bukti, status, dampak, dan PIC temuan. | Rekap kasus dan laporan fungsi, gangguan, serta keamanan komunikasi. | `KELOMPOK-10/evidence/S06/rekap-kasus-uji.csv`; `KELOMPOK-10/docs/pengujian/fungsi-gangguan-keamanan.md` |
| W14-T06 | Nicy | Menilai kelengkapan pengujian dan menetapkan prioritas/PIC temuan untuk minggu 15. Memisahkan target respons adaptif dari keberhasilan cadangan. | Catatan review pengujian dan daftar prioritas perbaikan. | `KELOMPOK-10/evidence/S06/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S06/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S06/README.md`, bagian **Minggu 14**.

### S07 — Minggu 15: Memperbaiki temuan pengujian dan melakukan pengujian ulang

**Ketergantungan dan urutan kerja:** Temuan dan prioritas minggu 12–14; pemilik modul memperbaiki temuan, Ikrom memverifikasi, Nicy meninjau penyelesaian.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W15-T01 | Nicy | Menentukan prioritas temuan, dampak, PIC, dan skenario verifikasi. Memeriksa kembali hasil perbaikan serta penyelesaian temuan penghambat serah terima. | Daftar tindak lanjut dan catatan review akhir perbaikan. | `KELOMPOK-10/evidence/S07/verifikasi-perbaikan.csv`; `KELOMPOK-10/evidence/S07/README.md` |
| W15-T02 | Rizky | Memperbaiki temuan pembacaan CCTV, deteksi, ROI, atau kepadatan yang menjadi tanggung jawab AI. Mencatat versi dan menguji ulang modul serta hubungan integrasinya. | Perubahan AI bila diperlukan, manifest terbaru bila berubah, dan hasil uji ulang. | `KELOMPOK-10/ai/`; `KELOMPOK-10/models/manifest.csv`; `KELOMPOK-10/evidence/S07/uji-ulang-ai.csv` |
| W15-T03 | Putu | Memperbaiki temuan kategori/durasi, MQTT, backend, layanan, atau konfigurasi. Menguji ulang perilaku yang berubah dan keterkaitannya dengan ESP32/AI. | Perubahan backend/konfigurasi/layanan bila diperlukan dan hasil uji ulang. | `KELOMPOK-10/backend/`; `KELOMPOK-10/configs/`; `KELOMPOK-10/infra/`; `KELOMPOK-10/evidence/S07/uji-ulang-backend.csv` |
| W15-T04 | Ramdhani | Memperbaiki temuan rangkaian, firmware, urutan, timer, penguncian, cadangan/pemulihan, atau OLED. Memperbarui dokumentasi perangkat jika sambungan berubah. | Perubahan perangkat/firmware bila diperlukan dan hasil uji ulang aktual. | `KELOMPOK-10/firmware/esp32/`; `KELOMPOK-10/docs/perangkat/perakitan.md`; `KELOMPOK-10/evidence/S07/uji-ulang-esp32.csv` |
| W15-T05 | Ikrom | Memperbaiki temuan flow pencatatan/format data yang menjadi tanggung jawabnya. Memverifikasi hasil perbaikan anggota dan menggabungkan bukti sebelum/sesudah serta status temuan. | Perubahan pencatatan bila diperlukan, rekap verifikasi, dan laporan uji ulang. | `KELOMPOK-10/evidence/S07/verifikasi-perbaikan.csv`; `KELOMPOK-10/backend/node-red/flow.json`; `KELOMPOK-10/docs/pengujian/perbaikan-dan-uji-ulang.md` |
| W15-T06 | Ikrom | Memperbarui laporan dan status pembagian data bila sampel uji dipakai untuk tuning. Menyiapkan data evaluasi terpisah untuk klaim independen versi hasil tuning. | Dokumentasi versi, independensi sampel, dan keterbatasan hasil evaluasi terakhir. | `KELOMPOK-10/docs/pengujian/perbaikan-dan-uji-ulang.md`; `KELOMPOK-10/data/metadata/pembagian-sampel.csv` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S07/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S07/README.md`, bagian **Minggu 15**.

### S08 — Minggu 16: Menyelesaikan laporan akhir, panduan penggunaan, dan serah terima

**Ketergantungan dan urutan kerja:** Versi akhir dan hasil uji ulang minggu 15; materi teknis anggota menjadi masukan laporan/panduan Ikrom dan pemeriksaan akhir Nicy.

| ID tugas | PIC | Pekerjaan | Hasil yang dikumpulkan | Lokasi berkas |
|---|---|---|---|---|
| W16-T01 | Rizky | Merapikan modul/dependensi AI, manifest YOLO, serta petunjuk sumber CCTV, ROI, dan inferensi sesuai versi terakhir yang diuji. | Kode/manifest AI final dan bagian instalasi, operasi, serta gangguan AI. | `KELOMPOK-10/ai/`; `KELOMPOK-10/models/manifest.csv`; `KELOMPOK-10/docs/serah-terima/panduan-instalasi.md`; `KELOMPOK-10/docs/serah-terima/panduan-operasi.md`; `KELOMPOK-10/docs/serah-terima/penanganan-gangguan.md` |
| W16-T02 | Putu | Merapikan backend, layanan, parameter final, dan contoh konfigurasi. Menulis pemasangan/start-stop, pemeriksaan MQTT/layanan, pencadangan data, serta pemulihan gangguan server. | Paket backend/server final dan bagian panduan instalasi, operasi, gangguan, serta maintenance server. | `KELOMPOK-10/docs/serah-terima/panduan-instalasi.md`; `KELOMPOK-10/docs/serah-terima/panduan-operasi.md`; `KELOMPOK-10/docs/serah-terima/penanganan-gangguan.md`; `KELOMPOK-10/backend/`; `KELOMPOK-10/configs/`; `KELOMPOK-10/infra/`; `KELOMPOK-10/docs/serah-terima/panduan-maintenance.md` |
| W16-T03 | Ramdhani | Merapikan firmware/pin sesuai rangkaian final. Menulis pemasangan, pengoperasian, gangguan, dan pemeriksaan berkala perangkat; mendemonstrasikan lampu, OLED, serta cadangan/pemulihan. | Firmware dan dokumentasi perangkat final, foto, rekaman demonstrasi, dan bagian panduan perangkat. | `KELOMPOK-10/docs/serah-terima/panduan-instalasi.md`; `KELOMPOK-10/docs/serah-terima/panduan-operasi.md`; `KELOMPOK-10/docs/serah-terima/penanganan-gangguan.md`; `KELOMPOK-10/docs/serah-terima/panduan-maintenance.md`; `KELOMPOK-10/firmware/esp32/`; `KELOMPOK-10/docs/perangkat/perakitan.md`; `KELOMPOK-10/evidence/S08/prototipe-final.jpg`; `KELOMPOK-10/evidence/S08/demonstrasi-final.mp4` |
| W16-T04 | Ikrom | Menyusun laporan akhir dengan masukan teknis anggota: implementasi, pengujian, pembahasan, keterbatasan, dan status temuan. Menyatukan panduan serta membuat indeks lokasi seluruh hasil/bukti. | Laporan akhir, laporan uji yang sesuai versi akhir, panduan gabungan, README, dan indeks paket serah terima. | `KELOMPOK-10/docs/laporan/laporan-akhir.docx`; `KELOMPOK-10/docs/pengujian/`; `KELOMPOK-10/README.md`; `KELOMPOK-10/docs/serah-terima/paket-serah-terima.md` |
| W16-T05 | Ikrom | Menyiapkan format pemeriksaan berkala, log maintenance, dan penanganan laporan gangguan dari materi teknis anggota. | Panduan dan format pencatatan maintenance setelah serah terima. | `KELOMPOK-10/docs/serah-terima/panduan-maintenance.md`; `KELOMPOK-10/docs/serah-terima/template-log-maintenance.csv` |
| W16-T06 | Nicy | Memeriksa kelengkapan hasil setiap anggota, kesesuaian dokumen dengan demo/versi uji, serta cakupan layanan maintenance 12 bulan setelah penyerahan. Mengatur serah terima dan mencatat pelaksanaan/hasil penerimaan yang benar-benar terjadi. | Checklist paket, review akhir, dan berita acara yang dilengkapi saat penyerahan berlangsung. | `KELOMPOK-10/docs/serah-terima/paket-serah-terima.md`; `KELOMPOK-10/docs/serah-terima/berita-acara.md`; `KELOMPOK-10/evidence/S08/README.md` |

**Pelaporan:** setiap pelaksana mengisi kegiatan aktual pada `KELOMPOK-10/evidence/S08/log-aktivitas.md`. Nicy memeriksa hasil dan mencatat ringkasan, temuan, serta URL commit pada `KELOMPOK-10/evidence/S08/README.md`, bagian **Minggu 16**.

## 4. Serah hasil antarmodul

| Pemberi → penerima | Hasil yang dibutuhkan | Waktu keterkaitan |
|---|---|---|
| Nicy → seluruh anggota | SRS, pembagian tugas, dan hasil penyelarasan kebutuhan. | Minggu 1; diperbarui jika ada keputusan yang berubah. |
| Putu → Rizky, Ramdhani, Ikrom | Kontrak pesan, identitas, validitas, satuan, dan struktur konfigurasi. | Dirancang minggu 3; dipakai saat pengembangan dan integrasi. |
| Rizky → Putu | Pengukuran jumlah/kepadatan, status validitas, identitas CCTV/frame, serta metadata sesuai kontrak. | Minggu 7–10. |
| Ikrom → Rizky dan Putu | Hitungan manual, metadata sampel, pengamatan layanan, dan pemisahan kalibrasi/uji. | Minggu 8–9 dan 13. |
| Putu → Ramdhani | Rencana durasi dan parameter statis cadangan yang disepakati serta versinya. | Minggu 9–10. |
| Ramdhani → Putu dan Ikrom | ACK serta status fase, mode, dan rencana yang benar-benar dijalankan. | Minggu 10–11. |
| Seluruh pemilik modul → Ikrom dan Nicy | Versi, hasil aktual, bukti uji, kendala, serta bahan panduan teknis. | Minggu 12–16. |

## 5. Pengumpulan, pemeriksaan, dan commit

1. PIC menyimpan hasil pada path lengkap yang tercantum. Path berakhiran `/` adalah folder; nama berkas di dalamnya mengikuti implementasi yang dicatat. Berkas setara yang sudah tersedia dapat digunakan dengan pemetaan jelas pada README sprint.
2. PIC mencatat tanggal, kegiatan, hasil/progres, kendala, dan tindak lanjut yang benar-benar terjadi. Dokumen rencana tidak menjadi bukti pengujian aktual.
3. Nicy memeriksa kelengkapan dan kesesuaian terhadap SRS. Temuan mencantumkan pemilik modul, dampak, dan tindak lanjut; status belum selesai tetap dicatat.
4. Pesan commit anggota menggunakan `Sxx-Wxx: hasil pekerjaan`, dengan dua digit sprint/minggu. Commit pelaporan mingguan menunjuk riwayat yang sudah menggabungkan hasil seluruh PIC minggu tersebut.
5. Setelah push, Nicy mencatat URL commit pelaporan pada bagian minggu terkait di README sprint. URL commit itu dicatat melalui pembaruan berikutnya agar tidak memerlukan tautan ke commit yang belum terbentuk.

**Commit untuk berkas ini:**

```text
S01-W01: susun pembagian pekerjaan tim
```

## 6. Ketentuan penyelesaian dan perubahan

- Hasil diterima setelah isi, lokasi, dan keterkaitannya diperiksa; checklist mengikuti bukti aktual.
- Rencana data adalah 15 siklus kalibrasi dan 15 siklus uji terpisah per CCTV. Kecukupan kategori diperiksa dan data kalibrasi dilengkapi bila perlu. Model/parameter dibekukan sebelum evaluasi independen.
- Statis cadangan dikonfigurasi bersama Putu dan dilaksanakan secara lokal oleh firmware Ramdhani. Jalur pencatatan Ikrom tidak boleh menghambat pengendalian.
- Nicy menyelaraskan perubahan kebutuhan/jadwal dengan pemilik modul dan mencatat dampak pada SRS, Kanban, matriks kebutuhan, serta bukti sprint yang terkait.
- Pengembangan berlangsung 16 minggu. Layanan maintenance 12 bulan dimulai setelah serah terima; minggu 16 menyiapkan panduan dan format pencatatannya. Pelaksanaan layanan mengikuti cakupan KJ dalam SRS, dengan pemilik modul sebagai penanggung jawab teknis sesuai bidangnya.
- Status penetapan dan verifikasi seluruh KF, KNF, dan KJ dirinci pada pekerjaan berikutnya, `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md`.

