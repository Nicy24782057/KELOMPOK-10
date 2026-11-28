# S02 — Persiapan Komponen dan Server

## Minggu 4

Ikrom merekap kesiapan komponen dan lingkungan pengembangan. Nicy Putra Pratama memeriksa hasil tiap PIC sebelum menutup Sprint 02. Rekap ini mengikuti [Kanban S02 #20](https://github.com/Nicy24782057/KELOMPOK-10/issues/20).

| Tugas | PIC | Hasil dan status | Lokasi bukti |
|---|---|---|---|
| W04-T01 | Putu | Docker Compose dan konfigurasi Mosquitto tersedia. Catatan Putu menyebut konfigurasi berhasil divalidasi. Panduan lingkungan server dan contoh variabel sudah tersedia di repo. | [Compose](../../infra/compose.yaml), [konfigurasi Mosquitto](../../infra/mosquitto/config/mosquitto.conf), [panduan server](../../infra/lingkungan-server.md), [contoh variabel](../../.env.example) |
| W04-T02 | Rizky | YOLO11n dan YOLO11s berhasil dimuat sebagai kandidat awal di CPU. Varian final ditentukan setelah evaluasi pada tahap implementasi AI. | [Dependensi](../../ai/requirements.txt), [manifest kandidat](../../models/manifest.csv), [lingkungan AI](../../infra/lingkungan-ai.md), [keluaran pemeriksaan](lingkungan-ai.txt) |
| W04-T03 | Ramdhani | Inventaris diperbarui dari daftar Dhani dan konfirmasi tim. Seluruh sembilan LED berhasil menyala pada uji awal. Breadboard tersedia dan daya saat uji berasal dari port USB laptop. | [Inventaris komponen](../../docs/perangkat/inventaris.md) |
| W04-T04 | Putu | Menurut laporan Putu, MQTT publish/subscribe di port 1883 dan MQTT TLS di port 8883 berhasil. Node-RED dan InfluxDB berhasil dijalankan dan diakses secara lokal. | [Laporan pemeriksaan layanan](status-layanan.txt) |
| W04-T05 | Ikrom | Rekap mencakup hasil layanan lokal, pemeriksaan AI di CPU, dan data komponen yang dikonfirmasi tim. Ikrom memeriksa kesesuaian ringkasan dengan inventaris dan log sebelum push. | [Rekap Minggu 4](#minggu-4) dan [log aktivitas](log-aktivitas.md) |
| W04-T06 | Nicy | Review akhir disetujui Nicy pada 28 November 2026. Sprint 2 siap ditutup. | [Review PM](#review-pm) |

### Lingkungan yang diperiksa

| Bagian | Lingkungan dan versi yang tercatat |
|---|---|
| Layanan server | Windows 11, Ubuntu WSL2, dan Docker Desktop. Tag image di Compose adalah `eclipse-mosquitto:2`, `nodered/node-red:4.1-debian`, dan `influxdb:2.7`. Versi Docker dan Compose belum dicatat di dokumen server. |
| AI | Windows 11 dan Python 3.14.3 di `.venv`. PyTorch 2.14.1+cpu, Torchvision 0.29.1+cpu, OpenCV 5.0.0, dan Ultralytics 8.4.189. Pemuatan kedua kandidat tercatat di CPU dengan CUDA `False` pada lingkungan tersebut. |


Hasil di atas berasal dari lingkungan pengembangan sementara. Pemeriksaan pada server Ubuntu dan GPU target, termasuk kinerja AI pada CCTV, mengikuti tahap implementasi. [Acuan server SRS](../../docs/perencanaan/srs.md#52-server)

### Kendala dan tindak lanjut

Putu mencatat penggantian tag image Node-RED ke `4.1-debian`, pembuatan konfigurasi Mosquitto yang semula belum tersedia, dan penggunaan `--env-file` agar Compose membaca file konfigurasi dari lokasi yang benar. [Laporan layanan](status-layanan.txt)

| PIC | Temuan atau kebutuhan | Tindak lanjut |
|---|---|---|
| Putu | `infra/lingkungan-server.md` dan `.env.example` sudah tersedia. Laporan Putu mencatat uji layanan pada lingkungan lokal. | Catat versi Docker/Compose dan hasil pemeriksaan pada server target sesuai panduan. |
| Ramdhani | Jumlah dan tipe komponen yang diketahui serta hasil uji nyala LED tercatat. Daya uji awal memakai USB laptop. | Konfirmasi adaptor saat menyiapkan catu daya mandiri. Cocokkan GPIO firmware dengan sambungan fisik serta uji urutan lampu dan OLED pada S03. |
| Ikrom | Pembaruan inventaris sudah dirujuk dalam rekap dan log kegiatan. | Rekap Minggu 4 sudah di-push oleh Ikrom dan ditinjau Nicy. |

### Review PM

Catatan telaah awal mengikuti bukti pada 9 November 2026. Nicy mengisi keputusan akhir setelah memeriksa pembaruan.

| Butir | Hasil telaah |
|---|---|
| Tanggal dan bukti yang ditelaah | 9 November 2026. Laporan Putu mencatat MQTT standar dan TLS berhasil serta Node-RED dan InfluxDB dapat diakses di lingkungan lokal. Bukti Rizky menunjukkan YOLO11n dan YOLO11s berhasil dimuat sebagai kandidat di CPU. Draf inventaris tersedia sebagai acuan pemeriksaan komponen. |
| Pembaruan 28 November 2026 | Daftar komponen Dhani dan konfirmasi tim sudah dirangkum dalam inventaris. Tim melaporkan semua LED menyala dan ESP32 mendapat daya USB dari laptop saat uji. Pengukuran transisi, konfirmasi sambungan GPIO, dan uji OLED mengikuti pemeriksaan S03. |
| Keputusan kesiapan menuju Sprint 3 | W04-T06 disetujui oleh Nicy Putra Pratama pada 28/11/2026. Bukti uji layanan lokal, pemuatan YOLO11n dan YOLO11s di CPU, serta inventaris komponen diterima. Putu melengkapi catatan versi Docker dan Compose. Ramdhani mengonfirmasi adaptor saat menyiapkan catu daya mandiri. Sprint 2 siap ditutup.   |

### Commit pelaporan

- [`1f51760` — konfigurasi dan laporan layanan Putu](https://github.com/Nicy24782057/KELOMPOK-10/commit/1f517607ff3d1be5fb97c880d6c20976bc82f3f5)
- [`8ad8933` — lingkungan AI dan dua kandidat YOLO Rizky](https://github.com/Nicy24782057/KELOMPOK-10/commit/8ad8933de704c6d651fa3ed450ee25efcf9ab7e3)
- [`87b3443` — draf inventaris Dhani dan acuan tanggal pencatatan](https://github.com/Nicy24782057/KELOMPOK-10/commit/87b3443978af21637ef2c93f43c1a5001c7e4d7b)
- [`41b7193` — penambahan contoh variabel lingkungan](https://github.com/Nicy24782057/KELOMPOK-10/commit/41b7193a0c6296235c7627d5e6c0da73cdfc96c9)

**URL commit pelaporan Minggu 4** — [5225f17](https://github.com/Nicy24782057/KELOMPOK-10/commit/5225f17b2674beb85f7083ee532c6e144484c584).

### Tindak lanjut dokumen Minggu 4

Catatan pemeriksaan berkas 25 November 2026 menggunakan snapshot repositori [`1293fef`](https://github.com/Nicy24782057/KELOMPOK-10/commit/1293fefcf6e6924504bd120186f9d43f39c06f63). Hasil Sprint 1 digunakan sebagai acuan yang sudah tersedia. Tindak lanjut dicatat dalam rekap dan log S02 untuk mendukung W04-T05 dan W04-T06.

| Butir | Hasil pemeriksaan berkas | Tindak lanjut |
|---|---|---|
| Acuan perencanaan | SRS, HLD, rancangan terperinci, prosedur pengamatan, dan rencana uji sudah tersedia pada repositori. | Gunakan [indeks perencanaan](../../docs/perencanaan/indeks-perencanaan.md) sebagai rujukan. Catatan tindak lanjut berikutnya masuk pada sprint pelaksanaannya. |
| Dokumen lingkungan | [Panduan server](../../infra/lingkungan-server.md) tersedia; nama lama menjadi pengarah. `.env.example` belum ditemukan pada snapshot yang diperiksa. | Putu melengkapi contoh variabel lingkungan sebelum rekap kesiapan diperbarui. Pengaturan lokal dan pengujian layanan mengikuti bukti pelaksana. |
| Pelaporan Minggu 4 | Bukti S02 memakai README.md, log-aktivitas.md, status-layanan.txt, dan lingkungan-ai.txt langsung di evidence/S02/. | Gunakan susunan berkas yang sama. Rincian pemeriksaan berkas dicatat pada [log aktivitas S02](log-aktivitas.md). Ikrom memperbarui rekap, lalu Nicy mengonfirmasi review sesuai bukti aktual. |

Pemeriksaan ini memperbaiki rujukan dokumentasi dan pencatatan tindak lanjut S02. Status kesiapan komponen, hasil layanan lama, dan keputusan review tetap mengikuti bukti yang tercatat. Commit yang disarankan untuk perubahan berkas ini: `S02-W04: rapikan rekap dan rujukan dokumen`. URL commit diisi setelah push yang sebenarnya.

### Kelengkapan konfigurasi lingkungan

Pembaruan berkas 25 November 2026 melengkapi tindak lanjut W04-T01 berdasarkan snapshot [`29388b8`](https://github.com/Nicy24782057/KELOMPOK-10/commit/29388b82459d16153dcb10d60c5c949fb58a3e6b). Contoh konfigurasi ditambahkan pada root proyek agar langkah penyiapan pada panduan server mempunyai berkas sumber yang sesuai.

| Butir | Hasil pemeriksaan berkas | Tindak lanjut |
|---|---|---|
| Contoh variabel lingkungan | [.env.example](../../.env.example) tersedia dalam pembaruan ini. Seluruh nama variabel yang dirujuk infra/compose.yaml tercakup, nilai default sesuai Compose, dan isian kredensial masih kosong. | Salin ke .env lokal, lalu isi nilai yang diperlukan sebelum menjalankan layanan. |
| Pencatatan Git | Aturan .gitignore mengizinkan .env.example dan mengabaikan .env lokal. | Sertakan .env.example saat mengunggah pembaruan ke GitHub. |
| MQTT | Contoh mencakup username/password untuk penyiapan passwordfile dan pengujian klien. Mosquitto tetap membaca passwordfile. | Putu menyiapkan passwordfile dan sertifikat lokal mengikuti [panduan server](../../infra/lingkungan-server.md). |
| Rekap S01 | Pada snapshot yang diperiksa, README S01 tergantikan oleh laporan pemeriksaan tambahan. Pembaruan ini memulihkan isi lengkap rekap tersebut persis dari commit [1293fef](https://github.com/Nicy24782057/KELOMPOK-10/commit/1293fefcf6e6924504bd120186f9d43f39c06f63). | Gunakan rekap S01 yang dipulihkan sebagai acuan. Pekerjaan lanjutan tetap dicatat pada sprint pelaksanaannya. |
| Validasi | Format YAML Compose, cakupan variabel, nilai default, placeholder kredensial, aturan Git, dan rujukan berkas diperiksa secara lokal. Docker dan layanan tidak dijalankan ulang dalam penyusunan berkas ini. | Pengujian layanan pada lingkungan pelaksana mengikuti bukti aktual. |

Kekurangan berkas contoh lingkungan yang dicatat sebelumnya ditangani oleh pembaruan ini. Inventaris fisik dan keputusan kesiapan pada rekap tetap mengikuti bukti yang tersedia. Catatan kegiatan ada pada [log aktivitas S02](log-aktivitas.md). Pesan commit yang disarankan: `S02-W04: lengkapi konfigurasi lingkungan dan pulihkan rekap S01`. URL commit ditambahkan setelah push yang sebenarnya.
