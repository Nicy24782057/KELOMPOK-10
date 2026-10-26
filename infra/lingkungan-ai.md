# Lingkungan AI — M04-B

PIC: Rizky Bintang Fadillah. Pemeriksa: Nicy Putra Pratama.

Tanggal penyusunan catatan: 26 Oktober 2026. Catatan ini berdasarkan keluaran terminal Windows dan gambar hasil yang disampaikan dalam sesi pengerjaan. Jam pelaksanaan pengujian tidak dicatat.

## Tujuan dan status

Memeriksa pemasangan dependensi, perangkat komputasi yang digunakan, pemuatan model, dan pemrosesan gambar contoh sesuai M04-B.

Lingkungan lokal berhasil mengimpor pustaka dan menjalankan inferensi pada tiga gambar CCTV menggunakan CPU. Hasil ini merupakan pemeriksaan lingkungan pengembangan sementara. Lingkungan server operasional mengikuti penyiapan dan verifikasi tim pada kartu terkait.

## Lingkungan yang teramati

| Komponen | Nilai berdasarkan keluaran aktual |
|---|---|
| Sistem operasi | Windows 11; CMD melaporkan build 10.0.26200.9711 |
| Python | 3.14.3, 64 bit (AMD64) |
| Python aktif | C:\Users\ACER\Downloads\Github\KELOMPOK-10\.venv\Scripts\python.exe |
| Folder proyek | C:\Users\ACER\Downloads\Github\KELOMPOK-10 |
| Prosesor yang dilaporkan YOLO | AMD Ryzen 7 8840HS w/ Radeon 780M Graphics |
| RAM | Belum dicatat |
| Perangkat inferensi | CPU, dipilih dengan device=cpu |
| torch.cuda.is_available() | False pada pemeriksaan impor sebelumnya |
| Pemeriksaan nvidia-smi | Perintah tidak dikenali pada CMD |

Torch yang terpasang adalah build CPU. Hasil CUDA False dan perintah nvidia-smi yang tidak dikenali tidak menetapkan ada atau tidaknya GPU NVIDIA secara fisik. Pemakaian GPU untuk inferensi belum diuji.

## Dependensi

| Paket | Versi distribusi terpasang |
|---|---|
| torch | 2.14.1+cpu |
| torchvision | 0.29.1+cpu |
| opencv-python | 5.0.0.93 |
| ultralytics | 8.4.189 |
| numpy, tercatat dalam snapshot | 2.5.2 |

Empat dependensi utama dikunci pada KELOMPOK-10/ai/requirements.txt. Versi lengkap seluruh paket yang teramati tersedia pada KELOMPOK-10/evidence/M04/lingkungan-ai.txt.

Versi cv2.__version__ yang sebelumnya tampil sebagai 5.0.0 adalah versi modul; versi distribusi opencv-python dari pip freeze adalah 5.0.0.93.

Pemeriksaan sebelumnya menunjukkan impor torch, torchvision, cv2, dan ultralytics berhasil. Perintah python -m pip check menghasilkan No broken requirements found. Keluaran kedua pemeriksaan tersebut diberikan secara terpisah dalam percakapan; berkas lingkungan-ai.txt yang disertakan berisi snapshot pip freeze dan pengujian tiga gambar CCTV.

## Model uji

| Pengaturan | Nilai |
|---|---|
| Model | YOLO11n, model deteksi pralatih |
| Lokasi bobot lokal | KELOMPOK-10/models/yolo11n.pt |
| Status pemilihan | Model uji awal M04-B; pemilihan akhir mengikuti evaluasi proyek |
| Ringkasan fused yang dilaporkan | 100 layers; 2,616,248 parameters; 6.5 GFLOPs |
| device | cpu |
| imgsz | 640 |
| conf | 0.25 |
| classes | [2,3,5,7]: car, motorcycle, bus, truck |
| save | True |

Model dibaca dari bobot yang sudah diunduh pada laptop pelaksana. Bobot tersebut dikecualikan oleh .gitignore repositori untuk berkas .pt. Paket bukti ini mencatat lokasi dan nama model; identitas model yang lebih lengkap disiapkan pada M07.

## Masukan uji

Nomor 01–03 mengikuti urutan gambar yang diberikan. Pemetaan kamera ke fase virtual A/B/C dilakukan pada M06.

| Nama unggahan | Masukan lokal | Resolusi unggahan |
|---|---|---|
| image(20261026-083958).png | KELOMPOK-10/evidence/M04/input/cctv-01.png | 790 x 453 |
| image(20261026-084053).png | KELOMPOK-10/evidence/M04/input/cctv-02.png | 797 x 452 |
| image(20261026-084310).png | KELOMPOK-10/evidence/M04/input/cctv-03.png | 793 x 446 |

Ketiga gambar memperlihatkan permukaan jalan basah, kendaraan dengan ukuran berbeda, dan beberapa kendaraan yang saling menutupi sebagian. Sumber URL CCTV dan ukuran frame asli dari stream belum disertakan. Resolusi di atas adalah resolusi berkas unggahan.

