# Matriks Kebutuhan dan Verifikasi

## Identitas dokumen

| Keterangan | Isi |
|---|---|
| Proyek | Estimasi Kepadatan Kendaraan dari CCTV untuk Pengendalian Lampu Lalu Lintas Adaptif pada Prototipe IoT |
| Tim | KELOMPOK-10 |
| Penyusun | Nicy Putra Pratama — Project Lead dan System Analyst |
| Kode pekerjaan | S01-W01 / W01-T03 |
| Versi / tanggal | 0.1 / 29 Oktober 2026 |
| Status dokumen | Draf untuk pemeriksaan |
| Lokasi pengumpulan | `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md` |
| Acuan utama | Proposal sempro `FINAL INI A(1).docx` |
| Dokumen pendamping | `KELOMPOK-10/docs/perencanaan/srs.md` versi 0.1 dan `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md` versi 0.1 |
| Acuan pelaksanaan | `Kanban_Proyek_Mandiri_Sprint_01-08.md`, versi diselaraskan dengan sempro, 29 Oktober 2026 |

## 1. Tujuan dan dasar pemetaan

Matriks ini menghubungkan **11 kebutuhan fungsional, 12 nonfungsional, dan 10 kebutuhan jasa** dengan pelaksana, cara verifikasi, kriteria hasil, serta jadwal dan bukti yang direncanakan. Nicy menyusun dan memeriksa pemetaan pada minggu 1. PIC teknis melaksanakan penugasan sesuai jadwal, bukan seluruhnya pada minggu 1.

| Acuan dalam proposal | Penggunaan |
|---|---|
| Bab 2 dan Tabel 4.8 | Jadwal, alokasi jam-orang, cakupan jasa, serah terima, serta maintenance. |
| Tabel 4.3 | Kode dan substansi KF-01–KF-11. |
| Tabel 4.5 | Kode dan substansi KNF-01–KNF-12. |
| Tabel 4.6–4.7 dan 4.9–4.10; Subbab 4.5 | Server, penempatan software, hardware, data, dan antarmuka. |
| Bab 5, terutama Subbab 5.3 | Pelaksanaan penghitungan, kalibrasi kategori/durasi, dan pengamatan layanan. |
| Tabel 6.2 | Identitas UJI-01–UJI-34 dan kebutuhan terkaitnya. |
| Tabel 6.3 dan penjelasan Subbab 6.4 | Kriteria fungsi, metrik, target, serta pelaporan keterbatasan. |

Nomor UJI dan hubungannya dengan kebutuhan pada Bagian 3–4 **mengikuti Tabel 6.2**, tanpa membuat nomor UJI tambahan. Ringkasan kriteria mempergunakan penjelasan Bab 4–6 dan SRS agar rujukan persamaan lama tidak mengubah substansi perhitungan. Tujuh kebutuhan jasa tidak diberi ID UJI khusus dalam tabel sumber; kebutuhan tersebut tetap diverifikasi melalui review administrasi/layanan yang dijelaskan pada matriks.

YOLO tetap ditulis sebagai keluarga model. Varian, bobot, dan konfigurasi ditetapkan saat implementasi berdasarkan ketepatan, waktu, dan sumber daya. Persoalan pembanding non-YOLO dicatat pada KT-06; matriks ini tidak menetapkannya sebagai pengujian wajib tambahan.

## 2. Cara membaca dan mengisi status

### 2.1 Status penetapan

| Penanda | Arti |
|---|---|
| T | Substansi atau target kebutuhan telah dinyatakan dalam acuan. Penanda ini bukan pernyataan bahwa implementasi sudah lulus. |
| P | Nilai parameter atau konfigurasi rinci masih harus ditetapkan dan dicatat sebelum pengujian terkait. |
| S | Ada bagian rumusan/rujukan naskah yang perlu diselaraskan. |
| T+P / T+S / T+P+S | Kebutuhan dasarnya sudah ada, dengan tindak lanjut parameter dan/atau penyelarasan yang disebutkan. |

**Status pelaksanaan awal seluruh baris: belum diverifikasi melalui matriks ini.** Belum ada nilai ukur, hasil lulus/gagal, atau bukti pelaksanaan baru yang ditetapkan dalam dokumen ini. Untuk layanan setelah serah terima, realisasinya belum jatuh tempo pada tahap penyusunan minggu 1.

Hasil aktual nantinya dicatat terpisah sebagai **belum diuji, lulus, gagal, atau belum dapat dinilai**, disertai versi, waktu, data, dan lokasi bukti. Ketersediaan dokumen atau keberhasilan satu kasus tidak otomatis meluluskan semua aspek kebutuhan.

### 2.2 Pembagian pemeriksaan

- **Pemilik modul** menyiapkan implementasi, masukan uji, versi, hasil aktual, dan bukti teknis.
- **Ikrom** mengelola acuan manual, metadata, rekap kasus/hasil, serta keterlacakan bukti.
- **Nicy** memeriksa kelengkapan, kesesuaian terhadap kebutuhan, dan tindak lanjut; tidak mengisi hasil teknis tanpa bukti.
- **M** pada kolom waktu berarti minggu proyek. Kalender kegiatan aktual diisi saat pelaksanaan, bukan dihitung dari tanggal draf.

## 3. Matriks kebutuhan

### 3.1 Kebutuhan fungsional

