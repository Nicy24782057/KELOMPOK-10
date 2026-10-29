# Rencana pengujian sistem

| Identitas | Nilai |
|---|---|
| Tim / sprint / minggu | KELOMPOK-10 / S01 / 3 |
| Tugas / PIC | W03-T06 / Ikrom Safei |
| Versi / tanggal | 0.1 / 29 Oktober 2026 |
| Status | Rencana UJI-01–UJI-34 tersedia; belum merupakan hasil pelaksanaan |
| Lokasi | `KELOMPOK-10/docs/pengujian/rencana-uji.md` |

## 1. Acuan dan urutan pengujian

ID, hubungan kebutuhan dan substansi hasil harapan mengikuti Tabel 6.2 proposal sempro `FINAL INI A(1).docx`, SRS dan matriks minggu 1. LLD minggu 3 menambahkan langkah operasional dan data batas tanpa menambah target kuantitatif baru. Rujukan nomor persamaan yang berbeda pada sumber dibaca menurut substansinya: kepadatan, titik tengah pusat, dasar+tambahan dan clamp.

| Tahap | Fokus / prasyarat | Pelaksana |
|---|---|---|
| Modul dan perangkat | Perakitan, kamera/ROI, hitungan, kepadatan, kategori/durasi | Ramdhani, Rizky, Putu sesuai modul; Ikrom merekam |
| Kalibrasi dan pembekuan | Data manual, split, K-means, layanan, ambang dan durasi beku | Putu/Rizky/Ikrom |
| Integrasi dan sistem | MQTT–ESP32, timer/lock, OLED, log, gangguan dan beban serentak | Putu/Ramdhani/Ikrom; Rizky AI |
| Evaluasi dan penerimaan | Dataset uji independen, metrik, panduan/serah terima | Ikrom dengan pemilik bidang; Nicy memeriksa |

Jadwal pelaksanaan mengikuti Kanban minggu 4–16; minggu 3 hanya menyiapkan rancangan ini. Kasus dapat dijalankan bertahap ketika prasyarat tersedia. Simulasi ditandai sebagai simulasi; hasil LED/timing/penerimaan ESP32 membutuhkan perangkat aktual.

## 2. Kondisi sebelum kasus dijalankan

- Catat commit kode, versi model/bobot/inferensi, konfigurasi sumber/ROI, parameter kendali, firmware, dependensi, GPU, sistem operasi, layanan dan koneksi aktual.
- Gunakan parameter aktual tervalidasi; fixture `example_only: true` hanya untuk pemeriksaan format/unit atau injeksi pada lingkungan uji yang sengaja mengizinkannya. Jalur operasi menolaknya.
- Ramdhani/Ikrom menetapkan resolusi/metode ukur dan toleransi kuning/merah bersama/pemicu sebelum uji timing. Target respons tetap ≤3000 ms; toleransi transisi tidak memperpanjang target ini.
- Rizky/Ikrom menetapkan dasar/ambang umur frame dan selang frame-ke-hijau yang dapat diterima sebelum pengamatan/uji terkait. Nilai belum tersedia membuat kasus bergantung padanya berstatus terhalang/belum dapat dinilai.
- Sebelum uji akhir, bekukan model, pengamatan, K1/K2, durasi, min/max dan statis. Hari/data uji berbeda dari kalibrasi; laporkan jumlah aktual dan keterwakilan kategori.
- Kontrol gangguan hanya pada lingkungan prototipe milik proyek. Catat pemulihan dan kondisi awal antar-kasus agar gangguan sebelumnya tidak mengubah kesimpulan.

## 3. Bentuk bukti dan status

Gunakan satu run_id untuk satu eksekusi kasus. Minimal: ID UJI/KF/KNF/KJ, tanggal/pelaksana aktual, prasyarat/versi, input dan kondisi, langkah, hasil harapan, nilai/hasil aktual, status, path bukti, temuan/PIC/tindak lanjut, serta referensi uji ulang. Rekap akhir: `KELOMPOK-10/evidence/S06/rekap-kasus-uji.csv`; bukti yang sudah dikumpulkan pada sprint sebelumnya tetap di lokasi asal dan ditautkan.

Folder rencana bukti per kasus dapat memakai `KELOMPOK-10/evidence/S06/UJI-XX/`, dengan `hasil.md`, input fixture/dataset ID, pesan/log `.jsonl`, tabel ukur `.csv`, foto/video atau ekspor query sesuai kasus. Folder tersebut belum dianggap ada sebelum eksekusi.

| Status | Arti |
|---|---|
| Belum diuji | Kasus baru direncanakan, belum ada eksekusi |
| Terhalang | Prasyarat/parameter/alat belum tersedia; sebutkan PIC dan tindak lanjut |
| Lulus | Seluruh kriteria kasus terpenuhi dengan bukti sesuai jenisnya |
| Gagal | Ada kriteria tidak terpenuhi; catat selisih dan temuan |
| Belum dapat dinilai | Data tidak memadai/penyebut tidak tersedia; jangan ditulis lulus |

