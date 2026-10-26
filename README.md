# KELOMPOK-10

Repositori ini adalah root proyek **KELOMPOK-10**. Struktur ini menempatkan hasil kerja M01–M16 pada lokasi yang konsisten agar mudah dikembangkan, diperiksa, dan diserahkan.

## Struktur proyek

```text
KELOMPOK-10/
├── ai/                         # Pembacaan CCTV, YOLO, ROI, dan kepadatan
├── backend/                    # Kategori, durasi hijau, komunikasi, integrasi
│   ├── kalibrasi/              # Penetapan ambang kategori dan durasi
│   └── node-red/               # Ekspor alur Node-RED
├── firmware/esp32/             # MQTT, LED, OLED, penguncian rencana
├── configs/                    # Konfigurasi kamera, ROI, kategori, durasi
│   └── mqtt/                   # Contoh format pesan MQTT
├── data/                       # Data pengamatan dan pengujian
│   ├── kalibrasi/
│   ├── uji/
│   └── metadata/
├── models/                     # Identitas, versi, dan lokasi bobot AI
├── infra/                      # Docker, Mosquitto, Node-RED, InfluxDB
├── tests/                      # Pengujian sistem
│   ├── performance/
│   ├── evaluation/
│   └── integration/
├── docs/                       # Dokumentasi teknis dan panduan
│   ├── perangkat/
   ├── operasional/
   ├── kalibrasi/
   ├── pengujian/
   └── serah-terima/
├── evidence/                   # Bukti pekerjaan kartu M01–M16
│   ├── M01/ ... M16/
├── .gitignore
└── README.md
```

## Penempatan hasil kerja

Gunakan path lengkap dari root `KELOMPOK-10/`. Contoh: program CCTV disimpan sebagai `ai/cctv_reader.py`, kode ESP32 sebagai `firmware/esp32/main.ino`, konfigurasi MQTT sebagai `configs/mqtt/contoh-pesan.json`, dan laporan pengujian sebagai `docs/pengujian/laporan.md`. Bukti setiap kartu disimpan pada `evidence/M01/` sampai `evidence/M16/`; kartu gabungan tetap memakai folder kartu yang sama. Hasil M01 yang sudah tersedia harus dipertahankan.

## Langkah awal

```bash
git clone <URL-REPOSITORI>
cd KELOMPOK-10
git status
```

1. Salin konfigurasi contoh dari `configs/` dan isi nilai lokal tanpa memasukkan kredensial.
2. Tempatkan kode sesuai bidangnya, lalu catat cara menjalankan atau mengujinya di `docs/`.
3. Simpan data yang dapat dilacak pada `data/` dan metadata sumber pada `data/metadata/`.
4. Jalankan pengujian dari `tests/` sebelum commit.
5. Simpan ringkasan dan bukti checkpoint pada `evidence/Mxx/`.

`.gitkeep` hanya dipakai pada folder kosong dan dapat dihapus setelah berkas kerja ditambahkan.

## Pemeriksaan akses dan commit

Putu memeriksa bahwa anggota dapat membaca repositori dan memiliki izin sesuai peran, termasuk membuat branch dan push bila diperlukan. Nicy meninjau struktur, README, akses, kendala, dan tindak lanjut pada `evidence/M02/README.md`.

Sebelum push, jalankan:

```bash
git status --short
git diff --cached --check
```

Commit pelaporan M02 yang disarankan:

```text
chore: siapkan struktur repositori dan dokumentasi M02
```