| Kode | Kebutuhan dan sumber | PIC implementasi / penanggung jawab | Cara verifikasi | ID UJI terkait | Kriteria keberhasilan | Status penetapan dan tindak lanjut | Rencana waktu |
|---|---|---|---|---|---|---|---|
| KF-01 | Pembacaan tiga CCTV; frame terbaru dan kegagalan dibedakan dari nol. **Sumber:** Tabel 4.3; SRS 3.1–3.2 dan 8.2. | Rizky; Ikrom mencatat sumber. | Baca tiga sumber, cocokkan ID/fase, lalu uji frame tidak tersedia, gagal dekode, kedaluwarsa, dan dimensi tidak sesuai. | UJI-02, UJI-08 | Tiap kamera menyediakan frame beridentitas benar; kondisi gagal mempunyai status/alasan, bukan hitungan nol sah. | T+P — sumber, waktu, dan umur frame mengikuti KT-02. | Pengembangan M6; integrasi M10; uji M14. |
| KF-02 | Konfigurasi sumber/fase, ROI, panjang, dan lajur. **Sumber:** Tabel 4.3; SRS 3.1–3.3. | Rizky untuk kamera/ROI; Putu untuk validasi config backend. | Cocokkan konfigurasi dengan sumber dan patokan fisik; uji panjang/lajur tidak positif serta titik dalam/batas/luar ROI. | UJI-02, UJI-03, UJI-05 | Pemetaan fase benar; patokan, ukuran, dan ROI terdokumentasi; konfigurasi tidak sah ditolak; aturan titik batas diterapkan. | T+P — konfigurasi aktual menunggu KT-02. | Rancangan M3; penetapan M6; uji M14. |
| KF-03 | YOLO pada satu frame utuh per pemicu; empat kelas dan hitungan ROI. **Sumber:** Tabel 4.3; SRS 2.3 dan 3.1–3.2. | Rizky; Ramdhani/Putu pada jalur pemicu; Ikrom untuk manual. | Periksa satu snapshot per pemicu sah, kelas mobil/motor/bus/truk, titik tengah bawah bounding box, nol valid, dan perbandingan manual pada frame/ROI sama. | UJI-04, UJI-05, UJI-06, UJI-07 | Titik di dalam/pada batas dihitung satu; titik luar diabaikan; hitungan tidak diakumulasi antarframe. E_N ≤10% per kamera pada data uji yang dapat dinilai; MAE/jumlah frame dilaporkan. | T+P — varian/inferensi dan sumber mengikuti KT-01/KT-02; ruang lingkup pembanding pada KT-06. | Pengembangan M7; integrasi M10; evaluasi M13–14. |
| KF-04 | Kepadatan sesaat rata-rata per lajur. **Sumber:** Tabel 4.3; SRS 3.3. | Rizky; Ikrom untuk acuan manual; Putu memakai hasilnya. | Bandingkan fungsi dengan hitungan acuan dari N, panjang meter, dan lajur; sertakan nol sah, nilai tidak sah, serta evaluasi data uji. | UJI-06, UJI-07, UJI-09, UJI-31 | k = 1000 × N / (L_m × m), satuan kendaraan/km/lajur; L_m dan m positif; pengukuran gagal dibedakan dari nol. Evaluasi hitungan/kategori dilaporkan per kamera. | T+P — rumus tetap; panjang/lajur aktual mengikuti KT-02. | Pengembangan M9; evaluasi M13–14. |
| KF-05 | Kategori rendah/sedang/tinggi dan durasi hasil kalibrasi. **Sumber:** Tabel 4.3; SRS 3.4–3.5, 8.3–8.4. | Putu; Rizky/Ikrom menyediakan data dan acuan manual. | Periksa config, frame kosong, batas K1/K2, K-means manual per kamera, P90/cakupan, dasar/tambahan, pembatasan durasi, serta kategori AI vs manual. | UJI-03, UJI-07, UJI-10, UJI-11, UJI-30, UJI-31, UJI-32, UJI-33, UJI-34 | Tiga kelompok tidak kosong/pusat berbeda dan terurut; K1/K2 titik tengah. Rendah 0≤k<K1, sedang K1≤k<K2, tinggi k≥K2. Durasi tidak menurun dan dibatasi; cakupan akhir ≥90% per kamera/kategori; akurasi/matriks kebingungan serta sampel dilaporkan. | T+P+S — KT-03/KT-08; kategori tanpa sampel belum tervalidasi. Perbaikan rujukan persamaan dicatat pada Bagian 6.2. | Kalibrasi M8–9; evaluasi terpisah M13–14. |
| KF-06 | Pemicu sisa hijau satu detik dan rencana fase berikutnya melalui MQTT. **Sumber:** Tabel 4.3; SRS 3.6–3.7 dan 7.3. | Ramdhani pada pemicu/penerimaan; Rizky pada frame; Putu pada plan/MQTT. | Telusuri A→B, B→C, C→A dari pemicu sampai plan; ukur di ESP32; kirim ulang pesan dan uji plan setelah tiga detik tetapi sebelum lock. | UJI-04, UJI-13, UJI-15, UJI-16 | Kamera fase berikutnya diproses satu kali per pemicu sah; target plan valid diterima ≤3 detik. Duplikasi tidak mengulang proses/timer. Plan valid sebelum lock dapat digunakan walau target respons terlewati dan dicatat gagal. | T+P — kontrak dan identitas diperinci melalui KT-04; target 3 detik tetap. | Kontrak M3; integrasi M10; uji M12 dan M14. |
| KF-07 | Urutan A–B–C–A dan transisi lampu. **Sumber:** Tabel 4.3; SRS 3.6 dan 7.2. | Ramdhani; Ikrom merekam hasil aktual. | Periksa sambungan dan keluaran LED; rekam beberapa giliran serta ukur interval terhadap toleransi yang ditetapkan sebelum uji. | UJI-01, UJI-12 | Urutan benar; paling banyak satu fase hijau; kuning nominal 3 detik dan merah bersama nominal 1 detik, dinilai terhadap toleransi terdokumentasi. | T+P — pin/catu daya dan toleransi timing mengikuti KT-04; nominal tidak berubah. | Rancangan M3; perakitan/uji dasar M5; uji M14. |
| KF-08 | OLED menampilkan fase, lampu, waktu, hitungan, kepadatan, kategori, dan mode. **Sumber:** Tabel 4.3; Subbab 4.5.1; SRS 7.1–7.2. | Ramdhani; Ikrom membandingkan tampilan dengan catatan. | Periksa OLED fisik dan cocokkan informasi dengan rencana serta status giliran aktif, termasuk data tidak tersedia. | UJI-01, UJI-20 | Seluruh informasi yang diwajibkan/satuan tersedia pada tata letak layar; fase/timer aktual sesuai perangkat; data terkait plan aktif benar; tidak tersedia dibedakan dari nol. | T — susunan tampilan diperinci saat rancangan/implementasi; tidak mengurangi isi wajib. | Dasar M5; integrasi M11; uji M14. |
| KF-09 | Pencatatan pengukuran, kategori, plan, ACK, mode, dan status. **Sumber:** Tabel 4.3; SRS 3.8 dan 8.1. | Ikrom untuk flow/data; Putu untuk layanan; pemilik modul untuk pesan. | Telusuri satu giliran dari pemicu ke InfluxDB; ganggu Node-RED/InfluxDB ketika jalur kendali tersedia. | UJI-21, UJI-23 | Catatan normal terhubung lewat ID/waktu dan versi parameter; ACK penerimaan dibedakan dari pelaksanaan; gangguan pencatatan tidak menghentikan urutan/pergantian lampu. | T+P — field/identitas dan lingkungan mengikuti KT-04/KT-05. | Integrasi M10–11; uji M14. |
| KF-10 | Statis cadangan lokal saat plan adaptif valid tidak tersedia pada lock. **Sumber:** Tabel 4.3; SRS 3.6. | Ramdhani untuk firmware; Putu untuk parameter/integrasi; Rizky untuk kegagalan sumber. | Uji frame gagal, plan setelah lock, server/jaringan gagal, serta pemulihan layanan pada perangkat yang tetap berfungsi dan mendapat daya. | UJI-08, UJI-17, UJI-18, UJI-19 | Statis lokal terverifikasi digunakan bila tidak ada kandidat sah pada lock; urutan/transisi tetap; plan baru setelah lock ditolak; adaptif pulih pada giliran sah berikutnya tanpa memotong fase aktif. | T+P — nilai statis dan pelaksanaannya mengikuti KT-03/KT-04. | Statis M9; integrasi M10; uji M14. |
| KF-11 | Validasi konfigurasi, frame, identitas, giliran, fase, durasi, dan duplikasi. **Sumber:** Tabel 4.3; SRS 3.6–3.7. | Rizky untuk frame/config AI; Putu untuk backend/pesan; Ramdhani untuk penerimaan/lock. | Berikan config/frame salah, payload rusak, sesi/giliran/fase salah, durasi di luar batas, pesan identik, dan rencana sebelum/sesudah lock. | UJI-03, UJI-08, UJI-14, UJI-15, UJI-16, UJI-17 | Masukan tidak sah ditolak dengan alasan; tidak mengubah kendali aktif. Duplikasi tidak mengulang inferensi/keputusan atau mereset timer. Keputusan/mode terkunci tetap dipertahankan. | T+P — aturan rinci mengikuti KT-02/KT-03/KT-04. | Rancangan M3; pengembangan M6–10; uji M14. |

### 3.2 Kebutuhan nonfungsional

