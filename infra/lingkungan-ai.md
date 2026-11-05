# Lingkungan AI — S02 / W04-T02

| Identitas | Nilai |
|---|---|
| Proyek | KELOMPOK-10 |
| PIC | Rizky Bintang Fadillah |
| Sprint / minggu / tugas | S02 / Minggu 4 / W04-T02 |
| Tanggal rekap | 5 November 2026 |
| Status | Lingkungan pengembangan CPU dan pemuatan dua kandidat terverifikasi dari keluaran pengguna; siap review Nicy |
| Acuan tugas | [Issue S02](https://github.com/Nicy24782057/KELOMPOK-10/issues/20) dan pembagian kerja W04-T02 |

## 1. Workflow dan ruang lingkup

Periksa interpreter proyek → pasang dependensi CPU di `.venv` → periksa impor dan dependensi → unduh bobot kandidat → muat pada CPU → catat versi, SHA256, dan hasil aktual.

Pemeriksaan ini menyiapkan lingkungan pengembangan sementara di laptop. Lingkungan implementasi satu server Ubuntu beserta GPU dan beban gabungan mengikuti rancangan S01 dan diperiksa pada perangkat target saat tersedia.

Issue S02 W04-T02 yang diperiksa pada 5 November 2026 meminta beberapa kandidat YOLO yang kompatibel. YOLO11n dan YOLO11s pralatih masing-masing telah berhasil dimuat pada CPU dan dicatat sebagai kandidat awal. Pemilihan model final menggunakan hasil evaluasi ketepatan hitungan, waktu inferensi, dan sumber daya pada tahap implementasi AI, kemudian dibekukan sebelum evaluasi pada data uji terpisah. Ketentuan kandidat ini sejalan dengan dokumen pembagian kerja.

## 2. Lingkungan yang benar-benar diperiksa

| Komponen | Hasil aktual / dasar |
|---|---|
| Sistem operasi | Windows 11 x64; keluaran platform awal `Windows-11-10.0.26200-SP0` |
| Python | 3.14.3 |
| Root proyek | `C:\Users\ACER\Downloads\Github\KELOMPOK-10` |
| Interpreter proyek | `C:\Users\ACER\Downloads\Github\KELOMPOK-10\.venv\Scripts\python.exe` |
| Virtual environment | `sys.prefix != sys.base_prefix` menghasilkan `True` |
| PyTorch | `2.14.1+cpu` |
| Torchvision | `0.29.1+cpu` |
| OpenCV | Paket `opencv-python==5.0.0.93`; `cv2.__version__` menghasilkan `5.0.0` |
| Ultralytics | `8.4.189` |
| CUDA pada PyTorch | `torch.cuda.is_available()` menghasilkan `False` |
| Perangkat model | `cpu` |
| Pemeriksaan dependensi | `python -m pip check` melalui interpreter `.venv` menghasilkan `No broken requirements found.` |
| Spesifikasi CPU / kapasitas RAM | Belum dikumpulkan dalam pemeriksaan S02 ini |
| GPU fisik | Belum diverifikasi pada S02; paket PyTorch CPU dan hasil CUDA False tidak menentukan keberadaan GPU fisik |

Seluruh versi dependensi pada `ai/requirements.txt` diambil dari blok `pip freeze` `.venv` pada 2 November 2026 setelah pemuatan YOLO11n. Pemeriksaan YOLO11s pada 5 November mengonfirmasi versi Python, Torch, Torchvision, OpenCV, serta Ultralytics yang sama. Snapshot lengkap bertanggal 2 November menjadi acuan daftar dependensi. File tersebut merupakan snapshot lingkungan Windows/CPU ini. Instalasi ulang bersih dari snapshot serta kesesuaiannya pada Ubuntu/GPU belum diuji.

## 3. Identitas dan hasil pemuatan kandidat

| Butir | YOLO11n | YOLO11s |
|---|---|---|
| Status pemilihan | `kandidat_awal` | `kandidat_awal` |
| Bobot lokal | `models/yolo11n.pt` | `models/yolo11s.pt` |
| Rilis aset | `v8.4.0` | `v8.4.0` |
| Tugas model | `detect` | `detect` |
| Perangkat model | `cpu` | `cpu` |
| Kelas sasaran | `2: car`, `3: motorcycle`, `5: bus`, `7: truck` | `2: car`, `3: motorcycle`, `5: bus`, `7: truck` |
| Mulai pemeriksaan | `2026-11-02T12:33:51.354229+07:00` | `2026-11-05T13:13:03.085780+07:00` |
| Selesai pemeriksaan | Waktu selesai belum dicatat pada sesi lama | `2026-11-05T13:16:18.861038+07:00` |
| Hasil keluaran | `PEMUATAN MODEL BERHASIL` | `STATUS: PEMUATAN YOLO11s BERHASIL` |

Identitas berkas hasil pengunduhan dicatat sebagai berikut.

| Kandidat | SHA256 |
|---|---|
| YOLO11n | `0ebbc80d4a7680d14987a577cd21342b65ecfd94632bd9a8da63ae6417644ee1` |
| YOLO11s | `85a76fe86dd8afe384648546b56a7a78580c7cb7b404fc595f97969322d502d5` |

Sumber bobot resmi tersedia pada [YOLO11n](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo11n.pt) dan [YOLO11s](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo11s.pt). SHA256 kedua berkas yang dilaporkan pengguna cocok dengan field `digest` pada [metadata rilis aset v8.4.0](https://api.github.com/repos/ultralytics/assets/releases/tags/v8.4.0) yang diperiksa pada 5 November 2026. Kecocokan ini memeriksa identitas berkas terhadap metadata penyedia.

Pemeriksaan S02 memuat model, memeriksa tugas deteksi, membaca empat kelas, dan menghitung SHA256. Evaluasi hitungan kendaraan serta waktu inferensi CCTV mengikuti tahap implementasi AI. `imgsz`, confidence, dan IoU tetap kosong pada manifest karena konfigurasi inferensi S02 belum ditetapkan. Waktu mulai dan selesai sesi YOLO11s mencakup pengunduhan serta pemeriksaan lingkungan, sehingga dicatat sebagai batas sesi pemeriksaan.

## 4. Riwayat kendala dan bukti

1. Pada pemeriksaan awal pukul `11:25:15.225239+07:00`, perintah memakai Python global `C:\Program Files\Python314\python.exe`, dengan virtualenv `False`. Impor `torchvision` dan `ultralytics` gagal. Daftar paket global pada blok tersebut memuat paket di luar lingkungan AI proyek.
2. Pemanggilan `.venv\Scripts\python.exe` berikutnya belum menemukan interpreter. Lingkungan proyek kemudian disiapkan dan dependensi dipasang melalui interpreter `.venv`.
3. Impor Torch, Torchvision, OpenCV, dan Ultralytics melalui `.venv` berhasil. Pemeriksaan `pip check` melalui `.venv` lulus berdasarkan keluaran konsol yang diberikan pengguna.
4. Bobot YOLO11n awalnya belum tersedia. Pada sesi 2 November yang dimulai pukul `12:33:51.354229+07:00`, bobot berhasil diunduh dan dimuat di CPU, kemudian `pip freeze` dari `.venv` ditambahkan ke log.
5. Pada 5 November 2026, Rizky menjalankan `ai/periksa_kandidat.py` melalui interpreter `.venv`. YOLO11s berhasil diunduh dan dimuat pada CPU. Tugas, empat kelas, SHA256, waktu mulai, dan waktu selesai tercetak. Skrip menambahkan hasil pemeriksaan ke log S02.

Bukti utama kedua pemuatan, hash, kelas, serta snapshot dependensi adalah log asli `evidence/S02/lingkungan-ai.txt` pada laptop pengguna. Blok awal yang gagal tetap dipertahankan. `No broken requirements found.` pada blok Python global tidak dipakai sebagai bukti konsistensi `.venv`; bukti `.venv` berasal dari perintah eksplisit berikut yang sudah dilaporkan berhasil:

```text
C:\Users\ACER\Downloads\Github\KELOMPOK-10>".venv\Scripts\python.exe" -m pip check
No broken requirements found.
```

Hasil impor konsol yang sudah diberikan:

```text
Python: 3.14.3
Lokasi Python: C:\Users\ACER\Downloads\Github\KELOMPOK-10\.venv\Scripts\python.exe
Virtualenv aktif: True
Torch: 2.14.1+cpu
Torchvision: 0.29.1+cpu
OpenCV: 5.0.0
Ultralytics: 8.4.189
CUDA tersedia: False
```

Karakter progress unduhan yang tidak terbaca pada tampilan CMD dipertahankan pada log asli. Keberhasilan pemuatan ditunjukkan oleh keluaran tugas, perangkat, kelas, hash, dan status akhir.

## 5. Penyiapan ulang pada Windows / CPU

Gunakan Python 3.14.3 dari root repositori. Perintah ini merupakan panduan berdasarkan lingkungan yang diperiksa; reproduksi pada instalasi bersih belum dilaksanakan.

```bat
python --version
python -m venv .venv
".venv\Scripts\python.exe" -m pip install -r ai\requirements.txt
".venv\Scripts\python.exe" -m pip check
```

File requirements memakai indeks tambahan CPU resmi dan mengunci versi `torch`/`torchvision` dengan akhiran `+cpu`. Paket lain tetap dipasang beserta versi snapshot yang tercatat. Semua perintah berikutnya dapat memanggil `.venv\Scripts\python.exe` secara langsung. Aktivasi opsional untuk CMD:

```bat
call .venv\Scripts\activate.bat
```

Untuk pemeriksaan pemuatan kandidat pada instalasi lain, sediakan bobot dari sumber yang tercatat lalu periksa identitasnya:

```bat
if not exist models mkdir models
".venv\Scripts\python.exe" -u -c "from pathlib import Path; import hashlib; from ultralytics import YOLO; p=Path('models/yolo11n.pt'); model=YOLO(str(p)); model.to('cpu'); print('Tugas model:', model.task); print('Perangkat model:', model.device); print('SHA256:', hashlib.sha256(p.read_bytes()).hexdigest()); print('Kelas kendaraan:', {k:v for k,v in model.names.items() if v in ('car','motorcycle','bus','truck')})"
```

Ultralytics dapat mengunduh bobot ketika berkas belum tersedia. Catat hasil aktual pada instalasi baru, cocokkan dengan manifest, dan laporkan bila hash/versinya berbeda. Bobot `.pt` tetap berada lokal sesuai `.gitignore`; manifest menyimpan acuan pengambilannya.

Pemeriksaan YOLO11s yang sudah dijalankan pengguna tersedia lengkap pada `ai/periksa_kandidat.py`. Dari root repositori, jalankan melalui interpreter proyek jika perlu mengulang pemeriksaan pada instalasi lain.

```bat
".venv\Scripts\python.exe" -u ai\periksa_kandidat.py
```

Skrip membuat folder yang diperlukan, memeriksa virtual environment, mencatat versi, memuat bobot pada CPU, memeriksa tugas serta kelas, lalu mencetak SHA256. Hasil pemeriksaan ditambahkan ke `evidence/S02/lingkungan-ai.txt`. Kemajuan unduhan tampil di terminal. Keluaran rinci pemeriksaan disimpan oleh fungsi `catat` di dalam skrip.


## 6. Kesiapan, batas hasil, dan tindak lanjut

| Butir | Status / tindak lanjut |
|---|---|
| Interpreter, impor pustaka, dan dependensi CPU | Terverifikasi pada lingkungan aktual |
| Pemuatan YOLO11n, YOLO11s, dan empat kelas | Terverifikasi pada CPU dari keluaran pengguna |
| Dependensi, manifest dua kandidat, skrip, dan catatan lingkungan | Disusun berdasarkan output aktual; menunggu penggabungan bukti lokal, commit, dan review |
| Konfigurasi inferensi / ketepatan CCTV / ROI | Dilanjutkan sesuai pekerjaan AI S04 |
| Kinerja tiga reader dan seluruh layanan, termasuk respons 3 detik | Belum diukur; dibuktikan pada integrasi/pengujian beban gabungan |
| Lingkungan satu server Ubuntu/GPU target | Menunggu lingkungan aktual dan koordinasi Putu; catat serta periksa kembali versi/build yang digunakan |
| Pemilihan model final | Menggunakan data pengembangan/kalibrasi, lalu bekukan sebelum evaluasi independen |
| Rekap kesiapan / penerimaan | Ikrom merekap W04-T05; Nicy memeriksa W04-T06; belum dicatat diterima |

Status kontribusi Rizky: **siap review untuk lingkungan pengembangan CPU**. Penyelesaian keseluruhan S02 tetap mengikuti hasil seluruh PIC dan penerimaan Nicy.

## 7. Acuan instalasi

- [Python 3.14 — venv](https://docs.python.org/3.14/library/venv.html).
- [PyTorch — pasangan versi dan indeks CPU](https://pytorch.org/get-started/previous-versions/).
- [Ultralytics — instalasi](https://docs.ultralytics.com/quickstart/).
- [Ultralytics — model YOLO11](https://docs.ultralytics.com/models/yolo11/).

Panduan instalasi awal diperiksa pada 2 November 2026. Metadata bobot rilis resmi diperiksa kembali pada 5 November 2026. Nilai versi dan hasil pemuatan bersumber dari output konsol pengguna. Reproduksi pada komputer asisten tidak dilakukan; review paket memeriksa konsistensi dokumen, manifest, dan identitas bobot.
