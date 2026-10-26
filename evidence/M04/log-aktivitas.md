# Log aktivitas M04

Bagian ini merekap aktivitas M04-B yang dibuktikan melalui keluaran terminal dan gambar hasil pelaksana. Tanggal pencatatan rekap: 26 Oktober 2026. Tanggal dan jam eksekusi tiap perintah tidak dicantumkan dalam keluaran terminal, sehingga kolom tanggal pelaksanaan ditandai belum dikonfirmasi. PIC lain menambahkan tabel untuk kontribusinya sendiri.

## Aktivitas 1 — Lingkungan dan dependensi

| Keterangan | Isian |
|---|---|
| Tanggal | Tanggal pelaksanaan belum dikonfirmasi; dicatat pada 26 Oktober 2026. |
| Nama pelaksana | Rizky Bintang Fadillah |
| Task/Issue | M04-B |
| Aktivitas yang dilakukan | Menyiapkan .venv dan dependensi, memeriksa impor serta lokasi Python aktif, menjalankan pip check, dan mencatat penggunaan CPU. |
| Hasil/progres | Python 3.14.3 dari .venv aktif; impor torch, torchvision, cv2, dan ultralytics berhasil; pip check melaporkan No broken requirements found; Torch build CPU dan CUDA False. |
| Kendala | Penggunaan GPU belum diuji; pemeriksaan nvidia-smi sebelumnya menghasilkan perintah tidak dikenali. |
| Lokasi berkas hasil/bukti | KELOMPOK-10/infra/lingkungan-ai.md; KELOMPOK-10/ai/requirements.txt; KELOMPOK-10/evidence/M04/lingkungan-ai.txt untuk snapshot versi paket. |

## Aktivitas 2 — Pemuatan model dan gambar contoh

| Keterangan | Isian |
|---|---|
| Tanggal | Tanggal pelaksanaan belum dikonfirmasi; dicatat pada 26 Oktober 2026. |
| Nama pelaksana | Rizky Bintang Fadillah |
| Task/Issue | M04-B |
| Aktivitas yang dilakukan | Memuat YOLO11n dan menguji gambar bus bawaan contoh, kemudian memproses tiga cuplikan CCTV dengan CPU, imgsz=640, conf=0.25, dan kelas 2/3/5/7; menyimpan log serta gambar hasil. |
| Hasil/progres | Ketiga gambar CCTV selesai diproses; keluaran mobil/sepeda motor berturut-turut 2/5, 8/0, dan 3/4; inferensi 72.9, 36.2, dan 32.3 ms. |
| Kendala | Tidak ada galat eksekusi yang tampak; beberapa kendaraan terlihat tanpa kotak deteksi. ROI dan evaluasi ketepatan dilaksanakan pada kartu terkait. |
| Lokasi berkas hasil/bukti | KELOMPOK-10/evidence/M04/input/; KELOMPOK-10/evidence/M04/uji-cctv/; KELOMPOK-10/evidence/M04/lingkungan-ai.txt; hasil uji bus sebelumnya dilaporkan berada di KELOMPOK-10/runs/detect/evidence/M04/uji-inferensi/. |

## Aktivitas 3 — Penyusunan berkas kontribusi

| Keterangan | Isian |
|---|---|
| Tanggal | 26 Oktober 2026 — penyusunan rekap dan berkas. |
| Nama pelaksana | Rizky Bintang Fadillah |
| Task/Issue | M04-B |
| Aktivitas yang dilakukan | Menyusun requirements paket utama, dokumentasi lingkungan, ringkasan hasil, dan rekap aktivitas berdasarkan bukti yang tersedia. |
| Hasil/progres | Berkas kontribusi M04-B disiapkan untuk digabungkan pada root repositori sesuai path Kanban; status review PM dan URL commit belum diisi. |
| Kendala | Tanggal pelaksanaan pengujian belum dicatat; hasil dan review PIC lain mengikuti pelaksanaan masing-masing. |
| Lokasi berkas hasil/bukti | KELOMPOK-10/ai/requirements.txt; KELOMPOK-10/infra/lingkungan-ai.md; KELOMPOK-10/evidence/M04/README.md; KELOMPOK-10/evidence/M04/log-aktivitas.md. |