| Kode | Kebutuhan dan sumber | PIC implementasi / penanggung jawab | Cara verifikasi | ID UJI terkait | Kriteria keberhasilan | Status penetapan dan tindak lanjut | Rencana waktu |
|---|---|---|---|---|---|---|---|
| KNF-01 | Target penerimaan rencana ≤3 detik sejak pemicu ESP32. **Sumber:** Tabel 4.5; Tabel 6.3; SRS 3.6 dan 4.2. | Ramdhani mengukur ujung-ke-ujung; Rizky/Putu waktu server; Ikrom merekap. | Catat t_kirim pemicu dan t_terima plan valid dengan jam lokal ESP32, termasuk beban gabungan dan plan terlambat sebelum lock. | UJI-13, UJI-16, UJI-24 | Selisih ≤3 detik memenuhi target. Tidak ada plan valid dalam batas tersebut tetap dicatat tidak memenuhi; keberhasilan statis/penanganan plan terlambat dinilai terpisah. | T — target ditetapkan; detail ukur/lingkungan dituntaskan melalui KT-04/KT-05. | Uji beban/respons M12; uji batas M14. |
| KNF-02 | Ambang umur frame dapat dikonfigurasi sesuai sumber. **Sumber:** Tabel 4.5; SRS 3.2 dan 8.2. | Rizky; Ikrom memeriksa metadata waktu. | Periksa asal timestamp dan ambang; uji frame gagal dekode, terlalu lama, atau dimensi tidak sesuai. | UJI-08 | Umur/validitas dinilai dengan dasar waktu terdokumentasi; frame tidak sah ditandai gagal/alasan, tidak menjadi nol. Timestamp penerimaan tidak dianggap otomatis waktu perekaman. | T+P — dasar waktu dan ambang per sumber mengikuti KT-02. | Penetapan sumber M6; uji M14. |
| KNF-03 | Evaluasi hitungan dan hasil kategori/layanan sesuai Bab 6. **Sumber:** Tabel 4.5; Tabel 6.3; SRS 4.2 dan 8.4. | Rizky untuk hitungan/kategori; Putu untuk durasi/cakupan; Ikrom untuk data/laporan. | Bandingkan manual dan AI pada frame/ROI sama; evaluasi kategori dengan ambang beku sama; nilai cakupan durasi akhir pada data uji terpisah. | UJI-06, UJI-31, UJI-34 | E_N ≤10% per kamera; MAE/jumlah frame dilaporkan. Akurasi/matriks kebingungan/jumlah sampel kategori dilaporkan tanpa ambang akurasi baru. Cakupan ≥90% per kamera/kategori; data tidak cukup dinyatakan. | T — metrik/target tetap; penerapan menunggu model/parameter beku KT-01/KT-03, serta penyelarasan KT-06/KT-08. | Evaluasi M13; pelengkapan verifikasi M14. |
| KNF-04 | Konsistensi giliran, lock, duplikasi, dan pemulihan. **Sumber:** Tabel 4.5; SRS 3.6–3.7. | Ramdhani; Putu pada identitas/rencana. | Amati urutan, kirim ulang plan, kirim plan baru setelah lock, dan pulihkan adaptif saat fase berjalan. | UJI-12, UJI-15, UJI-17, UJI-19 | Plan hanya berlaku untuk giliran sasaran; duplikasi tidak mereset waktu; keputusan terkunci tidak berubah; pemulihan tidak memotong fase aktif. | T+P — format sesi/giliran dan aturan kontrak mengikuti KT-04. | Integrasi M10; uji M14. |
| KNF-05 | Cadangan berjalan ketika ESP32 tetap berfungsi. **Sumber:** Tabel 4.5; SRS 3.6. | Ramdhani; Putu menangani gangguan server/MQTT. | Putuskan layanan/komunikasi secara terkontrol ketika ESP32 tetap hidup, kemudian amati lock dan keluaran. | UJI-18 | Bila plan valid belum tersedia pada lock, perangkat memakai statis lokal terverifikasi dan lampu berlanjut sesuai urutan/transisi. | T+P — durasi statis mengikuti KT-03; bukan jaminan operasi ketika ESP32/daya gagal. | Statis M9; integrasi M10; uji M14. |
| KNF-06 | Autentikasi/TLS dan pemisahan kredensial. **Sumber:** Tabel 4.5; SRS 7.3. | Putu untuk broker/server; Ramdhani untuk klien; semua pemilik berkas untuk rahasia. | Uji koneksi sah dan kredensial tidak sah; verifikasi TLS; periksa kode/contoh konfigurasi yang dibagikan. | UJI-25, UJI-26 | Koneksi sesuai konfigurasi diterima, kredensial tidak sah ditolak, TLS berfungsi; kredensial operasional terpisah dari berkas publik. | T — konfigurasi rinci dirancang M3 dan disiapkan M4 sesuai KT-04/KT-05. | Persiapan M4; integrasi M10; uji M14. |
| KNF-07 | Ketertelusuran pengukuran, rencana, ACK, pelaksanaan, dan sampel. **Sumber:** Tabel 4.5; SRS 3.7–3.8, 8.1 dan 8.3–8.4. | Ikrom untuk metadata/pencatatan; Rizky/Putu/Ramdhani untuk ID/waktu modul. | Telusuri identitas pesan, penolakan, versi parameter, pembagian sampel, waktu frame/awal hijau, dan kelompok awal lintas hijau. | UJI-14, UJI-21, UJI-29, UJI-32 | ID/waktu menghubungkan tahap tanpa menyamakan ACK dengan pelaksanaan; sampel/sumber/versi terlacak; hitungan frame dan kelompok awal terpisah; status belum pasti dipertahankan. | T+P+S — kontrak KT-04, metadata KT-02, dan penyelarasan prosedur KT-08. | Rancangan M3; data M6–8; integrasi M10–11; uji M13–14. |
| KNF-08 | Data dan konfigurasi penting tersimpan persisten. **Sumber:** Tabel 4.5; SRS 3.8 dan 5.2–5.3. | Putu untuk volume/layanan; Ikrom untuk penulisan dan pemeriksaan data. | Tulis data, jalankan ulang layanan penyimpanan, lalu baca kembali data/config penting. | UJI-22 | Data dan konfigurasi penting tetap tersedia pada penyimpanan persisten sesuai rancangan. | T — lokasi/volume aktual dicatat saat penyiapan KT-05. | Persiapan M4; integrasi M11; uji M14. |
| KNF-09 | Evaluasi CPU, RAM, GPU, dan penyimpanan pada beban gabungan. **Sumber:** Tabel 4.5–4.7; SRS 4.2 dan 5.2–5.3. | Rizky/Putu menyiapkan beban; Ikrom mencatat; Nicy menilai kecukupan. | Jalankan tiga pembaca CCTV, YOLO, backend, Mosquitto, Node-RED, dan InfluxDB bersama; catat sumber daya, lingkungan, dan respons ESP32. | UJI-24 | CPU/RAM/GPU/penyimpanan serta kondisi beban tercatat; respons dinilai terhadap 3 detik dan kecukupan server dijelaskan. Tidak menetapkan persentase pemakaian baru; uji CPU saja belum membuktikan target server GPU. | T — spesifikasi awal diketahui; kondisi aktual/kecukupan mengikuti KT-01/KT-05. | Persiapan M4; uji gabungan M12. |
| KNF-10 | Versi model, dependensi, layanan, konfigurasi, dan parameter tercatat. **Sumber:** Tabel 4.5; SRS 5.3 dan 8.4. | Rizky untuk AI; Putu untuk server/parameter; Ramdhani untuk firmware; Ikrom mengindeks. | Audit manifest/panduan, identitas sampel, dataset K-means, versi parameter, dan pembekuan sebelum evaluasi. | UJI-27, UJI-29, UJI-30 | Versi/asal parameter sesuai implementasi dan dapat ditelusuri; data uji bukan sumber tuning versi yang dinilai; pembekuan tercatat sebelum evaluasi. | T — isi versi diisi dari implementasi, bukan angka perkiraan; terkait KT-01/KT-03/KT-05. | Versi M4–9; beku sebelum evaluasi M13; audit akhir M16. |
| KNF-11 | Gangguan pencatatan tidak menghambat pengendalian. **Sumber:** Tabel 4.5; SRS 3.8. | Ikrom untuk pencatatan; Putu/Ramdhani untuk pemisahan jalur kendali. | Hentikan Node-RED/InfluxDB ketika jalur pengendalian tetap tersedia; amati beberapa pergantian lampu. | UJI-23 | Urutan dan pergantian lampu tetap berjalan; dampak hilangnya pencatatan dilaporkan tersendiri. | T — independensi jalur diwujudkan pada rancangan/integrasi. | Integrasi M11; uji M14. |
| KNF-12 | Dokumentasi konfigurasi, instalasi, operasi, integrasi, dan pengujian. **Sumber:** Tabel 4.5; SRS 8.3–8.4 dan 10. | Setiap pemilik modul menulis bagian teknis; Ikrom menggabungkan; Nicy memeriksa. | Audit versi/panduan/paket serah terima; periksa catatan sampel, prosedur layanan, P90, dan evaluasi cakupan. | UJI-27, UJI-28, UJI-29, UJI-32, UJI-33, UJI-34 | Dokumen sesuai versi akhir, menjelaskan asal parameter, pemisahan data, hasil/keterbatasan, dan layanan 12 bulan. Prosedur tidak mengubah status belum pasti menjadi selesai. | T+S — judul/prosedur dan rujukan naskah diselaraskan melalui KT-07/KT-08 serta Bagian 6.2. | Rancangan M3; pembaruan tiap tahap; paket akhir M16. |

