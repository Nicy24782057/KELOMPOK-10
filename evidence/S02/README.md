
## Minggu 4 — Kesiapan Lingkungan Server

### 1. Hasil Pekerjaan Putu

**PIC:** Putu  
**Tugas:** W04-T01 dan W04-T04

Putu telah menyiapkan lingkungan backend menggunakan Docker Desktop dengan dukungan Ubuntu WSL2. Konfigurasi Docker Compose telah dibuat untuk menjalankan tiga layanan utama, yaitu Mosquitto, Node-RED, dan InfluxDB.

Mosquitto telah dikonfigurasi menggunakan autentikasi username dan password serta sertifikat TLS untuk mendukung komunikasi MQTT yang aman.

### 2. Hasil Pemeriksaan Layanan

| Komponen | Hasil Pemeriksaan |
|---|---|
| Docker Desktop | Berhasil dijalankan |
| Docker Compose | Konfigurasi berhasil divalidasi |
| Mosquitto | Berhasil dijalankan |
| MQTT Port 1883 | Publish-subscribe berhasil |
| MQTT TLS Port 8883 | Komunikasi berhasil |
| Node-RED | Berhasil dijalankan dan diakses |
| InfluxDB | Berhasil dijalankan dan diakses |

### 3. Lokasi Berkas Hasil Pekerjaan

| Berkas | Keterangan |
|---|---|
| infra/compose.yaml | Konfigurasi layanan Docker |
| .env.example | Contoh variabel lingkungan |
| infra/lingkungan-server.md | Dokumentasi lingkungan server |
| infra/mosquitto/config/mosquitto.conf | Konfigurasi MQTT Broker |
| infra/mosquitto/config/passwordfile | Kredensial MQTT (tidak diunggah) |
| infra/mosquitto/certs/ca.crt | Sertifikat CA |
| infra/mosquitto/certs/server.crt | Sertifikat server |
| evidence/S02/status-layanan.txt | Bukti pengujian layanan |
| evidence/S02/log-aktivitas.md | Log aktivitas pelaksana |

### 4. Kendala dan Tindak Lanjut

1. Image Node-RED dengan tag awal tidak tersedia. Diperbaiki menggunakan nodered/node-red:4.1-debian.
2. Konfigurasi Mosquitto belum tersedia pada pemeriksaan awal. Telah dibuat dan disiapkan.
3. Docker Compose memerlukan lokasi file environment secara eksplisit. Diatasi menggunakan parameter --env-file.

### 5. Review PM

**Pemeriksa:** Nicy Putra Pratama

- Hasil yang diterima: Menunggu pemeriksaan.
- Temuan: Menunggu pemeriksaan.
- PIC tindak lanjut: Putu.
- Status tindak lanjut: Menunggu review.

### 6. Commit Pelaporan

**PIC:** Putu

URL commit GitHub:
[Diisi setelah commit dan push berhasil]

