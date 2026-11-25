# Pelaksanaan S03 perakitan dan firmware dasar

Tujuan S03 adalah menghasilkan rangkaian ESP32, sembilan LED dan OLED yang menjalankan urutan dasar A–B–C–A. Keluaran tahap ini menjadi dasar integrasi adaptif pada sprint berikutnya.

## Prasyarat dan acuan

Ramdhani mengisi jumlah tersedia, tipe dan kondisi aktual pada [inventaris](../perangkat/inventaris.md). Komponen acuan: satu ESP32-DevKitC V4/WROOM-32D, sembilan LED dengan sembilan resistor 330 ohm, OLED SSD1306 I2C 3,3 V, breadboard, jumper, kabel USB data dan sumber USB sesuai rancangan. Kekurangan dicatat sebelum pekerjaan yang bergantung padanya.

Pakai [perakitan.md](../perangkat/perakitan.md), [skema-rangkaian.svg](../perangkat/skema-rangkaian.svg), dan [pins.example.json](../../configs/pins.example.json). LED merah/kuning/hijau: A 25/26/27, B 14/18/19, C 23/32/33. OLED SDA21/SCL22. Tabel ini adalah rancangan, dan label pin papan aktual tetap diperiksa.

## Tugas dan hasil

| ID | Pelaksana | Pekerjaan | Keluaran |
|---|---|---|---|
| W05-T01 | Ramdhani | Merakit sesuai GPIO proposal, satu resistor per LED, GND bersama dan satu sumber daya | Perakitan diperbarui, foto rangkaian aktual, catatan pin dan komponen |
| W05-T02 | Ramdhani | Menulis firmware dasar dengan timer yang tetap berjalan, A–B–C–A, paling banyak satu hijau, kuning 3 s dan merah bersama 1 s | Kode firmware/esp32/ dan catatan durasi uji dasar |
| W05-T03 | Ramdhani | Menampilkan fase, keadaan lampu dan sisa waktu pada OLED | Kode OLED dan foto tampilan aktual |
| W05-T04 | Ikrom bersama Ramdhani | Mengukur transisi, keluaran dan tampilan menggunakan metode/toleransi yang dicatat sebelum uji | evidence/S03/pemeriksaan-dasar.csv serta foto/video dan temuan |
| W05-T05 | Nicy | Memeriksa kesesuaian rangkaian/kode/bukti dan menetapkan tindak lanjut | evidence/S03/README.md dan keputusan review aktual |

Pilih lingkungan firmware sesuai papan dan lingkungan anggota, lalu catat versi toolchain, board profile, dan dependensi OLED. Paket perencanaan ini tidak menetapkan suatu firmware sudah tersedia atau diuji.

## Durasi uji dasar dan durasi operasional

Durasi hijau untuk uji LED awal dicatat sebagai konfigurasi uji S03. Angka ini belum menjadi durasi kategori adaptif atau statis cadangan terverifikasi. Firmware/demo dasar diberi penanda mode uji. Sebelum pengoperasian adaptif, statis cadangan lokal dan batas durasi harus memenuhi validasi pada SRS/LLD.

## Bukti yang dikumpulkan

- Foto rangkaian aktual dengan GPIO/cabang LED dapat ditelusuri.
- Kode firmware yang menghasilkan keluaran pada foto/video.
- Tabel ukur transisi dan kesesuaian OLED, disertai metode/toleransi pra-uji.
- Log aktivitas sesuai tanggal dan pelaksana sebenarnya.
- Daftar masalah, tindakan, serta hasil uji ulang bila ada.

Simpan bukti pada evidence/S03/ ketika pelaksanaan dimulai. UJI-01, UJI-12, dan UJI-20 menjadi rujukan bagian pemeriksaan yang relevan; kemampuan adaptif/MQTT yang belum dikerjakan diuji pada integrasi sesuai rencana.