### 3.3 Kebutuhan waktu, jasa, dan maintenance

UJI-28 memeriksa kelengkapan serah terima dan **kesiapan dokumen** layanan. Pencapaian 12 bulan layanan, respons gangguan, jam aktual, dan laporan bulanan harus dinilai dari pelaksanaan sesudah penyerahan. Tanda **—** berarti tidak ada ID UJI khusus pada Tabel 6.2; cara review pada baris tersebut tetap wajib direncanakan.

| Kode | Kebutuhan dan sumber | PIC implementasi / penanggung jawab | Cara verifikasi | ID UJI terkait | Kriteria keberhasilan | Status penetapan dan tindak lanjut | Rencana waktu |
|---|---|---|---|---|---|---|---|
| KJ-01 | Pengembangan 16 minggu dengan alokasi 958 jam-orang. **Sumber:** Tabel 4.8; Bab 2; SRS 6.1–6.2. | Nicy mengoordinasikan; anggota mencatat kegiatan; Ikrom membantu rekap. | Review jadwal dan alokasi, bandingkan dengan log/progres aktual sepanjang sprint. | —; review administrasi/layanan. | Rencana 16 minggu/958 jam-orang tertelusur ke pekerjaan; realisasi, kendala, dan perubahan alokasi dicatat. Alokasi bukan klaim jam aktual yang sudah dihabiskan. | T — jadwal/alokasi ditetapkan; aktual dicatat saat pelaksanaan. | M1–16; review administrasi per minggu. |
| KJ-02 | Analisis sampai dokumentasi sebagai cakupan jasa teknis. **Sumber:** Tabel 4.8; Bab 2; SRS 6.1. | Nicy mengoordinasikan; semua anggota melaksanakan modulnya. | Review pembagian tugas, hasil, commit/bukti, temuan, serta kelengkapan tahap analisis, rancangan, pengembangan, perakitan, integrasi, uji, perbaikan, dan dokumentasi. | —; review administrasi/layanan. | Setiap tahap mempunyai PIC dan hasil yang diperiksa; pekerjaan belum selesai/temuan tetap tercatat dengan tindak lanjut. | T — cakupan ditetapkan; mengikuti Kanban/pembagian kerja. | M1–16; review akhir M16. |
| KJ-03 | Serah terima prototipe, kode, konfigurasi, panduan, dan laporan pengujian. **Sumber:** Tabel 4.8; SRS 6.1. | Nicy untuk pemeriksaan/penyerahan; Ikrom untuk indeks; pemilik modul untuk isi. | Periksa paket, demonstrasi, versi, laporan, dan berita acara saat serah terima berlangsung. | UJI-28 | Seluruh hasil wajib tersedia dan sesuai versi yang diuji; penyerahan/penerimaan yang benar-benar terjadi dicatat pada berita acara. | T — daftar hasil ditetapkan; penerimaan belum dilaksanakan pada dokumen rencana. | M16. |
| KJ-04 | Satu paket maintenance 12 bulan setelah serah terima. **Sumber:** Tabel 4.8; Bab 2; SRS 6.1 dan 6.3. | Nicy mengoordinasikan; pemilik modul menangani teknis; Ikrom melaporkan. | UJI-28 memeriksa kesiapan dokumen layanan; setelah serah terima, review tanggal mulai/akhir dan realisasi layanan sepanjang periode. | UJI-28 (kesiapan dokumen); review realisasi layanan. | Dokumen menjelaskan 12 bulan sesudah tanggal serah terima aktual; pelaksanaan dinilai dari catatan layanan, bukan hanya ketersediaan panduan. | T — periode ditetapkan; tanggal aktual mengikuti serah terima. | Kesiapan M16; pelaksanaan 12 bulan setelah penyerahan. |
| KJ-05 | Alokasi preventif/administrasi 12 jam-orang per bulan. **Sumber:** Tabel 4.8; SRS 6.3. | Nicy mengatur alokasi; pemilik modul memeriksa; Ikrom merekap. | Review rencana pemeriksaan dan alokasi bulanan; cocokkan log aktual tanggal, pelaksana, kegiatan, waktu, temuan, serta tindak lanjut. | —; review administrasi/layanan. | Alokasi gabungan 12 jam-orang/bulan tercantum; realisasi dilaporkan berdasarkan kegiatan nyata berikut perbedaan dari rencana. | T — alokasi ditetapkan; pembagian bulanan dirinci pada panduan. | Disiapkan M16; verifikasi bulanan selama maintenance. |
| KJ-06 | Alokasi korektif 8 jam-orang per bulan untuk seluruh tim. **Sumber:** Tabel 4.8; SRS 6.3. | Pemilik modul memperbaiki; Nicy mengoordinasikan alokasi; Ikrom mencatat. | Review alokasi gabungan dan, bila ada gangguan, log diagnosis, perbaikan, waktu, serta hasil verifikasi. | —; review administrasi/layanan. | Alokasi 8 jam-orang/bulan berlaku untuk seluruh tim, bukan per anggota; digunakan sesuai gangguan. Tidak wajib menghabiskan alokasi atau membuat kasus gangguan. | T — alokasi ditetapkan; penggunaan mengikuti kejadian. | Disiapkan M16; dinilai bila ada gangguan selama maintenance. |
| KJ-07 | Respons awal maksimal satu hari kerja; estimasi penyelesaian sesudah diagnosis. **Sumber:** Tabel 4.8; SRS 6.3. | Nicy mengoordinasikan respons; PIC modul mendiagnosis; Ikrom mencatat waktu. | Periksa prosedur penerimaan gangguan dan bandingkan waktu laporan–respons pada kasus nyata menurut hari kerja yang didokumentasikan. | —; review administrasi/layanan. | Respons awal ≤1 hari kerja; perkiraan penyelesaian diberikan setelah diagnosis. Respons awal tidak disamakan dengan tenggat perbaikan selesai. | T — target ditetapkan; mekanisme/hari kerja dijelaskan pada panduan layanan. | Disiapkan M16; verifikasi pada laporan gangguan aktual. |
| KJ-08 | Laporan bulanan pemeriksaan, temuan, tindakan, jam, dan hasil perbaikan. **Sumber:** Tabel 4.8; SRS 6.3. | Ikrom menyusun; pemilik modul memberi data; Nicy memeriksa. | UJI-28 memeriksa dokumen/format siap pakai; setelah serah terima, review laporan tiap bulan dengan log sumbernya. | UJI-28 (kesiapan dokumen); review realisasi layanan. | Format tersedia saat penyerahan; laporan aktual bulanan memuat seluruh unsur dan sesuai log, termasuk bulan tanpa gangguan. Kesiapan format tidak membuktikan 12 laporan telah terbit. | T — isi laporan ditetapkan; laporan aktual belum jatuh tempo. | Format M16; laporan bulanan selama 12 bulan layanan. |
| KJ-09 | Pekerjaan di luar cakupan/alokasi korektif memerlukan estimasi dan kesepakatan tambahan. **Sumber:** Tabel 4.8; SRS 6.3. | Nicy mengoordinasikan; pemilik modul menyiapkan estimasi. | Review aturan pada panduan; jika ada permintaan tambahan, periksa scope, estimasi, dan catatan kesepakatan sebelum pelaksanaan pekerjaan tambahan tersebut. | —; review administrasi/layanan. | Pekerjaan tambahan dan dasar kesepakatannya terdokumentasi; bila belum ada kasus, verifikasi aturan dan catat belum ada realisasi. | T — ketentuan layanan ditetapkan; berlaku hanya jika ada pekerjaan tambahan. | Aturan M16; review saat permintaan aktual. |
| KJ-10 | Hardware pengganti, server, listrik, dan internet di luar paket maintenance. **Sumber:** Tabel 4.8; Bab 2; SRS 6.3. | Nicy memeriksa lingkup biaya; pemilik modul memberi kebutuhan. | Cocokkan ketentuan paket dengan RAB/proposal serta panduan; jika ada pengeluaran, periksa pencatatan terpisah sesuai jenis biaya. | —; review administrasi/layanan. | Empat kelompok biaya dinyatakan terpisah dari paket maintenance; biaya aktual hanya dicatat bila terjadi dan tidak dinyatakan termasuk tanpa dasar perubahan kesepakatan. | T — batas biaya ditetapkan; tidak mengarang nilai pengeluaran. | Review dokumen M16; pemeriksaan ketika biaya terjadi. |

