# S02 — Persiapan Komponen dan Server

## Minggu 4

Ikrom merekap kesiapan komponen dan lingkungan pengembangan. Nicy Putra Pratama memeriksa hasil tiap PIC sebelum Sprint 3. Draf rekap ini mengikuti [Kanban S02 #20](https://github.com/Nicy24782057/KELOMPOK-10/issues/20).

| Tugas | PIC | Hasil dan status | Lokasi bukti |
|---|---|---|---|
| W04-T01 | Putu | Docker Compose dan konfigurasi Mosquitto tersedia. Catatan Putu menyebut konfigurasi berhasil divalidasi. Nama dan isi dokumen lingkungan serta berkas contoh variabel perlu diselaraskan dengan Kanban. | [Compose](../../infra/compose.yaml), [konfigurasi Mosquitto](../../infra/mosquitto/config/mosquitto.conf), [dokumen server saat ini](../../infra/lingkugan-server.md) |
| W04-T02 | Rizky | YOLO11n dan YOLO11s berhasil dimuat sebagai kandidat awal di CPU. Varian final ditentukan setelah evaluasi pada tahap implementasi AI. | [Dependensi](../../ai/requirements.txt), [manifest kandidat](../../models/manifest.csv), [lingkungan AI](../../infra/lingkungan-ai.md), [keluaran pemeriksaan](lingkungan-ai.txt) |
| W04-T03 | Ramdhani | Draf inventaris berisi jumlah dan spesifikasi acuan. Tanggal cek, jumlah tersedia, tipe, kondisi, serta kekurangan aktual menunggu pencatatan Ramdhani sebelum perakitan. | `docs/perangkat/inventaris.md` |
| W04-T04 | Putu | Menurut laporan Putu, MQTT publish/subscribe di port 1883 dan MQTT TLS di port 8883 berhasil. Node-RED dan InfluxDB berhasil dijalankan dan diakses secara lokal. | [Laporan pemeriksaan layanan](status-layanan.txt) |
| W04-T05 | Ikrom | Rekap awal mencakup hasil layanan lokal, pemeriksaan AI, dan status inventaris. Ikrom mengonfirmasi rekap setelah menerima hasil cek fisik dan pembaruan dokumen server. | [Rekap Minggu 4](#minggu-4) dan [log aktivitas](log-aktivitas.md) |
| W04-T06 | Nicy | Temuan dari telaah dokumen dan status sementara sudah dicatat. Keputusan akhir menunggu konfirmasi Nicy. | [Review PM](#review-pm) |

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
| Putu | Panduan server tersimpan sebagai `infra/lingkugan-server.md`. Daftar pemeriksaannya masih memuat status “Belum diuji”, sedangkan laporan layanan mencatat pengujian lokal. `.env.example` belum ditemukan di root `main` saat rekap. | Samakan nama panduan dengan `infra/lingkungan-server.md`, isi versi serta hasil cek sesuai bukti, dan lengkapi contoh variabel lingkungan tanpa kredensial. |
| Ramdhani | Hasil pengecekan fisik belum tercatat di draf inventaris. | Lengkapi hasil cek dan tindak lanjut kekurangan komponen sebelum perakitan S03. |
| Ikrom | Rekap masih memakai hasil yang tersedia dari Putu dan Rizky serta draf inventaris. | Perbarui status setelah menerima hasil cek Ramdhani dan konfirmasi kelengkapan dari Putu. |

### Review PM

Catatan telaah dokumen berikut disiapkan untuk konfirmasi Nicy Putra Pratama.

| Butir | Hasil telaah |
|---|---|
| Tanggal dan bukti yang ditelaah | 9 November 2026. Laporan Putu mencatat MQTT standar dan TLS berhasil serta Node-RED dan InfluxDB dapat diakses di lingkungan lokal. Bukti Rizky menunjukkan YOLO11n dan YOLO11s berhasil dimuat sebagai kandidat di CPU. Draf inventaris tersedia sebagai acuan pemeriksaan komponen. |
| Temuan, PIC, dan target tindak lanjut | Ramdhani mencatat jumlah tersedia, tipe, kondisi, dan kekurangan aktual sebelum perakitan S03. Putu menyelaraskan nama dan hasil pemeriksaan di panduan server serta melengkapi `.env.example` sebelum rekap final. Ikrom memperbarui rekap setelah kedua hasil tersebut tersedia. |
| Keputusan kesiapan menuju Sprint 3 | **Siap sebagian berdasarkan bukti dokumen.** Bukti awal layanan lokal dan lingkungan AI tersedia. Kesiapan perakitan menunggu konfirmasi stok dan kondisi komponen serta penyelesaian kekurangan yang menghambat. Nicy mengonfirmasi keputusan akhir setelah bukti tindak lanjut lengkap. |

### Commit pelaporan

- [`1f51760` — konfigurasi dan laporan layanan Putu](https://github.com/Nicy24782057/KELOMPOK-10/commit/1f517607ff3d1be5fb97c880d6c20976bc82f3f5)
- [`8ad8933` — lingkungan AI dan dua kandidat YOLO Rizky](https://github.com/Nicy24782057/KELOMPOK-10/commit/8ad8933de704c6d651fa3ed450ee25efcf9ab7e3)

Nicy mengisi URL commit pelaporan Minggu 4 yang mencakup hasil seluruh PIC setelah rekap dan review selesai.