## 4. Skenario UJI-01–UJI-34

### UJI-01 — Sambungan dan keluaran perangkat

**Kebutuhan:** KF-07, KF-08. **Pelaksana:** Ramdhani; Ikrom merekam. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Papan/modul aktual, skema GPIO, 9 resistor/LED, OLED, satu suplai USB; alat ukur tersedia.

**Langkah:** Saat daya mati cocokkan 9 cabang/polaritas/GND dan empat kabel OLED. Nyalakan satu suplai, ukur rail, jalankan satu keluaran per pin dan tampilan OLED; catat konsumsi/kondisi reset.

**Hasil harapan/kriteria:** Sambungan sesuai tabel pin, resistor tiap LED, keluaran sesuai pin, OLED terbaca, catu bekerja sesuai rancangan; ketidakcocokan dicatat dan diperbaiki.

**Bukti:** Foto rangkaian, tabel GPIO, pengukuran daya dan foto OLED; tidak diganti gambar rancangan.

### UJI-02 — Tiga CCTV dan pemetaan fase

**Kebutuhan:** KF-01, KF-02. **Pelaksana:** Rizky; Ikrom merekam. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Tiga sumber berbeda terdaftar dengan camera_id dan phase A/B/C.

**Langkah:** Baca tiap sumber; simpan frame beserta ID/dimensi/waktu. Minta fase A, B, C bergantian dan cocokkan kamera/ROI yang dipakai dengan konfigurasi.

**Hasil harapan/kriteria:** Ketiga frame tersedia dan identitas/pemetaan fase benar; sumber gagal tetap dilaporkan.

**Bukti:** Tiga frame, metadata pembacaan dan tabel fase→camera_id.

### UJI-03 — Validasi konfigurasi pengamatan

**Kebutuhan:** KF-02, KF-05, KF-11. **Pelaksana:** Rizky + Putu; Ikrom merekam. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Patokan/ukur panjang dan lajur terdokumentasi; konfigurasi valid serta varian rusak.

**Langkah:** Periksa sumber/ROI/dimensi. Injeksi L=0/negatif, lajur=0/noninteger, ROI di luar frame, fase/kamera tidak cocok, K1≥K2 dan parameter durasi tidak terurut.

**Hasil harapan/kriteria:** Konfigurasi sah diterima; yang tidak sah ditolak beserta alasan, tanpa rencana adaptif dari masukan tersebut.

**Bukti:** Konfigurasi per varian, hasil validator, bukti patokan/panjang/lajur.

### UJI-04 — Pemicu dan satu snapshot kamera tujuan

**Kebutuhan:** KF-03, KF-06. **Pelaksana:** Ramdhani + Rizky + Putu; Ikrom merekam. **Status awal:** Belum diuji.

**Prasyarat/masukan:** ESP32/timer dan tiga reader berfungsi; ID pemicu/pengukuran tersedia.

**Langkah:** Amati minimal dua putaran A→B→C→A. Rekam saat trigger melintasi sisa 1000 ms, next_phase, kamera frame terpilih dan jumlah pemanggilan AI per trigger unik.

**Hasil harapan/kriteria:** Satu pemicu per giliran saat sisa satu detik dalam toleransi pra-uji; satu frame utuh kamera berikutnya diproses, tanpa akumulasi antarframe.

**Bukti:** Log monotonic ESP, trigger/measurement, frame_id dan counter inferensi; video timer bila diperlukan.

### UJI-05 — Aturan titik ROI dan koordinat

**Kebutuhan:** KF-02, KF-03. **Pelaksana:** Rizky; Ikrom merekam. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Poligon/fixture bbox diketahui dalam koordinat frame asli.

**Langkah:** Sediakan bbox dengan bottom-center di dalam, tepat di sisi/sudut batas, serta di luar walau bbox beririsan. Ulangi jalur resize/letterbox dengan pemetaan kembali ke frame asli.

**Hasil harapan/kriteria:** Titik dalam/batas dihitung dan luar diabaikan; hasil sama setelah pemetaan koordinat. Kelas di luar empat kelas target diabaikan.

**Bukti:** Gambar anotasi titik/ROI, koordinat fixture dan hasil hitungan.

### UJI-06 — Akurasi hitungan terhadap manual

**Kebutuhan:** KF-03, KF-04, KNF-03. **Pelaksana:** Rizky + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Frame uji terpisah/manual terverifikasi, ROI sama dan model/inferensi beku.

**Langkah:** Jalankan AI pada semua frame uji yang layak; hitung selisih absolut per frame. Rekap n pasangan, kegagalan AI/data, MAE, jumlah manual dan E_N per kamera.