## 4. Indeks kasus uji dari proposal

Daftar berikut membantu memeriksa hubungan dua arah: dari kebutuhan ke kasus pada Bagian 3, dan dari kasus ke kebutuhan pada bagian ini. Ringkasan bukan pengganti langkah uji terperinci pada `KELOMPOK-10/docs/pengujian/rencana-uji.md`, yang disusun pada minggu 3. PIC merupakan pembagian pelaksanaan tim; kode kebutuhan terkait mengikuti tabel sumber.

| ID UJI | Kebutuhan terkait pada Tabel 6.2 | Fokus pemeriksaan | Pelaksana sesuai modul |
|---|---|---|---|
| UJI-01 | KF-07, KF-08 | Sambungan, catu daya, GPIO, LED, resistor, dan OLED. | Ramdhani; Ikrom mencatat bukti. |
| UJI-02 | KF-01, KF-02 | Pembacaan tiga CCTV dan pemetaan fase virtual. | Rizky; Ikrom memeriksa metadata. |
| UJI-03 | KF-02, KF-05, KF-11 | Validasi ROI, panjang, lajur, dan konfigurasi pengendalian. | Rizky/Putu sesuai konfigurasi. |
| UJI-04 | KF-03, KF-06 | Pemicu pada sisa hijau satu detik untuk kamera fase berikutnya. | Ramdhani/Rizky/Putu pada jalurnya. |
| UJI-05 | KF-02, KF-03 | Titik acuan di dalam, pada batas, dan di luar ROI. | Rizky. |
| UJI-06 | KF-03, KF-04, KNF-03 | MAE dan E_N hitungan pada frame uji yang sama, per kamera. | Rizky; Ikrom menyediakan acuan manual. |
| UJI-07 | KF-03, KF-04, KF-05 | Frame valid tanpa kendaraan: nol sah, kategori, dan durasi. | Rizky/Putu. |
| UJI-08 | KF-01, KF-10, KF-11, KNF-02 | Frame gagal/tua/tidak sesuai dan statis saat lock bila plan valid tidak ada. | Rizky; Putu/Ramdhani untuk dampak pengendalian. |
| UJI-09 | KF-04 | Rumus kepadatan dan satuan dari N, panjang, serta lajur. | Rizky. |
| UJI-10 | KF-05 | Batas kategori di sekitar dan tepat pada K1/K2. | Putu. |
| UJI-11 | KF-05 | Waktu dasar, tambahan kategori, dan batas minimum–maksimum. | Putu. |
| UJI-12 | KF-07, KNF-04 | Urutan A–B–C–A, kuning, merah bersama, dan maksimal satu hijau. | Ramdhani; Ikrom merekam. |
| UJI-13 | KF-06, KNF-01 | Respons dari pemicu dikirim sampai plan valid diterima ESP32. | Ramdhani mengukur; Rizky/Putu menelusuri tahap server. |
| UJI-14 | KF-11, KNF-07 | Pesan rusak, identitas/fase salah, dan durasi tidak sah. | Putu/Ramdhani pada penerima pesan terkait. |
| UJI-15 | KF-06, KF-11, KNF-04 | Pemicu/rencana identik dikirim ulang. | Rizky/Putu/Ramdhani pada modulnya. |
| UJI-16 | KF-06, KF-11, KNF-01 | Rencana valid sesudah tiga detik tetapi sebelum lock. | Putu/Ramdhani; Ikrom memisahkan penilaian fungsi dan respons. |
| UJI-17 | KF-10, KF-11, KNF-04 | Rencana baru setelah lock ditolak untuk giliran terkunci. | Ramdhani; Putu memasok pesan uji. |
| UJI-18 | KF-10, KNF-05 | Gangguan server/komunikasi ketika ESP32 tetap berfungsi. | Putu/Ramdhani. |
| UJI-19 | KF-10, KNF-04 | Pemulihan adaptif pada giliran berikutnya yang memenuhi syarat. | Putu/Ramdhani. |
| UJI-20 | KF-08 | OLED dibandingkan dengan rencana dan status giliran aktif. | Ramdhani; Ikrom memeriksa bukti. |
| UJI-21 | KF-09, KNF-07 | Keterhubungan pemicu, pengukuran, versi, rencana, ACK, dan pelaksanaan. | Ikrom; Rizky/Putu/Ramdhani menyediakan peristiwa modul. |
| UJI-22 | KNF-08 | Data/config tetap tersedia setelah layanan penyimpanan diulang. | Ikrom; Putu menangani volume/layanan. |
| UJI-23 | KF-09, KNF-11 | Lampu tetap berjalan saat pencatatan dihentikan dan jalur kendali tersedia. | Ikrom/Putu/Ramdhani. |
| UJI-24 | KNF-01, KNF-09 | Beban tiga pembaca CCTV, AI, backend, dan layanan bersama. | Rizky/Putu; Ramdhani mengukur respons; Ikrom merekap. |
| UJI-25 | KNF-06 | Koneksi sah/tidak sah serta TLS. | Putu; Ramdhani memeriksa klien ESP32. |
| UJI-26 | KNF-06 | Pemisahan kredensial dari kode dan konfigurasi publik. | Putu dan pemilik berkas terkait; Nicy memeriksa. |
| UJI-27 | KNF-10, KNF-12 | Versi model, dependensi, config, parameter, dan panduan. | Pemilik modul; Ikrom menggabungkan; Nicy memeriksa. |
| UJI-28 | KNF-12, KJ-03, KJ-04, KJ-08 | Kelengkapan serah terima dan dokumen layanan 12 bulan. | Nicy/Ikrom; materi teknis dari pemilik modul. |
| UJI-29 | KNF-07, KNF-10, KNF-12 | Identitas sampel, pemisahan kalibrasi/uji, dan versi parameter. | Ikrom; Rizky/Putu memeriksa penggunaan dataset. |
| UJI-30 | KF-05, KNF-10 | Tiga kelompok K-means manual per kamera dan titik tengah K1/K2. | Putu; Rizky/Ikrom memeriksa data. |
| UJI-31 | KF-04, KF-05, KNF-03 | Kategori AI versus acuan manual dengan ambang beku yang sama. | Rizky/Putu; Ikrom merekap. |
| UJI-32 | KF-05, KNF-07, KNF-12 | Waktu frame, awal hijau, kelompok awal, lintas hijau, dan status pengamatan. | Ikrom/Rizky/Putu sesuai bagian pengamatan. |
| UJI-33 | KF-05, KNF-12 | P90 waktu lengkap dan penanganan penyelesaian belum pasti. | Putu; Ikrom memeriksa data/status. |
| UJI-34 | KF-05, KNF-03, KNF-12 | Cakupan layanan pada durasi akhir per kamera/kategori; kalibrasi dan uji terpisah. | Putu; Ikrom merekap; Nicy memeriksa. |

