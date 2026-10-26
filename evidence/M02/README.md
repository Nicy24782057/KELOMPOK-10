# Evidence M02 — Penyiapan Repositori dan Struktur Modul

## Informasi checkpoint

| Item | Keterangan |
|---|---|
| Task/Issue | M02 |
| Pelaksana | Putu |
| Tanggal penyiapan | 26 Oktober 2026 |
| Pemantau PM | Nicy |
| Status struktur lokal | Selesai |
| Status review PM | Menunggu pemeriksaan Nicy |

## Ringkasan pekerjaan

Struktur awal repositori telah dibuat untuk memisahkan pekerjaan AI, backend, firmware ESP32, konfigurasi, data, pengujian, dokumentasi, dan bukti checkpoint. Berkas `README.md` utama berisi peta direktori, langkah awal penggunaan, alur commit, serta petunjuk penanganan kredensial. Berkas `.gitignore` disiapkan untuk mengecualikan lingkungan lokal, cache, hasil build, log, kredensial, dan artefak model berukuran besar.

Folder yang masih kosong diberi `.gitkeep` sesuai ketentuan. Penanda tersebut dapat dihapus ketika folder mulai berisi berkas kerja.

## Pemeriksaan akses

Pemeriksaan akses remote harus dilakukan pada layanan Git yang digunakan tim karena URL remote dan daftar anggota tidak tersedia di workspace ini. Putu perlu memverifikasi hal berikut sebelum push:

- Putu dapat membaca, membuat branch, commit, dan push ke repositori.
- Nicy dapat membaca repositori dan meninjau commit M02.
- Anggota lain memperoleh izin sesuai kebutuhan tugasnya.
- Branch utama dan aturan pull request mengikuti kesepakatan tim.

Status pemeriksaan pada workspace ini: **belum dapat diverifikasi secara remote**.

## Kendala

Tidak ada kendala pada pembuatan struktur dan berkas lokal. Kendala yang masih perlu ditindaklanjuti adalah pemeriksaan akses remote serta pengisian URL commit setelah perubahan di-push.

## Hasil dan lokasi berkas

| Lokasi | Kegunaan |
|---|---|
| `README.md` | Petunjuk awal dan penjelasan struktur repositori |
| `.gitignore` | Pengabaian berkas lokal, lingkungan pengembangan, dan kredensial |
| `ai/.gitkeep` | Penanda folder pengembangan AI |
| `backend/.gitkeep` | Penanda folder backend dan integrasi |
| `firmware/esp32/.gitkeep` | Penanda folder program ESP32 |
| `configs/.gitkeep` | Penanda folder konfigurasi |
| `data/.gitkeep` | Penanda folder data pengamatan dan pengujian |
| `tests/.gitkeep` | Penanda folder pengujian |
| `docs/.gitkeep` | Penanda folder dokumentasi teknis |
| `evidence/M02/README.md` | Ringkasan hasil penyiapan dan status review |
| `evidence/M02/log-aktivitas.md` | Log aktivitas Putu pada M02 |

## Bukti pengerjaan / commit

Commit SHA/URL: **diisi setelah commit pelaporan M02 di-push ke remote**.

Contoh pesan commit:

```text
chore: siapkan struktur repositori M02
```

## Review PM

Bagian ini diisi Nicy setelah pemeriksaan.

| Pemeriksaan | Status | Catatan |
|---|---|---|
| Struktur folder lengkap | Menunggu review |  |
| README utama jelas | Menunggu review |  |
| `.gitignore` diperiksa | Menunggu review |  |
| Akses anggota diperiksa | Menunggu review remote |  |
| Kendala tercatat | Menunggu review |  |