**Hasil harapan/kriteria:** MAE/E_N tersedia per kamera; target E_N≤10% jika Σmanual>0. Penyebut nol atau data tidak cukup diberi belum dapat dinilai untuk E_N, bukan otomatis lulus.

**Bukti:** CSV pasangan kelas/total per frame, frame/anotasi, skrip/rumus dan laporan metrik per kamera.

### UJI-07 — Nol valid dalam ROI

**Kebutuhan:** KF-03, KF-04, KF-05. **Pelaksana:** Rizky + Putu. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Frame valid kosong, konfigurasi sah dan K1>0.

**Langkah:** Proses satu snapshot tanpa empat kelas target di ROI, termasuk fixture objek di luar ROI. Periksa measurement, kategori, usulan dan clamp durasi.

**Hasil harapan/kriteria:** valid=true, count=0, k=0, reason=null, kategori rendah dan durasi sesuai parameter/batas; berbeda dari frame gagal.

**Bukti:** Frame kosong, measurement/plan, hasil hitungan dan perhitungan durasi.

### UJI-08 — Frame gagal dan statis pada lock

**Kebutuhan:** KF-01, KF-10, KF-11, KNF-02. **Pelaksana:** Rizky + Ramdhani + Putu. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Ambang umur/dimensi terdefinisi; statis lokal sah; tidak ada kandidat adaptif lain untuk sasaran.

**Langkah:** Uji satu per satu: buffer kosong, sumber terputus, gagal decode, frame melewati ambang umur, dan dimensi tak sesuai. Tunggu lock tiap giliran.

**Hasil harapan/kriteria:** Measurement invalid dengan count/k null dan alasan; tidak menjadi nol/rencana adaptif baru. Pada lock tanpa kandidat, statis lokal berjalan.

**Bukti:** Fixture gangguan/metadata umur, measurement invalid, lock/status dan video lampu.

### UJI-09 — Rumus kepadatan dan satuan

**Kebutuhan:** KF-04. **Pelaksana:** Rizky + Putu. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Input terkontrol; rumus 1000*N/(L_m*m).

**Langkah:** Hitung N=6,L=100,m=2 (k=30); N=0 (k=0); N=3,L=50,m=1 (k=60). Uji L/m tidak sah dan nilai nonfinite pada validator.

**Hasil harapan/kriteria:** Hasil tepat sesuai rumus/satuan kendaraan/km/lajur; input tidak sah ditolak dan tidak dipaksakan jadi 0.

**Bukti:** Tabel masukan/harapan/aktual dan keluaran validator.

### UJI-10 — Batas kategori K1/K2

**Kebutuhan:** KF-05. **Pelaksana:** Putu; Ikrom memeriksa. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Ambang valid; fixture boleh memakai K1=20,K2=40 secara jelas sebagai data uji.

**Langkah:** Masukkan k=0,19.9,20,20.1,39.9,40,40.1. Tambahkan negatif/nonfinite dan K1≥K2 sebagai kasus invalid.

**Hasil harapan/kriteria:** 0≤k<K1 rendah; K1≤k<K2 sedang; k≥K2 tinggi; nilai/konfigurasi tidak sah ditolak. Gunakan k penuh, bukan pembulatan tampilan.

**Bukti:** Tabel semua batas dan hasil kategori/penolakan.

### UJI-11 — Dasar, tambahan dan pembatasan durasi

**Kebutuhan:** KF-05. **Pelaksana:** Putu; Ikrom memeriksa. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Base/tambahan/batas sah; fixture tidak dipakai sebagai parameter terkalibrasi.

**Langkah:** Dengan min=5,max=40, uji usulan 4,5,20,40,41; harapan 5,5,20,40,40. Periksa base=10 dan tambahan 0/10/20 memberi 10/20/30. Uji tabel kategori yang tidak sesuai base+tambahan.

**Hasil harapan/kriteria:** g_usulan=base+tambahan; g_final=min(g_max,max(g_min,g_usulan)); tabel materialisasi konsisten, min/max sah dan durasi kategori tidak menurun.

**Bukti:** Tabel aritmetika/batas, konfigurasi fixture dan penolakan ketidakcocokan.

### UJI-12 — Urutan, kuning dan merah bersama

**Kebutuhan:** KF-07, KNF-04. **Pelaksana:** Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** GPIO/perangkat aktual; metode/resolusi/toleransi timing sudah ditetapkan.

**Langkah:** Rekam minimal dua putaran utuh pada mode adaptif dan statis. Ukur setiap interval hijau, kuning dan merah bersama; cocokkan GPIO/status dengan video/alat ukur.

**Hasil harapan/kriteria:** Urutan A→B→C→A, maksimal satu hijau, kuning nominal 3 detik dan merah bersama nominal 1 detik sesuai toleransi pra-uji. Pemicu tidak menambah durasi hijau.

