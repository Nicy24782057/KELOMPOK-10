# Evidence M03 — Penyiapan Format Konfigurasi Backend dan Pesan MQTT

| Item | Keterangan |
|---|---|
| Task/Issue | M03 |
| Pelaksana | Putu |
| Pemantau PM | Nicy |
| Tanggal penyiapan | 26 - October - 2026 |
| Status lokal | Selesai |
| Status review PM | Menunggu pemeriksaan Nicy |

## Ringkasan pekerjaan

Format konfigurasi awal dan pertukaran pesan MQTT telah disiapkan dalam bentuk JSON sebagai acuan bersama backend, AI, dan ESP32. Konfigurasi mencakup pemetaan fase A/B/C, giliran, durasi, serta urutan waktu statis cadangan. Contoh pesan mencakup trigger, measurement, control plan, ACK, dan status perangkat.

Informasi antarpesan dibuat konsisten melalui `message_id`, `message_type`, `schema_version`, `device_id`, `session_id`, `turn_id`, `phase_id`, dan waktu ISO 8601. Contoh hasil measurement juga membedakan jumlah kendaraan nol yang valid dari pengukuran yang tidak tersedia atau tidak valid.

Pemetaan ROI tetap menjadi pekerjaan Rizky. Implementasi pengiriman, penerimaan, dan pelaksanaan pesan pada perangkat menjadi pekerjaan Ramdhani pada kartu integrasi, terutama M10.

## Hasil dan lokasi berkas

- `configs/control.example.json` — contoh konfigurasi fase, durasi, dan waktu statis cadangan.
- `configs/mqtt/trigger.example.json` — contoh pesan pemicu.
- `configs/mqtt/measurement.example.json` — contoh hasil pengukuran AI beserta validitasnya.
- `configs/mqtt/plan.example.json` — contoh rencana fase dan durasi.
- `configs/mqtt/ack.example.json` — contoh konfirmasi pesan.
- `configs/mqtt/status.example.json` — contoh status perangkat.
- `evidence/M03/hasil-pemeriksaan-format.txt` — hasil pemeriksaan format dan temuan.
- `evidence/M03/log-aktivitas.md` — log aktivitas Putu.

## Keputusan format

1. Payload menggunakan JSON UTF-8 dan memiliki `schema_version`.
2. Identitas sesi, giliran, dan fase dibawa bersama pesan yang relevan.
3. Pengukuran valid dengan `vehicle_count: 0` tetap diproses sebagai hasil valid.
4. Pengukuran `unavailable` atau `invalid` menggunakan nilai pengukuran `null` dan alasan bila tersedia.
5. Durasi serta pemetaan pada contoh diberi penanda sementara sampai hasil kalibrasi ditetapkan.

## Pemeriksaan dan tindak lanjut

Hasil pemeriksaan lengkap tersimpan pada `hasil-pemeriksaan-format.txt`. Enam berkas JSON dapat dibaca, field utama konsisten, dan perbedaan status pengukuran sudah jelas. Pengujian broker MQTT serta implementasi firmware dilakukan pada kartu integrasi berikutnya.

## Review PM oleh Nicy

| Pemeriksaan | Status | Catatan |
|---|---|---|
| Konfigurasi fase, durasi, dan fallback | Menunggu review |  |
| Lima format pesan MQTT tersedia | Menunggu review |  |
| Field sesi, giliran, fase, waktu, dan validitas | Menunggu review |  |
| Jumlah kendaraan nol dibedakan dari pengukuran gagal | Menunggu review |  |
| Hasil pemeriksaan format terdokumentasi | Menunggu review |  |
| Kesesuaian untuk integrasi backend, AI, dan ESP32 | Menunggu review |  |

## Bukti pengerjaan / commit

Commit SHA/URL: **diisi setelah commit M03 di-push ke remote**.
