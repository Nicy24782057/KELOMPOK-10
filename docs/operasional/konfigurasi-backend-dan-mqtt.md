# Format Konfigurasi Backend dan Pesan MQTT (M03)

## Tujuan

M03 menetapkan format awal yang menjadi acuan bersama untuk backend, AI, dan ESP32. M03 hanya menetapkan susunan data; program pengirim, penerima, dan pelaksana pesan dikembangkan pada kartu integrasi, terutama M10.

## Berkas konfigurasi

- `configs/control.example.json` — contoh pemetaan fase A/B/C, giliran, durasi, dan waktu statis cadangan.
- `configs/mqtt/trigger.example.json` — pesan pemicu pengukuran dan perencanaan giliran berikutnya.
- `configs/mqtt/measurement.example.json` — hasil pengukuran AI dan status validitasnya.
- `configs/mqtt/plan.example.json` — rencana fase dan durasi yang dikirim backend.
- `configs/mqtt/ack.example.json` — konfirmasi penerimaan atau penanganan pesan.
- `configs/mqtt/status.example.json` — kondisi perangkat dan fase yang sedang berjalan.

Semua berkas contoh menggunakan JSON UTF-8. Nilai durasi, pemetaan fase, dan konfigurasi fallback diberi penanda sementara karena belum berasal dari kalibrasi. Nilai final diperbarui setelah hasil kalibrasi tersedia.

## Informasi wajib dan konsistensi

Pesan MQTT memakai `message_id`, `message_type`, `schema_version`, `device_id`, `session_id`, `turn_id`, serta identitas fase jika pesan berkaitan dengan fase. Waktu memakai format ISO 8601 dengan zona waktu. `topic` menunjukkan kanal MQTT yang digunakan.

| Jenis pesan | Informasi utama |
|---|---|
| `trigger` | sesi, giliran, fase tujuan, waktu permintaan, dan jendela pengukuran |
| `measurement` | waktu pengukuran, status validitas, jumlah kendaraan, kepadatan, kategori, dan sumber AI |
| `control_plan` | sesi, giliran, fase, masa berlaku, kategori, dan durasi hijau/kuning/all-red |
| `ack` | ID pesan yang dikonfirmasi, status penanganan, waktu, dan alasan bila gagal |
| `device_status` | kondisi perangkat, sesi/giliran/fase aktif, rencana berjalan, waktu, dan fallback |

## Status pengukuran

`measurement_status` membedakan hasil yang dapat dipakai dari hasil yang tidak tersedia atau tidak sah. Jumlah kendaraan nol adalah hasil valid jika `measurement_status` bernilai `valid`, `vehicle_count_status` bernilai `valid_zero`, dan `vehicle_count` bernilai `0`.

- `valid`: hasil dapat dipakai; `vehicle_count` boleh bernilai `0`.
- `unavailable`: pengukuran tidak tersedia; `vehicle_count` dan `density_ratio` harus `null`.
- `invalid`: pengukuran diterima tetapi tidak dapat dipercaya; `vehicle_count` dan `density_ratio` harus `null`, disertai alasan.

Dengan aturan ini, kendaraan yang memang tidak terdeteksi tidak disamakan dengan kamera atau proses AI yang gagal.

## Pemeriksaan integrasi

1. Backend, AI, dan firmware harus memakai nama field, `schema_version`, dan topik yang sama.
2. Penerima harus memeriksa `message_id` agar pesan duplikat tidak diproses dua kali.
3. Rencana hanya dijalankan jika pengukuran valid atau fallback telah diaktifkan sesuai aturan.
4. `duration_source: temporary_config` dan `config_status: temporary_example` tidak boleh dianggap sebagai hasil kalibrasi.
5. Pengujian publish/subscribe dan implementasi perangkat dilakukan pada kartu integrasi terkait.