**Bukti:** Video/trace GPIO, tabel interval aktual beserta toleransi, log state machine.

### UJI-13 — Respons pemicu sampai plan valid diterima

**Kebutuhan:** KF-06, KNF-01. **Pelaksana:** Putu + Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** ESP32 aktual dengan jam monotonic; pipeline berjalan dan trigger terkait dikenal.

**Langkah:** Untuk tiap giliran sampel, catat t_send trigger dan t_receive pertama plan valid pada ESP32. Hitung response_ms; kaitkan tahap server tanpa mengurangkan jam server dengan ESP.

**Hasil harapan/kriteria:** Target tiap penerimaan valid ≤3000 ms. Laporkan n, nilai, min/rata-rata/maks dan jumlah melewati target; ketiadaan plan dicatat gagal respons/timeout, tidak dibuang.

**Bukti:** Log monotonic/ID, tabel response_ms, log tahap server dan kondisi jaringan.

### UJI-14 — Pesan rusak atau identitas/nilai salah

**Kebutuhan:** KF-11, KNF-07. **Pelaksana:** Putu + Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Perangkat berjalan; fixture normal dan mutasi satu field setiap varian.

**Langkah:** Kirim JSON rusak, schema tak didukung, contoh produksi, controller/session/turn/phase salah, field hilang, tipe salah, k negatif dan green di luar batas.

**Hasil harapan/kriteria:** Pesan ditolak/alasan tersedia; keluaran/timer/kandidat sah tidak berubah. ACK hanya bila identitas dapat diambil; JSON tak terbaca menghasilkan catatan lokal, tanpa ID rekaan.

**Bukti:** Payload varian, ACK/log penolakan dan trace keadaan sebelum/sesudah.

### UJI-15 — Duplikasi trigger dan plan

**Kebutuhan:** KF-06, KF-11, KNF-04. **Pelaksana:** Putu + Ramdhani + Rizky + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Counter inferensi, cache hasil trigger dan ACK; satu rencana sah.

**Langkah:** Kirim trigger identik saat processing dan sesudah selesai; ulangi plan sebelum dan sesudah lock. Kirim plan_id sama dengan isi berbeda sebagai konflik.

**Hasil harapan/kriteria:** Tidak ada inferensi kedua/keputusan berbeda atau reset timer. Plan/ACK identik digunakan kembali; konflik isi ditolak. Ulangi reconnect/restart backend dengan rekonsiliasi untuk memastikan tidak membentuk hasil berbeda.

**Bukti:** Counter AI, ID/isi plan/ACK, cache/restart log serta timer/status.

### UJI-16 — Plan lewat 3 detik sebelum lock

**Kebutuhan:** KF-06, KF-11, KNF-01. **Pelaksana:** Putu + Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Kandidat kosong; injeksi delay dan titik lock lokal dapat diketahui.

**Langkah:** Tunda plan sah hingga misalnya 3500 ms sejak trigger, dengan penerimaan tetap sebelum lock aktual; jangan menaksir dari timestamp server. Amati pelaksanaan berikutnya.

**Hasil harapan/kriteria:** Kandidat dapat diterima dan dijalankan untuk sasaran; response_target_met=false dan kasus target 3 detik gagal. Penerimaan fungsional tidak mengubah penilaian respons.

**Bukti:** t_send/t_receive/t_lock, ACK, status plan yang digunakan dan catatan respons.

### UJI-17 — Plan baru setelah lock

**Kebutuhan:** KF-10, KF-11, KNF-04. **Pelaksana:** Putu + Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Giliran sudah lock, diketahui kandidat/mode/durasi terkunci.

**Langkah:** Kirim plan baru pada/sesudah lock aktual, saat merah bersama dan saat hijau sasaran telah mulai. Bedakan dari retransmisi identik yang pernah ditangani.

**Hasil harapan/kriteria:** Plan baru ditolak turn_locked/turn_mismatch sesuai keadaan; durasi/mode terkunci dan timer aktif tidak berubah. Duplikat identik tetap memakai ACK awal tanpa efek baru.

**Bukti:** Log lock/payload/ACK dan durasi/mode aktual sebelum/sesudah.

### UJI-18 — Statis saat server/komunikasi gagal

**Kebutuhan:** KF-10, KNF-05. **Pelaksana:** Putu + Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** ESP32/daya berfungsi dan statis lokal telah diverifikasi.

**Langkah:** Dalam giliran tanpa kandidat, hentikan backend, broker atau jaringan secara terpisah; tunggu lock dan dua transisi. Uji kondisi kandidat sudah diterima sebelum putus sebagai kontrol.

**Hasil harapan/kriteria:** Tanpa kandidat valid, statis lokal dipakai dan urutan/transisi berlanjut. Kandidat sah yang sudah tersedia dapat tetap digunakan. Gangguan tidak memotong hijau atau membuat timer menunggu jaringan.