## 5. Rencana penempatan hasil dan bukti

Semua path di bawah adalah tujuan pengumpulan, **bukan pernyataan bahwa berkas/bukti sudah tersedia**. Lokasi mengikuti Kanban dan pembagian pekerjaan. Kode, konfigurasi, data, dan laporan harus menunjukkan versi yang sama dengan kasus yang dinilai. Bukti awal pada sprint implementasi tetap dipertahankan; evaluasi akhir mengacu pada versi dan kondisi yang dicatat saat pengujian.

### 5.1 Bukti teknis

| Kebutuhan / kelompok uji | Path lengkap | Isi yang disimpan dan PIC |
|---|---|---|
| KF-01–KF-02, KNF-02; UJI-02–UJI-03, UJI-08 | `KELOMPOK-10/docs/operasional/konfigurasi-kamera.md`; `KELOMPOK-10/configs/cameras.example.json`; `KELOMPOK-10/data/metadata/sumber-rekaman.csv`; `KELOMPOK-10/evidence/S04/pemeriksaan-sumber.csv` | Rizky: dasar sumber/ROI, panjang/lajur, dimensi/timestamp, dan hasil pembacaan. Ikrom: metadata/bukti sumber. Config contoh tidak menggantikan pencatatan config aktual yang diuji. |
| KF-03–KF-04, KNF-03; UJI-05–UJI-09 | `KELOMPOK-10/ai/`; `KELOMPOK-10/models/manifest.csv`; `KELOMPOK-10/evidence/S04/perbandingan-manual.csv`; `KELOMPOK-10/evidence/S04/pemeriksaan-kepadatan.csv` | Rizky: kode/manifest dan hasil perhitungan; Ikrom: identitas frame serta hitungan pembanding manual. |
| KF-05, KNF-10; UJI-10–UJI-11, UJI-30, UJI-32–UJI-34 | `KELOMPOK-10/data/kalibrasi/observasi.csv`; `KELOMPOK-10/backend/kalibrasi/`; `KELOMPOK-10/configs/control.json`; `KELOMPOK-10/docs/kalibrasi/hasil-kalibrasi.md`; `KELOMPOK-10/evidence/S04/pemeriksaan-aturan.csv` | Putu: pengaturan K-means, pusat/anggota, K1/K2, durasi/cakupan akhir, versi dan batas; Rizky/Ikrom: data serta acuan manual. |
| KNF-07, KNF-10, KNF-12; UJI-29, UJI-32 | `KELOMPOK-10/docs/perencanaan/prosedur-ai-dan-pengamatan.md`; `KELOMPOK-10/data/metadata/pembagian-sampel.csv`; `KELOMPOK-10/data/kalibrasi/README.md`; `KELOMPOK-10/data/uji/README.md` | Rizky/Ikrom: prosedur, identitas, hari/periode, kelompok awal, status penyelesaian, dan pembagian sampel. Putu: hubungan versi parameter dengan dataset. |
| KF-03–KF-05, KNF-03; UJI-06, UJI-31, UJI-34 | `KELOMPOK-10/data/uji/observasi.csv`; `KELOMPOK-10/tests/evaluation/`; `KELOMPOK-10/evidence/S06/evaluasi-sampel.csv`; `KELOMPOK-10/docs/pengujian/evaluasi-data-uji.md` | Rizky/Putu: perhitungan evaluasi; Ikrom: data, rekap, serta laporan per kamera/kategori dan keterbatasannya. |
| KF-06, KF-11, KNF-04, KNF-07; UJI-04, UJI-14–UJI-17, UJI-21 | `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md`; `KELOMPOK-10/configs/mqtt/`; `KELOMPOK-10/evidence/S05/mqtt-pemicu-rencana.txt`; `KELOMPOK-10/docs/pengujian/integrasi-mqtt.md` | Putu: kontrak dan integrasi; Ramdhani: penerimaan/lock; Rizky: pemrosesan pengukuran; Ikrom: pesan aktual, ID, dan urutan peristiwa. |
| KF-07–KF-08; UJI-01, UJI-12, UJI-20 | `KELOMPOK-10/docs/perangkat/perakitan.md`; `KELOMPOK-10/firmware/esp32/`; `KELOMPOK-10/evidence/S03/pemeriksaan-dasar.csv`; `KELOMPOK-10/evidence/S05/oled-status.jpg` | Ramdhani: rangkaian, pin, firmware dan tampilan; Ikrom: hasil pemeriksaan dasar serta pencocokan dengan status. |
| KF-09, KNF-07–KNF-08, KNF-11; UJI-21–UJI-23 | `KELOMPOK-10/backend/node-red/flow.json`; `KELOMPOK-10/infra/compose.yaml`; `KELOMPOK-10/evidence/S05/pemeriksaan-pencatatan.csv`; `KELOMPOK-10/docs/pengujian/pencatatan-data.md` | Ikrom: flow, contoh data, dan hasil persistensi/gangguan; Putu: layanan/volume; Ramdhani: bukti kelangsungan lampu. |
| KNF-01, KNF-09; UJI-13, UJI-24 | `KELOMPOK-10/evidence/S06/waktu-ai.csv`; `KELOMPOK-10/evidence/S06/waktu-backend.csv`; `KELOMPOK-10/evidence/S06/respons-esp32.csv`; `KELOMPOK-10/evidence/S06/sumber-daya.csv`; `KELOMPOK-10/docs/pengujian/hasil-beban-respons.md` | Rizky/Putu/Ramdhani: waktu tahap dan ujung-ke-ujung; Ikrom: sumber daya, rekap, dan analisis beban gabungan. |
| KF-01, KF-11, KNF-02; UJI-07–UJI-08 | `KELOMPOK-10/evidence/S06/kasus-ai.csv` | Rizky: membedakan frame valid nol kendaraan dari pengukuran gagal beserta alasan. Penilaian lanjutan kategori/durasi/cadangan dihubungkan ke bukti modul terkait. |
| KF-06, KF-11, KNF-06; UJI-14–UJI-16, UJI-25–UJI-26 | `KELOMPOK-10/evidence/S06/kasus-mqtt.csv`; `KELOMPOK-10/tests/integration/` | Putu: pesan normal/tidak sah/duplikat/terlambat, hasil autentikasi/TLS, dan pemeriksaan pemisahan rahasia. Bukti publik tidak memuat kredensial operasional. |
| KF-07, KF-10–KF-11, KNF-04–KNF-05; UJI-12, UJI-15–UJI-19 | `KELOMPOK-10/evidence/S06/kasus-esp32.csv`; `KELOMPOK-10/evidence/S06/fallback-pemulihan.mp4` | Ramdhani: hasil timing, duplikasi, lock, statis, serta pemulihan pada perangkat aktual. |
| KF-08–KF-09, KNF-08, KNF-11; UJI-20, UJI-22–UJI-23 | `KELOMPOK-10/evidence/S06/kasus-pencatatan-oled.csv` | Ikrom bersama Ramdhani/Putu: pencocokan OLED, persistensi, serta kelangsungan lampu saat pencatatan terganggu. |
| Seluruh kasus UJI-01–UJI-34 | `KELOMPOK-10/docs/pengujian/rencana-uji.md`; `KELOMPOK-10/evidence/S06/rekap-kasus-uji.csv` | Ikrom mengelola rencana dan rekap: ID, versi, hasil harapan/aktual, bukti, status, dampak, PIC temuan. Pengujian yang dilakukan lebih awal ditautkan ke bukti sprint asal. |
| Temuan pengujian yang diperbaiki | `KELOMPOK-10/evidence/S07/verifikasi-perbaikan.csv`; `KELOMPOK-10/docs/pengujian/perbaikan-dan-uji-ulang.md` | Pemilik modul: perubahan dan uji ulang; Ikrom: rekap; Nicy: review penyelesaian dan keterbatasan tersisa. |
| KNF-10, KNF-12; UJI-27–UJI-28 | `KELOMPOK-10/docs/serah-terima/panduan-instalasi.md`; `KELOMPOK-10/docs/serah-terima/panduan-operasi.md`; `KELOMPOK-10/docs/serah-terima/penanganan-gangguan.md`; `KELOMPOK-10/docs/serah-terima/paket-serah-terima.md` | Pemilik modul: materi teknis; Ikrom: panduan/indeks gabungan; Nicy: pemeriksaan kesesuaian versi akhir. |

