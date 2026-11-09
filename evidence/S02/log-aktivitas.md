# Log aktivitas S02 — Minggu 4

Catatan kegiatan tiap pelaksana untuk [rekap kesiapan Sprint 2](README.md). Gunakan tanggal pelaksanaan yang tercatat pada bukti.

## Aktivitas Rizky — W04-T02

Tanggal dan hasil pada bagian ini mengikuti keluaran konsol pemeriksaan lingkungan AI.

| Tanggal | Sprint / minggu | ID tugas | Pelaksana / PIC | Aktivitas aktual | Hasil / progres | Lokasi bukti | Kendala / tindak lanjut |
|---|---|---|---|---|---|---|---|
| 2 November 2026 | S02 / Minggu 4 | W04-T02 | Rizky Bintang Fadillah | Memeriksa interpreter dan impor pustaka AI dari folder proyek. | Pemeriksaan awal menggunakan Python global, virtualenv False; impor torchvision dan ultralytics gagal. | `evidence/S02/lingkungan-ai.txt`, blok awal mulai 11:25:15.225239+07:00 | Pemeriksaan dilanjutkan dengan lingkungan proyek; jejak kegagalan dipertahankan. |
| 2 November 2026 | S02 / Minggu 4 | W04-T02 | Rizky Bintang Fadillah | Menyiapkan `.venv` dan memasang Torch/Torchvision CPU, Ultralytics serta OpenCV melalui interpreter proyek. Memeriksa impor dan dependensi. | Python 3.14.3; virtualenv True; torch 2.14.1+cpu; torchvision 0.29.1+cpu; OpenCV 5.0.0; Ultralytics 8.4.189. Pemeriksaan pip melalui `.venv` menghasilkan No broken requirements found. | Keluaran konsol yang direkap pada `infra/lingkungan-ai.md` | CPU digunakan sebagai lingkungan sementara; lingkungan Ubuntu/GPU target belum diverifikasi. |
| 2 November 2026 | S02 / Minggu 4 | W04-T02 | Rizky Bintang Fadillah | Mengunduh bobot pralatih YOLO11n, memuatnya pada CPU, memeriksa tugas/kelas, menghitung SHA256, dan mengumpulkan pip freeze `.venv`. | Pemuatan berhasil; tugas detect; perangkat cpu; kelas 2/car, 3/motorcycle, 5/bus, 7/truck. SHA256 tercatat pada manifest. Sesi mulai 12:33:51.354229+07:00. | `evidence/S02/lingkungan-ai.txt`; `models/manifest.csv`; bobot lokal `models/yolo11n.pt` | Status model kandidat awal; inferensi CCTV S02 dan pemilihan final menunggu pengembangan/kalibrasi. |
| 2 November 2026 | S02 / Minggu 4 | Pelaporan W04-T02 | Rizky Bintang Fadillah; penyusunan dengan pendampingan asisten | Menyusun snapshot dependensi, manifest kandidat, dokumentasi lingkungan, dan catatan kontribusi berdasarkan output aktual yang diberikan. | Berkas kontribusi tersedia untuk diterapkan ke repositori dan ditelaah Rizky; siap review Nicy setelah penggabungan. | `ai/requirements.txt`; `models/manifest.csv`; `infra/lingkungan-ai.md`; `evidence/S02/log-aktivitas.md` | Ikrom merekap kesiapan; Nicy menyelaraskan penyebutan model pada Kanban dan mencatat hasil review. Commit/push serta persetujuan belum dicatat selesai. |
| 5 November 2026 | S02 / Minggu 4 | W04-T02 | Rizky Bintang Fadillah | Menjalankan `ai/periksa_kandidat.py` melalui Python `.venv`, mengunduh dan memuat kandidat YOLO11s pada CPU. | Berhasil; detect; cpu; empat kelas kendaraan sesuai. Mulai 13:13:03.085780+07:00, selesai 13:16:18.861038+07:00. SHA256 `85a76fe86dd8afe384648546b56a7a78580c7cb7b404fc595f97969322d502d5`. | Log asli `evidence/S02/lingkungan-ai.txt`; `ai/periksa_kandidat.py`; `models/manifest.csv` | Dua kandidat, YOLO11n dan YOLO11s, tersedia untuk evaluasi implementasi. Review Nicy menunggu penggabungan bukti. |
| 5 November 2026 | S02 / Minggu 4 | Pelaporan W04-T02 | Rizky Bintang Fadillah; penyusunan dengan pendampingan asisten | Melengkapi manifest dua kandidat dan memperbarui dokumentasi dari keluaran aktual. Memeriksa kecocokan SHA256 dengan metadata rilis resmi. | Kedua hash cocok dengan digest metadata v8.4.0. Issue S02 sudah memakai beberapa kandidat; tindak lanjut perubahan penyebutan model pada catatan 2 November telah terpenuhi untuk kartu S02. | `models/manifest.csv`; `infra/lingkungan-ai.md`; `PETUNJUK_S02_RIZKY.md` | Ikrom menggabungkan rekap kesiapan. Nicy mencatat hasil review dan URL commit pelaporan setelah penerimaan aktual. |


