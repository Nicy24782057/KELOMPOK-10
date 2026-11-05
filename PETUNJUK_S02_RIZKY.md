# Penerapan kontribusi Rizky S02 Minggu 4

Paket ini merangkum hasil aktual YOLO11n pada 2 November 2026 dan YOLO11s pada 5 November 2026. Kedua kandidat berhasil dimuat pada CPU. Hasil lingkungan dan pemuatan berasal dari keluaran yang dikirim Rizky. Manifest beserta dokumentasi telah diperiksa terhadap hasil tersebut.

## Isi dan lokasi tujuan

| Berkas dalam paket | Lokasi pada repositori |
|---|---|
| `ai/requirements.txt` | Snapshot 40 paket `.venv` Windows CPU pada 2 November 2026. |
| `ai/periksa_kandidat.py` | Skrip pemeriksaan YOLO11s yang sudah dijalankan pada 5 November. |
| `models/manifest.csv` | Identitas, SHA256, kelas, versi, dan status dua kandidat. |
| `infra/lingkungan-ai.md` | Lingkungan, hasil, riwayat kendala, petunjuk, dan tindak lanjut. |
| `evidence/S02/log-aktivitas.md` | Catatan kontribusi Rizky tanggal 2 dan 5 November. Gabungkan baris ke log bersama. |

Letakkan berkas di bawah root `KELOMPOK-10/` sesuai path di atas. Jika log bersama sudah berisi aktivitas anggota lain, tambahkan baris Rizky yang belum tercatat. Pertahankan catatan dan tanggal kegiatan sebelumnya.

Bukti utama `evidence/S02/lingkungan-ai.txt` berasal dari laptop Rizky. Pastikan file tersebut memuat sesi YOLO11n, sesi YOLO11s, dan riwayat pemeriksaan sebelumnya. Paket berisi dokumentasi dan skrip, sedangkan log asli dilampirkan dari folder proyek lokal ketika pengumpulan. Bobot `models/yolo11n.pt` dan `models/yolo11s.pt` disimpan lokal mengikuti `.gitignore`.

## Hasil pemeriksaan yang menjadi dasar

| Kandidat | Hasil pemuatan | Perangkat | Status pemilihan |
|---|---|---|---|
| YOLO11n | Berhasil pada 2 November 2026 | CPU | Kandidat awal |
| YOLO11s | Berhasil pada 5 November 2026 | CPU | Kandidat awal |

Empat kelas tersedia pada kedua kandidat, yaitu `car`, `motorcycle`, `bus`, dan `truck`. SHA256 yang dilaporkan pengguna cocok dengan digest pada metadata rilis resmi v8.4.0. Evaluasi ketepatan hitungan, waktu inferensi, dan sumber daya dilakukan pada tahap implementasi AI untuk memilih model final.

Issue [S02 W04-T02](https://github.com/Nicy24782057/KELOMPOK-10/issues/20) yang diperiksa pada 5 November meminta beberapa kandidat. Paket ini telah memuat dua kandidat sesuai lingkup tersebut. Rekap kesiapan server/AI/inventaris serta penerimaan seluruh S02 mengikuti hasil aktual setiap PIC dan review Nicy.

## Ringkasan untuk Ikrom dan Nicy

Gabungkan ringkasan berikut ke bagian Minggu 4 pada `evidence/S02/README.md`.

| ID tugas | PIC | Hasil aktual | Bukti | Status |
|---|---|---|---|---|
| W04-T02 | Rizky Bintang Fadillah | Lingkungan Python 3.14.3 pada `.venv` Windows dan pustaka CPU terperiksa. Dua kandidat pralatih, YOLO11n dan YOLO11s, berhasil dimuat pada CPU. Empat kelas serta SHA256 tercatat. | `ai/requirements.txt`, `ai/periksa_kandidat.py`, `models/manifest.csv`, `infra/lingkungan-ai.md`, serta log asli `evidence/S02/lingkungan-ai.txt` | Siap review untuk lingkungan pengembangan CPU setelah bukti lokal digabungkan; menunggu penerimaan Nicy. |

Nicy mengisi Review PM setelah memeriksa bukti, mencatat hasil yang diterima, temuan, PIC, dan tindak lanjut. URL commit pelaporan diisi setelah hasil yang diperiksa tersedia di GitHub. Perbedaan antara lingkungan CPU sementara dan server Ubuntu/GPU target tercantum di dokumentasi lingkungan.

## Pemeriksaan dan commit kontribusi

Dari root repositori, periksa perubahan, gabungkan log bersama, lalu tinjau staging.

```bat
git status --short
git add ai/requirements.txt ai/periksa_kandidat.py models/manifest.csv infra/lingkungan-ai.md evidence/S02/lingkungan-ai.txt evidence/S02/log-aktivitas.md
git diff --cached --check
git diff --cached --stat
git diff --cached
```

Sesudah hasil staging sesuai kontribusi yang diperiksa, gunakan pesan commit berikut.

```bat
git commit -m "S02-W04: siapkan lingkungan AI CPU dan dua kandidat YOLO"
```

Push mengikuti branch kerja tim yang digunakan. Commit pelaporan gabungan seluruh PIC memakai pesan yang disepakati pada kartu sprint, yaitu `S02-W04: siapkan komponen dan lingkungan server`.

`PETUNJUK_S02_RIZKY.md` memandu pemasangan paket. Berkas kontribusi teknis dan log yang dikumpulkan tercantum pada tabel di atas.