### 5.2 Bukti jasa dan layanan

| Kebutuhan | Path lengkap | Bentuk pemeriksaan |
|---|---|---|
| KJ-01–KJ-02 | `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md`; `KELOMPOK-10/evidence/S01/README.md`; `KELOMPOK-10/evidence/S01/log-aktivitas.md` | Nicy memeriksa rencana/alokasi dan progres minggu 1–3. Minggu berikutnya memakai README/log sprint masing-masing pada path lengkap yang tercantum dalam Kanban. |
| KJ-03; UJI-28 | `KELOMPOK-10/docs/serah-terima/paket-serah-terima.md`; `KELOMPOK-10/docs/serah-terima/berita-acara.md`; `KELOMPOK-10/docs/laporan/laporan-akhir.docx` | Nicy/Ikrom memeriksa kelengkapan paket dan versi; tanggal serta hasil penerimaan diisi ketika penyerahan berlangsung. |
| KJ-04–KJ-10 | `KELOMPOK-10/docs/serah-terima/panduan-maintenance.md`; `KELOMPOK-10/docs/serah-terima/template-log-maintenance.csv` | Ikrom menyusun format dari masukan teknis anggota; Nicy memeriksa cakupan, periode, alokasi, respons, laporan, tambahan, dan biaya terpisah. Lokasi arsip laporan/log layanan aktual ditetapkan dalam panduan sebelum layanan berjalan. |

### 5.3 Pemeriksaan sumber daya dan antarmuka pendukung

Kelompok ini menelusuri rincian SRS yang mendukung KF/KNF tanpa memberi kode kebutuhan baru.

| Kelompok dan sumber | Cara pemeriksaan / kasus terkait | PIC dan lokasi utama |
|---|---|---|
| Hardware — SRS 5.1; Tabel 4.9 | Cocokkan inventaris dan rangkaian: satu ESP32-DevKitC V4/WROOM-32D, sembilan LED/resistor, OLED SSD1306 I²C, breadboard/jumper, USB data, dan adaptor sesuai rincian SRS. UJI-01 memeriksa sambungan, catu daya, dan keluaran. | Ramdhani; `KELOMPOK-10/docs/perangkat/inventaris.md`; `KELOMPOK-10/docs/perangkat/perakitan.md`. |
| Server — SRS 5.2; Tabel 4.6 | Bandingkan lingkungan aktual dengan acuan satu server Ubuntu 24.04 LTS, setara 4 vCPU/16 GiB RAM, GPU NVIDIA T4 16 GB atau sebanding/CUDA, dan SSD persisten minimum 100 GB. Kecukupan diuji pada UJI-24 bersama UJI-13; perbedaan lingkungan dicatat. | Putu/Rizky; `KELOMPOK-10/infra/lingkungan-server.md`; `KELOMPOK-10/infra/lingkungan-ai.md`; `KELOMPOK-10/evidence/S06/kondisi-pengujian.md`. |
| Penempatan software — SRS 5.3; Tabel 4.7 | AI/backend pada host Ubuntu; Mosquitto/Node-RED/InfluxDB pada Docker di server yang sama; firmware pada ESP32. Catat versi dan periksa operasi bersama melalui UJI-24/UJI-27. | Putu/Rizky/Ramdhani; `KELOMPOK-10/infra/compose.yaml`; `KELOMPOK-10/models/manifest.csv`; `KELOMPOK-10/firmware/esp32/`. |
| Antarmuka/data — SRS 7–8; Subbab 4.5 dan Tabel 4.10 | Periksa koneksi fisik/OLED, JSON/identitas dan waktu, MQTT QoS 1 untuk plan/ACK, plan retain false, TLS, serta keterlacakan konfigurasi/data; didukung UJI-01/UJI-14–UJI-15/UJI-20–UJI-21/UJI-25/UJI-27/UJI-29. Pemeriksaan rinci dimasukkan pada langkah kasus terkait tanpa membuat nomor UJI baru. | Pemilik modul sesuai antarmuka; `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md`; `KELOMPOK-10/configs/mqtt/`; `KELOMPOK-10/docs/perangkat/perakitan.md`. |

## 6. Parameter, keputusan terbuka, dan penyelarasan

### 6.1 Tindak lanjut KT dari SRS

Seluruh KT di bawah masih dicatat sebagai tindak lanjut terbuka pada draf ini. Penetapan aktual harus mempunyai dasar, tanggal, versi, dan lokasi hasil; tidak diisi dengan nilai perkiraan seolah-olah sudah dikalibrasi.

| ID | Hal yang perlu diselesaikan | Kebutuhan terdampak | PIC | Waktu dan hasil yang ditunggu |
|---|---|---|---|---|
| KT-01 | Pilih varian/bobot YOLO, input, confidence, NMS, pustaka, dan komputasi. | KF-03; KNF-01, KNF-03, KNF-09–KNF-10. | Rizky; Nicy memeriksa lingkup. | Saat implementasi AI, dicatat sebelum evaluasi akhir pada manifest/lingkungan dan bukti evaluasi. |
| KT-02 | Tetapkan sumber/fase, ROI, panjang, lajur, dimensi/FPS/format, timestamp, dasar umur frame, dan ambang validitas. | KF-01–KF-04, KF-11; KNF-02, KNF-07. | Rizky; Ikrom untuk metadata. | Pemeriksaan sumber M6; rincian harus siap sebelum uji terkait. Hasil pada konfigurasi kamera dan metadata. |
| KT-03 | Lengkapi data/pengaturan K-means, K1/K2, durasi kategori, batas, serta statis lokal terverifikasi. | KF-05, KF-10–KF-11; KNF-03, KNF-05, KNF-10. | Putu; Rizky/Ikrom untuk data; Ramdhani untuk statis aktual. | Kalibrasi M8–9; bekukan sebelum evaluasi terpisah. Hasil pada config, laporan kalibrasi, dan pemeriksaan statis. |
| KT-04 | Rinci pin/catu daya, topic/field/identitas, lock, dan toleransi pengukuran timing. | KF-06–KF-11; KNF-01, KNF-04, KNF-06–KNF-07. | Ramdhani/Putu sesuai modul; Ikrom menyiapkan verifikasi. | Rancangan M3 dan penyelesaian implementasi; toleransi harus ditetapkan sebelum uji timing, bukan disesuaikan agar hasil lulus. |
| KT-05 | Catat penempatan server, versi lingkungan, jaringan, ketersediaan komponen, serta kecukupan kapasitas. | KNF-01, KNF-08–KNF-10; sumber daya pendukung KF. | Putu/Rizky/Ramdhani sesuai komponen; Nicy mengoordinasikan. | Persiapan M4 dan beban/integrasi M10–12. Hasil pada inventaris, lingkungan aktual, dan laporan beban. |
| KT-06 | Selaraskan pembanding detektor: Subbab 2.1/4.1.2/BMC menyebut sekurangnya satu non-YOLO pada frame/perangkat sama; Tabel 1.3/Subbab 6.1 menempatkannya sebagai kajian literatur dengan implementasi YOLO. | Lingkup KF-03 dan evaluasi KNF-03/KNF-09; belum menjadi kasus uji wajib tambahan. | Nicy bersama Rizky/tim. | Pemeriksaan kebutuhan sebelum lingkup evaluasi difinalkan; catat keputusan dan perbarui dokumen terkait. |
| KT-07 | Seragamkan judul sampul dengan Subbab 4.1.1. | Identitas SRS, matriks, dan dokumen akhir. | Nicy. | Pemeriksaan naskah; judul draf tetap mengikuti sampul sempro. |
| KT-08 | Lengkapi instruksi editorial tersisa pada Subbab 5.3; selaraskan jumlah kendaraan frame dengan kelompok awal pada Subbab 4.6. | KF-05; KNF-03, KNF-07, KNF-12; UJI-32–UJI-34. | Nicy bersama Putu/Rizky/Ikrom. | Sebelum prosedur/kalibrasi dibekukan; tulis aturan ketidakpastian, layanan lintas hijau, serta dampak pembatasan durasi secara lengkap. |