**Bukti:** Waktu gangguan, status/trace lokal dan video urutan; konfigurasi statis aktual.

### UJI-19 — Pemulihan ke adaptif

**Kebutuhan:** KF-10, KNF-04. **Pelaksana:** Putu + Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Mode statis berjalan dan layanan dapat dipulihkan.

**Langkah:** Pulihkan sumber/server/jaringan pada hijau statis yang sedang aktif. Kirim rencana untuk giliran sah berikutnya sebelum lock dan amati perubahan.

**Hasil harapan/kriteria:** Hijau aktif tidak dipotong/direset; adaptif digunakan pada giliran berikutnya yang memenuhi syarat. Sesi/pesan usang tidak dihidupkan kembali.

**Bukti:** Timestamp pemulihan, trigger/plan/ACK/status dan video transisi mode.

### UJI-20 — OLED sesuai pelaksanaan

**Kebutuhan:** KF-08. **Pelaksana:** Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** OLED dan log plan/status; kasus adaptif, nol valid, statis dan transisi tersedia.

**Langkah:** Cocokkan fase/lampu, sisa waktu, mode, N/k/kategori dan satuan dengan rencana yang digunakan. Sediakan kandidat berikutnya berbeda untuk memastikan tidak tampil sebagai data aktif.

**Hasil harapan/kriteria:** OLED mengikuti timer/status aktual dan plan aktif. Data statis tidak tersedia tampil --, berbeda dari N/k=0 valid; satuan terbaca.

**Bukti:** Foto/video OLED tiap kondisi beserta plan/status yang dirujuk.

### UJI-21 — Penelusuran dari pemicu sampai eksekusi

**Kebutuhan:** KF-09, KNF-07. **Pelaksana:** Ikrom + Putu + Ramdhani. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Pencatatan berjalan, versi aktual dan satu rantai normal/invalid tersedia.

**Langkah:** Query trigger→measurement→plan→ACK→status green_started berdasarkan controller/session/turn/measurement_id/plan_id. Cocokkan kamera, waktu dan versi; ulangi pada fallback.

**Hasil harapan/kriteria:** Hubungan tidak ambigu; ACK penerimaan dibedakan dari pelaksanaan. Invalid menyimpan alasan tanpa field numerik nol pengganti; statis mengacu config lokal.

**Bukti:** Ekspor query/record InfluxDB, pesan dan tabel hubungan ID.

### UJI-22 — Persistensi setelah restart

**Kebutuhan:** KNF-08. **Pelaksana:** Putu + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Data/konfigurasi penting telah ditulis, volume persisten terpasang.

**Langkah:** Catat ID/jumlah record kontrol dan konfigurasi, restart layanan/container penyimpanan tanpa menghapus volume, lalu query record/config yang sama.

**Hasil harapan/kriteria:** Data/konfigurasi pada penyimpanan persisten tersedia kembali; tidak menyimpulkan pesan yang belum pernah tersimpan pasti pulih.

**Bukti:** Konfigurasi volume, query sebelum/sesudah, keluaran restart dan identitas record.

### UJI-23 — Pencatatan tidak menghambat kendali

**Kebutuhan:** KF-09, KNF-11. **Pelaksana:** Ikrom + Putu + Ramdhani. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Jalur MQTT kendali/backend/ESP tersedia; log dapat dihentikan terpisah.

**Langkah:** Hentikan Node-RED lalu InfluxDB secara terpisah saat kendali aktif. Amati plan/timer/transisi dan respons; pulihkan log dan catat gap data.

**Hasil harapan/kriteria:** Urutan/pergantian tetap berjalan tanpa menunggu penyimpanan. Kegagalan/gap dilaporkan, tidak mengklaim replay penuh tanpa bukti.

**Bukti:** Waktu stop/restart, timer/plan/ACK lokal dan rekap gap/antrean.

### UJI-24 — Beban server gabungan

**Kebutuhan:** KNF-01, KNF-09. **Pelaksana:** Putu + Rizky + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Lingkungan GPU aktual tercatat; tiga reader, AI, backend, Mosquitto, Node-RED dan InfluxDB berjalan bersama.

**Langkah:** Jalankan workload siklus yang dilaporkan, ukur respons ESP dan tiap tahap, CPU/RAM/GPU/VRAM/disk/jaringan serta kegagalan frame/plan. Catat durasi uji dan jumlah giliran.

**Hasil harapan/kriteria:** Sumber daya dan respons tersedia; respons dinilai terhadap ≤3000 ms, kegagalan tidak disembunyikan. CPU sementara tidak membuktikan kecukupan server GPU target.

**Bukti:** Versi/spesifikasi aktual, seri resource/response, log workload dan ringkasan kegagalan.

### UJI-25 — Autentikasi, ACL dan TLS

**Kebutuhan:** KNF-06. **Pelaksana:** Putu + Ramdhani + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Listener/sertifikat/CA dan akun uji sah; tidak memakai kredensial nyata pada laporan publik.

