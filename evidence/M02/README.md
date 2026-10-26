# Evidence M02 — Penyiapan Repositori dan Struktur Modul

| Item | Keterangan |
|---|---|
| Task/Issue | M02 |
| Pelaksana | Putu |
| Pemantau PM | Nicy |
| Tanggal penyiapan | 26 Oktober 2026 |
| Status lokal | Selesai |
| Status review PM | Menunggu pemeriksaan Nicy |

## Ringkasan pelaksanaan

Root proyek disiapkan sebagai `KELOMPOK-10/` dengan folder AI, backend, firmware ESP32, konfigurasi, data, models, infra, pengujian, dokumentasi, dan evidence. Subfolder kalibrasi, MQTT, pengujian, dokumentasi, serta `evidence/M01/`–`evidence/M16/` juga dibuat sesuai ketentuan. Folder yang masih kosong diberi `.gitkeep`. Berkas M01 yang sudah tersedia tetap dipertahankan.

README utama menjelaskan fungsi folder, contoh path lengkap, lokasi hasil M01–M16, dan langkah awal penggunaan. `.gitignore` mencakup berkas lokal, lingkungan pengembangan, cache, kredensial, log, serta artefak model berukuran besar.

## Pemeriksaan akses

Pemeriksaan akses remote belum dapat dilakukan dari workspace karena URL repositori, daftar anggota, dan layanan Git tim belum tersedia. Setelah remote disambungkan, Putu perlu memastikan akses baca/tulis sesuai peran, Nicy dapat meninjau commit, dan aturan branch/pull request tim berlaku.

## Kendala dan tindak lanjut

Kendala: akses remote dan URL commit belum dapat diverifikasi. Tindak lanjut: sambungkan remote, push commit M02, tempel satu URL commit di bagian bukti, lalu minta review Nicy.

## Hasil dan lokasi berkas

- `README.md` — petunjuk awal, fungsi folder, dan contoh path.
- `.gitignore` — aturan berkas yang diabaikan.
- `ai/`, `backend/`, `firmware/esp32/`, `configs/`, `data/`, `models/`, `infra/`, `tests/`, `docs/` — struktur modul dan submodul.
- `evidence/M01/`–`evidence/M16/` — pengelompokan bukti setiap kartu.
- `evidence/M02/log-aktivitas.md` — log aktivitas Putu.

## Bukti pengerjaan / commit

Commit SHA/URL: **diisi setelah commit M02 di-push ke remote**.

## Review PM oleh Nicy

| Pemeriksaan | Status | Catatan |
|---|---|---|
| Struktur folder dan subfolder | Menunggu review |  |
| README dan konsistensi path | Menunggu review |  |
| `.gitignore` | Menunggu review |  |
| Akses anggota | Menunggu verifikasi remote |  |
| Kendala dan tindak lanjut | Menunggu review |  |
