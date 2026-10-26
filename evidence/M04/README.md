# M04 — Persiapan lingkungan pengembangan dan komponen prototipe

Catatan ini memuat hasil M04-B yang disiapkan untuk digabungkan dengan hasil PIC lain. Tanggal pencatatan: 26 Oktober 2026. Kode kartu dan lokasi berkas mengikuti Kanban proyek.

## M04-A — Hasil Putu

Hasil dan status bagian server diisi Putu. Paket kontribusi Rizky ini tidak menyertakan penilaian pelaksanaan M04-A.

## M04-B — Hasil Rizky

PIC: Rizky Bintang Fadillah.

Lingkungan sementara Windows 11, Python 3.14.3, dan .venv berhasil mengimpor dependensi utama serta memproses tiga contoh gambar CCTV dengan YOLO11n pada CPU. Dokumentasi bersumber dari keluaran terminal dan gambar hasil yang disampaikan pelaksana.

### Pemeriksaan

- [x] Dependensi utama terpasang dan berhasil diimpor.
- [x] Perangkat yang digunakan terverifikasi CPU; CUDA False pada build Torch CPU.
- [x] Pemuatan YOLO11n dan pemrosesan tiga gambar CCTV berhasil.
- [x] Versi paket, konfigurasi model uji, bukti, keterbatasan, dan temuan dicatat.
- [ ] Hasil M04-B ditinjau Nicy.

Ketersediaan GPU NVIDIA secara fisik belum dipastikan. Penggunaan GPU dan lingkungan server belum diuji pada catatan ini.

### Hasil aktual

| Masukan | Mobil terdeteksi | Sepeda motor terdeteksi | Bus terdeteksi | Truk terdeteksi | Inferensi |
|---|---:|---:|---:|---:|---:|
| cctv-01.png | 2 | 5 | 0 | 0 | 72.9 ms |
| cctv-02.png | 8 | 0 | 0 | 0 | 36.2 ms |
| cctv-03.png | 3 | 4 | 0 | 0 | 32.3 ms |

Ringkasan waktu per gambar yang dilaporkan pustaka: preprocessing 1.8 ms, inferensi 47.1 ms, postprocessing 8.7 ms.

Hitungan tersebut adalah deteksi seluruh gambar. Penghitungan kendaraan dalam ROI dan evaluasi ketepatan menjadi pekerjaan M06–M07 serta M13. Target respons keseluruhan tiga detik belum dinilai dari uji ini.

### Temuan

- Pada cctv-02 terdapat sepeda motor yang terlihat tanpa kotak deteksi. Pada cctv-03 juga terdapat kendaraan yang belum diberi kotak.
- Kendaraan pada sisi jalan lain ikut dapat terdeteksi karena ROI belum diterapkan.
- Cuplikan menunjukkan kondisi permukaan jalan basah; tiga contoh ini belum mewakili seluruh kondisi operasi.
- Model YOLO11n dan konfigurasi ini berstatus uji awal.
- Log pemrosesan tidak memperlihatkan galat eksekusi. Temuan visual ditindaklanjuti pada M07.

### Lokasi hasil

| Berkas atau folder | Isi |
|---|---|
| KELOMPOK-10/ai/requirements.txt | Empat dependensi utama dengan versi teramati dan indeks tambahan CPU PyTorch. |
| KELOMPOK-10/infra/lingkungan-ai.md | Lingkungan, versi, konfigurasi, langkah pemasangan, hasil, dan keterbatasan. |
| KELOMPOK-10/evidence/M04/lingkungan-ai.txt | Salinan keluaran pip freeze dan uji tiga gambar yang diberikan pelaksana. |
| KELOMPOK-10/evidence/M04/input/cctv-01.png | Gambar masukan pertama. |
| KELOMPOK-10/evidence/M04/input/cctv-02.png | Gambar masukan kedua. |
| KELOMPOK-10/evidence/M04/input/cctv-03.png | Gambar masukan ketiga. |
| KELOMPOK-10/evidence/M04/uji-cctv/cctv-01.jpg | Gambar hasil deteksi pertama. |
| KELOMPOK-10/evidence/M04/uji-cctv/cctv-02.jpg | Gambar hasil deteksi kedua. |
| KELOMPOK-10/evidence/M04/uji-cctv/cctv-03.jpg | Gambar hasil deteksi ketiga. |
| KELOMPOK-10/evidence/M04/log-aktivitas.md | Rekap aktivitas aktual M04-B. |

Bobot model tersedia pada laptop pelaksana di KELOMPOK-10/models/yolo11n.pt. Berkas .pt mengikuti aturan .gitignore repositori.

## M04-C — Hasil Ramdhani

Hasil dan status bagian komponen diisi Ramdhani. Paket kontribusi Rizky ini tidak menyertakan penilaian pelaksanaan M04-C.

## Review PM — Nicy

Hasil review belum dicatat. Bagian ini diisi Nicy setelah memeriksa kontribusi tiap PIC dan tindak lanjutnya.

## Bukti Pengerjaan / Commit

URL commit pelaporan belum dicantumkan. Sesuai Kanban, satu URL commit pelaporan M04 mencakup hasil seluruh PIC, README, dan log aktivitas setelah digabungkan dan di-push.

Status kartu M04 keseluruhan mengikuti kelengkapan hasil ketiga PIC dan review PM.