**Langkah:** Uji akun sah, salah password, anonim, sertifikat/hostname tidak dipercaya, koneksi non-TLS dan publish di luar ACL. Verifikasi klien tidak menonaktifkan pengecekan TLS.

**Hasil harapan/kriteria:** Koneksi/akses sah berhasil; yang tidak sah ditolak dan TLS terverifikasi. ESP tetap timer/statis bila koneksi tidak dapat dipercaya.

**Bukti:** Konfigurasi tersamarkan, log penolakan/handshake dan bukti ACL tanpa password/private key.

### UJI-26 — Pemisahan rahasia dari berkas publik

**Kebutuhan:** KNF-06. **Pelaksana:** Nicy + Putu; Ikrom merekam. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Daftar berkas/commit yang akan dibagikan dan pola nama variabel privat.

**Langkah:** Periksa kode, contoh, log, ekspor dan riwayat commit yang dibagikan untuk token/password/private key/alamat berisi kredensial. Pastikan .env privat tidak terlacak dan contoh hanya nama variabel.

**Hasil harapan/kriteria:** Kredensial operasional terpisah. Jika pernah bocor, tindak lanjuti rotasi/pembersihan dan uji ulang; jangan hanya menyamarkan tampilan terakhir.

**Bukti:** Catatan pemeriksaan tanpa menyalin nilai rahasia, daftar file/temuan dan tindak lanjut.

### UJI-27 — Reproduksi versi dan asal parameter

**Kebutuhan:** KNF-10, KNF-12. **Pelaksana:** Nicy + pemilik modul; Ikrom merekam. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Manifest model/dependensi, config/parameter beku dan panduan tersedia.

**Langkah:** Ikuti panduan di lingkungan bersih/tercatat; muat versi model/parameter yang sama. Telusuri K1/K2/durasi ke dataset dan laporan kalibrasi, lalu cocokkan firmware/pin/topik.

**Hasil harapan/kriteria:** Dokumen sesuai implementasi dan versi/asal parameter dapat ditelusuri; ketidakcocokan diperbaiki sebelum penyerahan.

**Bukti:** Manifest/hash, catatan instalasi ulang, config dan rujukan dataset/laporan.

### UJI-28 — Serah terima dan kesiapan maintenance

**Kebutuhan:** KNF-12, KJ-03, KJ-04, KJ-08. **Pelaksana:** Nicy; seluruh PIC menyediakan hasil. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Tahap serah terima dengan prototipe dan laporan akhir tersedia.

**Langkah:** Periksa prototipe, kode/config/parameter, laporan uji, panduan penggunaan/perawatan dan dokumen layanan 12 bulan. Cocokkan daftar kebutuhan dan penerimaan aktual.

**Hasil harapan/kriteria:** Paket serah terima/dokumen layanan lengkap. Pemeriksaan kesiapan tidak membuktikan maintenance 12 bulan telah dilaksanakan; layanan aktual dicatat setelah penyerahan.

**Bukti:** Checklist serah terima, versi artefak, berita acara bila benar-benar dilakukan dan dokumen layanan.

### UJI-29 — Pemisahan, jumlah dan asal sampel

**Kebutuhan:** KNF-07, KNF-10, KNF-12. **Pelaksana:** Ikrom + Rizky + Putu. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Kalibrasi/uji dan metadata rekaman tersedia.

**Langkah:** Audit sample_id, hari rekaman, kamera, periode, frame, split dan versi. Hitung 15+15 rencana per kamera, jumlah aktual per periode/kategori, serta rekaman lanjutan/duplikasi.

**Hasil harapan/kriteria:** Data uji tidak dipakai menetapkan parameter versi yang dinilai, hari berbeda, sampel terlacak; kekurangan/kategori kosong dan pengganti dilaporkan.

**Bukti:** Daftar split, metadata/hash dataset, tabel jumlah dan catatan pembekuan.

### UJI-30 — K-means dan ambang per kamera

**Kebutuhan:** KF-05, KNF-10. **Pelaksana:** Putu + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Kepadatan manual kalibrasi per kamera dan setting algoritma tercatat.

**Langkah:** Jalankan ulang K-means 1D k=3 dengan setting tersimpan, periksa anggota/pusat/rentang, urutkan pusat dan hitung titik tengah. Uji data seragam/kelompok kosong sebagai negatif.

**Hasil harapan/kriteria:** Tiga kelompok tidak kosong, pusat berbeda dan terurut; K1/K2 tepat titik tengah. Data tidak memadai ditandai belum tervalidasi dan ditambah sebelum freeze.

**Bukti:** Dataset input, setting/version, label/ukuran/pusat dan hitungan K1/K2.

### UJI-31 — Kategori sistem versus acuan

