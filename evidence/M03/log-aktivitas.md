# Log Aktivitas M03

| Keterangan | Isian |
|---|---|
| Tanggal | 26 - October - 2026 |
| Nama pelaksana | Putu |
| Task/Issue | M03 |
| Aktivitas yang dilakukan | Menetapkan format konfigurasi pengendalian dalam JSON; membuat contoh pesan MQTT untuk trigger, measurement, control plan, ACK, dan status perangkat; menyusun field identitas sesi, giliran, fase, waktu, validitas, kepadatan, kategori, dan durasi; serta memeriksa keterbacaan dan konsistensi format. |
| Hasil/progres | `control.example.json` dan lima contoh pesan MQTT tersedia. Format measurement membedakan jumlah kendaraan nol yang valid dari pengukuran unavailable atau invalid. Hasil pemeriksaan format dan ringkasan M03 sudah dicatat di `evidence/M03/`. Nilai durasi dan pemetaan fase ditandai sebagai parameter sementara. |
| Kendala | Pengujian publish/subscribe broker, implementasi firmware, pemetaan ROI, dan nilai kalibrasi final belum tersedia pada M03 sehingga masih menjadi tindak lanjut kartu terkait. |
| Lokasi berkas hasil/bukti | `configs/control.example.json`, `configs/mqtt/trigger.example.json`, `configs/mqtt/measurement.example.json`, `configs/mqtt/plan.example.json`, `configs/mqtt/ack.example.json`, `configs/mqtt/status.example.json`, `evidence/M03/hasil-pemeriksaan-format.txt`, `evidence/M03/README.md`, dan berkas ini. |
