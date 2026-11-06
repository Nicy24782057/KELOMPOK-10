
# Dokumentasi Lingkungan Server dan Backend

## 1. Tujuan

Dokumentasi ini menjelaskan persiapan lingkungan server backend untuk mendukung sistem AI Adaptive Traffic Signal Control.

Lingkungan server menggunakan Docker untuk menjalankan layanan komunikasi MQTT, pengolahan alur data, dan penyimpanan hasil pengukuran.

## 2. Teknologi yang Digunakan

| Komponen | Teknologi | Versi/Tag |
|---|---|---|
| Sistem Operasi | Ubuntu / Linux | Diisi sesuai lingkungan aktual |
| Container Runtime | Docker Engine | Diisi hasil pemeriksaan |
| Container Management | Docker Compose | Diisi hasil pemeriksaan |
| MQTT Broker | Eclipse Mosquitto | 2 |
| Flow Processing | Node-RED | 4 |
| Database | InfluxDB | 2.7 |

## 3. Arsitektur Layanan

Lingkungan backend terdiri atas tiga layanan utama:

1. Mosquitto
   Berfungsi sebagai MQTT Broker untuk menerima dan meneruskan pesan antara perangkat ESP32 dan backend.

2. Node-RED
   Berfungsi mengelola alur komunikasi dan pemrosesan data dari perangkat maupun layanan backend.

3. InfluxDB
   Berfungsi menyimpan data pengukuran lalu lintas berdasarkan waktu untuk kebutuhan pencatatan dan analisis.

Ketiga layanan dihubungkan melalui jaringan internal Docker menggunakan network backend.

## 4. Konfigurasi Lingkungan

Konfigurasi layanan disimpan pada file:

- infra/compose.yaml
- .env.example

Pengaturan mencakup:

- Port komunikasi MQTT: 1883.
- Port MQTT TLS: 8883.
- Port Node-RED: 1880.
- Port InfluxDB: 8086.
- Zona waktu: Asia/Jakarta.
- Jaringan komunikasi internal Docker.
- Volume persisten untuk penyimpanan data.
- Variabel autentikasi dan konfigurasi layanan.

Kredensial asli disimpan dalam file .env dan tidak dimasukkan ke repository.

## 5. Struktur Penyimpanan

Data layanan menggunakan Docker Named Volumes agar tetap tersimpan ketika container dihentikan atau dijalankan ulang.

Volume yang digunakan:

- mosquitto_data
- nodered_data
- influxdb_data
- influxdb_config

## 6. Langkah Menjalankan Server

### 6.1 Persiapan Konfigurasi

Salin file contoh konfigurasi:

```bash
cp .env.example .env
```

Sesuaikan seluruh nilai konfigurasi pada file .env dengan kredensial yang digunakan.

Pastikan konfigurasi Mosquitto dan file sertifikat TLS telah disiapkan sebelum layanan dijalankan.

### 6.2 Pemeriksaan Docker

Periksa instalasi Docker:

```bash
docker --version
```

Periksa Docker Compose:

```bash
docker compose version
```

### 6.3 Pemeriksaan Konfigurasi

Periksa validitas konfigurasi Docker Compose:

```bash
docker compose config
```

### 6.4 Menjalankan Layanan

Jalankan seluruh layanan:

```bash
docker compose up -d
```

### 6.5 Memeriksa Status Container

Gunakan perintah:

```bash
docker compose ps
```

Periksa log layanan:

```bash
docker compose logs
```

### 6.6 Menghentikan Layanan

Untuk menghentikan seluruh container tanpa menghapus volume:

```bash
docker compose down
```

## 7. Alamat Akses Layanan

| Layanan | Alamat |
|---|---|
| MQTT Broker | localhost:1883 |
| MQTT TLS | localhost:8883 |
| Node-RED | http://localhost:1880 |
| InfluxDB | http://localhost:8086 |

Alamat localhost digunakan untuk akses dari komputer host. Komunikasi antarlayanan di dalam Docker menggunakan nama service sebagai hostname.

## 8. Pemeriksaan Kesiapan Lingkungan

Pemeriksaan dilakukan untuk memastikan setiap layanan dapat dijalankan dan diakses.

| No. | Pemeriksaan | Hasil |
|---|---|---|
| 1 | Docker Engine tersedia | Belum diuji |
| 2 | Docker Compose tersedia | Belum diuji |
| 3 | Container Mosquitto berjalan | Belum diuji |
| 4 | Container Node-RED berjalan | Belum diuji |
| 5 | Container InfluxDB berjalan | Belum diuji |
| 6 | Komunikasi MQTT | Belum diuji |
| 7 | Akses Node-RED | Belum diuji |
| 8 | Akses InfluxDB | Belum diuji |

## 9. Kendala dan Tindak Lanjut

Setiap kendala selama persiapan dan pengujian lingkungan server dicatat berdasarkan kondisi aktual.

| Kendala | Tindak Lanjut | Status |
|---|---|---|
| Belum ada hasil pemeriksaan | Menunggu pengujian layanan | Pending |

## 10. Kesimpulan

Lingkungan backend dirancang menggunakan Docker Compose dengan tiga layanan utama, yaitu Mosquitto, Node-RED, dan InfluxDB.

Konfigurasi telah disusun untuk mendukung komunikasi antarlayanan, pengolahan data, serta penyimpanan data secara persisten.

Status kesiapan akhir ditentukan berdasarkan hasil pemeriksaan aktual setelah seluruh layanan dijalankan dan diuji.