**Kebutuhan:** KF-04, KF-05, KNF-03. **Pelaksana:** Rizky + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Data uji terpisah, hitungan AI/manual pada frame sama dan ambang beku yang sama.

**Langkah:** Hitung kategori manual dan AI dari k masing-masing. Buat confusion matrix 3×3 per kamera dengan baris manual/kolom AI, jumlah kelas dan akurasi; laporkan pasangan gagal terpisah.

**Hasil harapan/kriteria:** Akurasi/matriks/jumlah kategori dilaporkan per kamera tanpa ambang kelulusan baru; kategori tidak terwakili terlihat, bukan diasumsikan akurat.

**Bukti:** CSV pasangan kategori, K1/K2 versi, matriks dan akurasi per kamera.

### UJI-32 — Prosedur frame dan kelompok awal

**Kebutuhan:** KF-05, KNF-07, KNF-12. **Pelaksana:** Rizky + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Video menunjukkan awal hijau/garis henti, anotasi kelompok dan template lengkap.

**Langkah:** Pilih contoh selesai hijau pertama, lintas hijau, kosong, hilang identitas, putus rekaman, serta selesai kuning/merah. Cek frame sekitar 5 detik sebelumnya dan kelompok saat awal hijau.

**Hasil harapan/kriteria:** Jumlah frame dan kelompok awal terpisah; hanya hijau dijumlahkan. Ketidakpastian/status benar, T lengkap tidak dibuat dari batas bawah atau peristiwa nonhijau.

**Bukti:** Frame/time offset, video/anotasi anggota, green_segments_json dan status penyelesaian.

### UJI-33 — P90 dan sampel belum pasti

**Kebutuhan:** KF-05, KNF-12. **Pelaksana:** Putu + Ikrom. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Data layanan per kamera/kategori serta fixture lengkap/tidak pasti.

**Langkah:** Untuk T=[2,3,4,5,6,7,8,9,10,11], r=9 dan g_raw=10. Untuk 10 sampel dengan 9 terverifikasi selesai≤g dan 1 unknown, coverage=90%; jika hanya 8 selesai, 80%. Uji kategori kosong.

**Hasil harapan/kriteria:** Nearest-rank dan pembulatan detik benar. Unknown tetap penyebut, tidak menjadi berhasil; kategori kosong tidak punya P90/coverage. Kandidat terkecil hanya dipilih jika target terbukti.

**Bukti:** Tabel urutan/rank/ceil, daftar denominator/indikator, hasil fixture dan data kalibrasi aktual.

### UJI-34 — Cakupan pada durasi akhir

**Kebutuhan:** KF-05, KNF-03, KNF-12. **Pelaksana:** Putu + Ikrom; Nicy memeriksa. **Status awal:** Belum diuji.

**Prasyarat/masukan:** Durasi raw/terurut/clamp dan data layanan kalibrasi/uji terpisah tersedia.

**Langkah:** Per kamera/kategori, hitung ulang coverage pada g_final setelah monotonic/clamp. Tunjukkan fixture cap maksimum yang menurunkan coverage. Sajikan n lengkap/unknown dan hasil kalibrasi versus uji.

**Hasil harapan/kriteria:** Cakupan dibandingkan target ≥90% per kamera/kategori. Hasil di bawah target, kategori kosong dan parameter belum tervalidasi terbuka; tidak merata-ratakan kamera untuk menyembunyikan kegagalan.

**Bukti:** Tabel parameter sebelum/sesudah, indikator per sampel dan ringkasan coverage kalibrasi/uji terpisah.

## 5. Metrik dan keputusan hasil

### 5.1 Hitungan kendaraan

Untuk setiap kamera, n adalah jumlah pasangan frame sah yang dapat dibandingkan. `e_i=|N_AI,i−N_manual,i|`, `MAE=Σe_i/n`, dan `E_N=100×Σe_i/ΣN_manual,i`. Jangan memakai `|ΣN_AI−ΣN_manual|` karena galat berlawanan dapat saling meniadakan. Target E_N ≤10% **per kamera**, tanpa ambang MAE tambahan dari LLD.

Jika n=0, kedua metrik belum dapat dihitung. Jika Σmanual=0, E_N tidak terdefinisi; laporkan MAE dan kecocokan nol. Kegagalan AI/invalid frame dipisahkan dari nilai nol dan dilaporkan jumlah/persentasenya; keberhasilan pada subset tidak menyatakan seluruh pipeline lulus. Jelaskan populasi dan alasan tidak dapat dibandingkan.

### 5.2 Kategori

Kategori acuan memakai k manual dan K1/K2 beku yang juga dipakai sistem. Buat matriks 3×3 untuk rendah/sedang/tinggi per kamera, baris acuan manual dan kolom AI. `akurasi=100×jumlah diagonal/n pasangan kategori sah`. Laporkan n tiap kategori termasuk nol, pasangan tidak tersedia dan keterbatasan. Proposal tidak menetapkan target akurasi numerik kategori tambahan.

