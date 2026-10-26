# Repositori Proyek

Repositori ini menjadi tempat kerja bersama untuk pengembangan modul AI, backend, firmware ESP32, konfigurasi, data, pengujian, dokumentasi, dan bukti pengerjaan proyek.

## Struktur direktori

```text
.
├── ai/                         # Pengembangan model dan integrasi AI
├── backend/                    # API, layanan aplikasi, dan integrasi backend
├── firmware/
│   └── esp32/                  # Program dan konfigurasi firmware ESP32
├── configs/                    # Konfigurasi non-rahasia dan contoh konfigurasi
├── data/                       # Data pengamatan, sampel, dan data pengujian
├── tests/                      # Pengujian unit, integrasi, dan validasi
├── docs/                       # Dokumentasi teknis dan keputusan proyek
├── evidence/
│   └── M02/
│       ├── README.md           # Ringkasan hasil penyiapan M02
│       └── log-aktivitas.md    # Log aktivitas Putu pada M02
├── .gitignore                  # Berkas yang tidak boleh masuk ke Git
└── README.md                   # Petunjuk utama repositori
```

Berkas `.gitkeep` digunakan sementara pada folder yang belum berisi berkas kerja. Setelah folder memiliki berkas yang sebenarnya, `.gitkeep` dapat dihapus.

## Langkah awal penggunaan

1. Kloning repositori dan masuk ke direktori proyek.

   ```bash
   git clone <URL-REPOSITORI>
   cd <NAMA-REPOSITORI>
   ```

2. Periksa status dan cabang kerja sebelum membuat perubahan.

   ```bash
   git status
   git branch --show-current
   ```

3. Simpan pekerjaan sesuai modulnya: kode AI di `ai/`, layanan di `backend/`, dan program ESP32 di `firmware/esp32/`.

4. Letakkan konfigurasi yang tidak rahasia atau contoh konfigurasi di `configs/`. Kredensial, token, kata sandi, dan berkas `.env` harus tetap lokal dan tidak boleh di-commit.

5. Simpan data pengamatan atau data uji yang memang perlu dilacak di `data/`. Jangan memasukkan data pribadi atau data berukuran besar tanpa persetujuan tim.

6. Jalankan pengujian yang relevan dari `tests/` sebelum membuat commit.

7. Catat perubahan penting pada `docs/` dan bukti setiap checkpoint pada `evidence/`.

## Alur commit

Gunakan pesan commit yang singkat dan menjelaskan perubahan, misalnya:

```text
chore: siapkan struktur repositori M02
```

Sebelum push, pastikan tidak ada kredensial atau berkas lokal yang ikut terlacak:

```bash
git status --short
git diff --cached --check
```

## Pemeriksaan akses

Putu perlu memastikan anggota yang ditugaskan memiliki akses baca/tulis sesuai perannya dan dapat melakukan push ke remote. Nicy memeriksa kelengkapan struktur, petunjuk awal, pengaturan akses, serta kendala yang dicatat pada `evidence/M02/README.md`.

## Pelaporan M02

Ringkasan pekerjaan dan status review tersedia di [evidence/M02/README.md](evidence/M02/README.md), sedangkan aktivitas harian dicatat pada [evidence/M02/log-aktivitas.md](evidence/M02/log-aktivitas.md).