## Aktivitas Putu — Minggu 4 (S02-W04)

**PIC:** Putu  
**Tanggung Jawab:** Server dan Backend

### Pekerjaan yang Dilaksanakan

1. Menyiapkan lingkungan backend menggunakan Windows 11, Ubuntu WSL2, dan Docker Desktop.
2. Menyiapkan konfigurasi Docker Compose untuk Mosquitto, Node-RED, dan InfluxDB.
3. Membuat konfigurasi variabel lingkungan melalui `.env.example` dan `.env`.
4. Mengonfigurasi Mosquitto dengan autentikasi username/password.
5. Membuat sertifikat CA dan sertifikat server untuk komunikasi MQTT TLS.
6. Menjalankan ketiga layanan backend menggunakan Docker Compose.
7. Menguji komunikasi MQTT standar pada port 1883.
8. Menguji komunikasi MQTT TLS pada port 8883.
9. Memeriksa akses Node-RED dan InfluxDB.
10. Mendokumentasikan hasil pemeriksaan layanan pada `evidence/S02/status-layanan.txt`.

### Hasil Pekerjaan

- Konfigurasi Docker Compose tersedia.
- Mosquitto berhasil menjalankan komunikasi MQTT standar dan TLS.
- Node-RED berhasil dijalankan dan diakses.
- InfluxDB berhasil dijalankan dan diakses.
- Autentikasi MQTT dan verifikasi sertifikat TLS berhasil diuji.
- Bukti pemeriksaan layanan telah disiapkan.

### Kendala dan Perbaikan

- Tag image Node-RED awal tidak tersedia, diperbaiki menggunakan `nodered/node-red:4.1-debian`.
- Konfigurasi Mosquitto belum tersedia, kemudian dibuat.
- Docker Compose memerlukan lokasi `.env` secara eksplisit, diperbaiki menggunakan parameter `--env-file`.

### Status

W04-T01: Selesai.  
W04-T04: Pengujian layanan berhasil.

## Progres Ramdhani, Ikrom, dan Nicy

Bagian ini mencatat progres dokumen per PIC. Tanggal mengikuti penyusunan atau telaah berkas.

| Tanggal | Sprint / minggu | ID tugas | PIC | Aktivitas tercatat | Hasil / progres | Lokasi bukti | Kendala / tindak lanjut |
|---|---|---|---|---|---|---|---|
| 6 November 2026 | S02 / Minggu 4 | W04-T03 | Ramdhani | Penyusunan daftar kebutuhan komponen dari proposal dan SRS untuk pemeriksaan sebelum perakitan. | Draf inventaris sudah memuat jumlah dan spesifikasi acuan ESP32, LED, resistor, OLED, kabel, breadboard, dan catu daya. | `docs/perangkat/inventaris.md` | Ramdhani perlu mencatat jumlah yang tersedia, tipe, kondisi, dan kekurangan berdasarkan cek fisik sebelum S03. |
| 9 November 2026 | S02 / Minggu 4 | W04-T05 | Ikrom | Penggabungan laporan layanan Putu, bukti pemeriksaan AI Rizky, dan draf inventaris ke rekap Minggu 4. | Rekap W04-T01 sampai W04-T06 mencatat bukti, status kesiapan, kendala, dan PIC tindak lanjut. | [Rekap Minggu 4](README.md#minggu-4) | Ikrom perlu mengonfirmasi rekap setelah menerima hasil cek fisik dan pembaruan dokumen server. |
| 9 November 2026 | S02 / Minggu 4 | W04-T06 | Nicy Putra Pratama | Telaah bukti dokumen kesiapan S02 dan pencatatan temuan untuk Review PM. | Catatan review memuat hasil pengujian lokal, pemeriksaan AI di CPU, dan status sementara siap sebagian. | [Review PM](README.md#review-pm) | Nicy perlu mengonfirmasi keputusan akhir setelah hasil inventaris dan bukti tindak lanjut lengkap. |