### 5.3 Layanan kelompok awal

T_i hanya lengkap bila kelompok awal terverifikasi selesai saat hijau (atau kosong terverifikasi dengan T_i=0). Akumulasi menghitung hijau saja. P90 nearest-rank hanya untuk kategori dengan seluruh T_i diketahui: `r=ceil(0,90n)` dan `g_raw=ceil(T_(r))` detik.

Pada kandidat/final g, `coverage=100×ΣI_i(g)/n_layanan`, dengan I=1 hanya bila selesai terverifikasi dan T_i≤g. Semua sampel layanan berkategori sah yang dipilih, termasuk penyelesaian belum pasti, berada pada penyebut. Unknown bukan keberhasilan. Kategori tanpa sampel belum dapat dinilai. Baris frame/acuan tidak layak yang tak dapat diberi kategori dilaporkan terpisah dengan alasan/pengganti.

Target ≥90% dinilai **per kamera dan kategori** pada durasi akhir setelah pengurutan/clamp. Sajikan tabel kalibrasi dan uji terpisah, termasuk n, jumlah verified/unknown, g_raw, g terurut, min/max, g_final, coverage dan temuan. Batas maksimum dapat mengurangi coverage; jangan mengubah label unknown agar mencapai target.

### 5.4 Respons dan timing

`response_ms = t_plan_valid_received_ESP − t_trigger_sent_ESP` pada jam monotonic dalam sesi yang sama. Target ≤3000 ms. ACK retransmisi mempertahankan nilai penerimaan pertama; waktu penerbitan ACK atau waktu server bukan pengganti. Laporkan n, setiap nilai, statistik ringkas, jumlah lewat target dan tidak ada plan. Fallback yang benar tidak menjadikan respons adaptif terlambat sebagai lulus.

Kuning 3 detik, merah bersama 1 detik, pemicu sisa 1 detik dan posisi lock diperiksa dengan metode/toleransi pra-uji. Lock aktual sebelum merah bersama memisahkan plan terlambat yang masih boleh menjadi kandidat dari plan baru yang wajib ditolak. Interval nominal pemicu→hijau berikutnya sekitar 5 detik bukan target respons.

## 6. Register prasyarat yang masih perlu ditetapkan

| ID | Keputusan/data | PIC | Batas sebelum kasus |
|---|---|---|---|
| PU-01 / KT-01 | Varian/bobot YOLO, setting inferensi dan lingkungan/versi aktual | Rizky | UJI-06, UJI-24, UJI-27, UJI-31 dan evaluasi akhir |
| PU-02 / KT-02 | Sumber, ROI, ukuran/lajur, dasar/ambang umur, keterlihatan sinyal dan toleransi frame-ke-hijau | Rizky + Ikrom | UJI-02–UJI-08, UJI-29, UJI-32 |
| PU-03 / KT-03 | Dataset kalibrasi, K-means/ambang/durasi/batas, statis lokal sah dan pembekuan | Putu + Rizky + Ikrom + Ramdhani | UJI operasional, UJI-30–UJI-34 |
| PU-04 / KT-04 | Papan/pin/OLED aktual, resolusi alat dan toleransi timing | Ramdhani + Ikrom | UJI-01, UJI-04, UJI-12–UJI-20 |
| PU-05 / KT-05 | Penempatan server/GPU, layanan/volume/TLS/ACL, lama dan jumlah giliran beban | Putu + Rizky | UJI-21–UJI-27 |
| PU-06 / KT-06 | Penyelarasan ruang lingkup pembanding non-YOLO pada naskah | Nicy + Rizky | Sebelum lingkup evaluasi final; tidak menambah UJI rekaan |
| PU-07 / KT-07–KT-08 | Judul, rujukan persamaan dan instruksi editorial naskah sumber | Nicy bersama pemilik materi | Sebelum dokumen akhir/prosedur dibekukan |

## 7. Pencatatan temuan dan uji ulang

Ikrom menyimpan hasil aktual dan memberi setiap temuan ID, dampak, bukti, PIC, tindak lanjut dan versi perbaikan. Pemilik modul memperbaiki, kemudian ulangi kasus gagal dan kasus yang terpengaruh perubahan (misalnya perubahan lock memerlukan UJI-13–UJI-19). Pertahankan hasil awal serta hasil ulang; jangan menimpa run lama agar terlihat selalu lulus.

Nicy menilai kelengkapan bukti dan keputusan penerimaan saat review aktual. Rancangan ini tidak mengisi nilai hasil, nama pelaksana seolah telah menjalankan kasus, tanda tangan, atau URL commit yang belum ada. Review KJ lain yang tidak memiliki UJI sumber dicatat sebagai review administratif KJ terkait, tanpa menambah nomor UJI-35 dan seterusnya.