### 6.2 Catatan rujukan persamaan

Pada UJI-11, tabel sumber masih merujuk Persamaan (4.3)/(4.4) untuk durasi/pembatasan, sedangkan bagian kebutuhan terbaru menggunakan nomor tersebut untuk K1/K2 dan menuliskan durasi/pembatasan pada (4.5)/(4.6). Beberapa label persamaan pada Subbab 6.4 juga belum seragam dengan nomor yang disebut dalam paragraf.

**Tindak lanjut Nicy:** selaraskan nomor rujukan saat pemeriksaan naskah. Untuk perancangan uji, gunakan nama dan substansi perhitungan pada SRS: titik tengah pusat untuk K1/K2, waktu dasar ditambah tambahan kategori, pembatasan minimum–maksimum, MAE/E_N, akurasi kategori, serta cakupan layanan. Catatan ini tidak mengubah nomor kasus atau menambah target kuantitatif.

## 7. Aturan penilaian agar hasil tidak salah disimpulkan

1. **Hitungan dan kategori.** Bandingkan AI/manual pada frame serta ROI yang sama. Hitung kesalahan absolut tiap frame sebelum penjumlahan. Laporkan E_N dan MAE per kamera; jika total manual nol, E_N tidak dihitung dan hasil diperiksa dengan MAE/kesesuaian nol. Tanpa frame yang dapat dibandingkan, metrik belum dapat dihitung. Akurasi kategori/matriks kebingungan dilaporkan tanpa menetapkan ambang kelulusan baru yang tidak ada pada proposal.
2. **Kalibrasi dan data uji.** Rencana 15 kalibrasi + 15 uji per CCTV berarti 45 + 45 siklus untuk tiga kamera. Setiap kelompok per kamera mencakup lima pagi, lima siang, lima sore, dengan hari uji berbeda dari kalibrasi. Kecukupan kategori diperiksa; jumlah rencana tidak menjamin semua kategori terwakili. Jumlah siklus pengamatan berbeda dari jumlah kasus UJI.
3. **Waktu layanan.** Frame kepadatan sekitar lima detik sebelum hijau aktual dan kelompok yang sudah mengantre saat hijau dimulai dicatat terpisah. Untuk kelompok yang masih terlacak lintas giliran, hanya waktu hijau dijumlahkan. P90 nearest-rank berlaku ketika waktu layanan lengkap, dengan pembulatan kandidat detik penuh sesuai prosedur proposal. Sampel belum pasti tetap masuk penyebut cakupan dan tidak dinyatakan berhasil. Nilai cakupan ≥90% diperiksa pada durasi akhir sesudah pengurutan dan pembatasan.
4. **Keterwakilan.** Kategori tanpa sampel tidak dinyatakan lulus atau memiliki cakupan 100%; nyatakan belum teruji/belum dapat dinilai. Pisahkan hasil kalibrasi dari hasil uji per kamera/kategori dan laporkan data gagal/tidak layak beserta alasannya.
5. **Respons dan lock.** Target 3 detik berbeda dari lock sebelum merah bersama. Plan valid setelah 3 detik tetapi sebelum lock dapat diterima secara fungsional pada UJI-16, namun target responsnya tidak terpenuhi. Plan baru setelah lock ditolak untuk giliran tersebut. Keberhasilan statis tidak mengubah kegagalan target respons menjadi lulus.
6. **Versi dan pembekuan.** Bekukan model/inferensi, pengamatan, dan parameter sebelum evaluasi akhir. Bila data uji dipakai menyetel versi baru, catat sebagai data pengembangan dan gunakan data uji yang tetap terpisah untuk klaim evaluasi independen versi baru.
7. **Bukti pelaksanaan.** Review rancangan atau simulasi dicatat sesuai bentuknya. Kasus keluaran fisik dan respons penerimaan ESP32 memerlukan bukti perangkat aktual. Hasil persiapan dengan CPU saja belum membuktikan kecukupan konfigurasi server GPU.

## 8. Pencatatan hasil aktual dan pelaporan minggu 1

### 8.1 Format hasil uji saat dilaksanakan

Format berikut digunakan ketika pengujian berlangsung dan dapat dirinci pada rencana uji. Dokumen ini tidak membuat rekap hasil fiktif.

```text
ID kebutuhan | ID UJI / jenis review | tanggal dan pelaksana |
versi kode/model/parameter | identitas sampel/kondisi |
hasil yang diharapkan | hasil aktual/nilai ukur | status |
path bukti | temuan | PIC dan tindak lanjut | hasil uji ulang
```

Rekap teknis dikelola Ikrom pada `KELOMPOK-10/evidence/S06/rekap-kasus-uji.csv`; bukti uji yang dilakukan pada sprint sebelumnya tetap ditautkan ke lokasi asal. Review KJ tanpa ID UJI dicatat dengan kode KJ dan jenis review, tanpa mengarang nomor kasus dari proposal. Log/laporan maintenance aktual mengikuti lokasi arsip yang ditetapkan pada panduan layanan.

### 8.2 Hasil W01-T03 dan commit

| Path lengkap | Isi / tindak lanjut minggu 1 |
|---|---|
| `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md` | Matriks 33 kebutuhan, hubungan dengan 34 UJI, kriteria, PIC, rencana bukti, dan keputusan terbuka ini. |
| `KELOMPOK-10/evidence/S01/README.md` | Nicy mencatat ringkasan W01-T03, hasil pemeriksaan, temuan/tindak lanjut, dan URL commit pada bagian Minggu 1. |
| `KELOMPOK-10/evidence/S01/log-aktivitas.md` | Nicy mencatat tanggal dan aktivitas aktual penyusunan/pemeriksaan matriks. |

Pesan commit pekerjaan untuk berkas ini:

```text
S01-W01: susun matriks kebutuhan dan verifikasi
```

Setelah SRS, pembagian pekerjaan, dan matriks diperiksa serta pelaporan dilengkapi, commit pelaporan minggu 1 mengikuti Kanban:

```text
S01-W01: susun SRS dan pembagian pekerjaan
```

Commit pelaporan harus mencakup ketiga dokumen beserta ringkasan/log aktual. Setelah push, URL commit pelaporan dicatat pada README melalui pembaruan berikutnya; jangan mengisi URL yang belum terbentuk.

### 8.3 Checklist pemeriksaan W01-T03

- [ ] KF-01–KF-11, KNF-01–KNF-12, dan KJ-01–KJ-10 lengkap serta konsisten dengan SRS.
- [ ] Semua UJI-01–UJI-34 terpetakan sesuai Tabel 6.2.
- [ ] Kebutuhan jasa tanpa nomor UJI memiliki metode review yang jelas.
- [ ] Kesiapan dokumen maintenance dibedakan dari realisasi layanan setelah penyerahan.
- [ ] Parameter belum final dan ketidakkonsistenan naskah memiliki PIC/tindak lanjut.
- [ ] Tidak ada klaim pengujian lulus atau nilai hasil yang belum mempunyai bukti.
- [ ] Ringkasan, log kegiatan aktual, dan hasil pemeriksaan Nicy dicatat sebelum pelaporan minggu 1 ditutup.