## Langkah pemasangan untuk lingkungan CPU sejenis

Jalankan dari root repositori pada CMD Windows dengan Python 3.14.3 tersedia:

~~~bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r ai\requirements.txt
~~~

Langkah ini mendokumentasikan pemasangan pada lingkungan CPU sejenis. Lingkungan yang sudah lulus pemeriksaan tidak perlu dipasang ulang. Requirements mengunci empat paket utama; snapshot seluruh versi dependensi tersedia dalam bukti terminal.

## Pemeriksaan impor dan dependensi

Perintah pemeriksaan yang sebelumnya dijalankan pelaksana:

~~~bat
python -c "import sys, torch, torchvision, cv2, ultralytics; print('Python:', sys.version.split()[0]); print('Lokasi Python:', sys.executable); print('Torch:', torch.__version__); print('Torchvision:', torchvision.__version__); print('OpenCV:', cv2.__version__); print('Ultralytics:', ultralytics.__version__); print('CUDA tersedia:', torch.cuda.is_available())"
python -m pip check
~~~

## Perintah pengujian CCTV yang dijalankan

Folder masukan berisi ketiga PNG pada tabel. Perintah dijalankan dari root repositori dengan .venv aktif:

~~~bat
python -m pip freeze >> evidence\M04\lingkungan-ai.txt
yolo predict model=models/yolo11n.pt source=evidence/M04/input device=cpu imgsz=640 conf=0.25 classes=[2,3,5,7] save=True project="%CD%\evidence\M04" name=uji-cctv >> evidence\M04\lingkungan-ai.txt 2>&1
type evidence\M04\lingkungan-ai.txt
~~~

Project memakai path absolut agar keluaran langsung berada di folder bukti. Pengujian yang tercatat menghasilkan KELOMPOK-10/evidence/M04/uji-cctv/. Pada pengulangan, pustaka dapat memberikan akhiran nomor folder; catat lokasi yang dilaporkan terminal.

Parameter imgsz=640 menyatakan ukuran target pemrosesan. Log aktual melaporkan tensor 384 x 640; ukuran tensor ini berbeda dari resolusi berkas masukan pada tabel.

## Hasil aktual

| Gambar hasil | Car | Motorcycle | Bus | Truck | Inferensi per gambar |
|---|---:|---:|---:|---:|---:|
| KELOMPOK-10/evidence/M04/uji-cctv/cctv-01.jpg | 2 | 5 | 0 | 0 | 72.9 ms |
| KELOMPOK-10/evidence/M04/uji-cctv/cctv-02.jpg | 8 | 0 | 0 | 0 | 36.2 ms |
| KELOMPOK-10/evidence/M04/uji-cctv/cctv-03.jpg | 3 | 4 | 0 | 0 | 32.3 ms |

Angka tersebut merupakan deteksi yang dilaporkan model pada seluruh gambar. Angka ini belum menjadi acuan hitungan manual atau jumlah kendaraan dalam ROI.

Ringkasan pustaka per gambar: preprocessing 1.8 ms, inferensi 47.1 ms, postprocessing 8.7 ms; bentuk tensor (1, 3, 384, 640). Angka ini berasal dari satu eksekusi pada tiga gambar. Respons keseluruhan sejak pemicu ESP32 sampai penerimaan rencana belum diukur; target tiga detik dinilai melalui pengujian integrasi dan M12.

## Temuan visual dan tindak lanjut

1. Pada cctv-02, sepeda motor terlihat tanpa kotak deteksi; log hanya melaporkan mobil. Pada cctv-03 juga terdapat sepeda motor yang belum diberi kotak.
2. Kendaraan pada bagian jalan lain atau kendaraan di luar calon area pengamatan dapat ikut terdeteksi karena pemrosesan menggunakan seluruh gambar.
3. Penetapan ROI, aturan titik tengah bawah bounding box, dan penghitungan satu snapshot diterapkan pada M06–M07. Panjang fisik area dan jumlah lajur harus ditentukan berdasarkan verifikasi sumber serta pengukuran yang dapat dijelaskan.
4. Ketepatan model diperiksa menggunakan hitungan manual dan data yang sesuai. Uji lingkungan ini belum menghasilkan MAE, EN, atau kesimpulan kelayakan model akhir.
5. Cuplikan M04 ini dipakai sebagai contoh pengembangan. Data kalibrasi dan evaluasi independen disiapkan serta dipisahkan sesuai M08 dan M13.

Tidak ada galat pemrosesan yang tampak pada log tiga gambar. Temuan ketepatan deteksi dicatat untuk M07. Ringkasan dan log kontribusi terdapat pada KELOMPOK-10/evidence/M04/README.md serta KELOMPOK-10/evidence/M04/log-aktivitas.md. Pemeriksaan PM belum dicatat.
