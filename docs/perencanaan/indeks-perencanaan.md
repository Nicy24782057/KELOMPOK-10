# Indeks perencanaan dan catatan penyelarasan S01

| Identitas | Nilai |
|---|---|
| Tim / sprint / minggu | KELOMPOK-10 / S01 / 3 |
| Tugas / PIC | W03-T07 / Nicy Putra Pratama |
| Versi / tanggal | 0.1 / 29 Oktober 2026 |
| Status | Indeks dan pemeriksaan konsistensi paket tersedia; menunggu review penerimaan PM |
| Lokasi | `KELOMPOK-10/docs/perencanaan/indeks-perencanaan.md` |

## 1. Acuan yang digunakan

Sumber utama adalah [proposal sempro FINAL INI A(1).docx](https://chatgpt.com/library?file_id=libfile_a053b583a2988191a86db0925c2a4b52&account_id=personal). Gunakan versi ini, bersama SRS/HLD dan Kanban Sprint 01–08 yang menjadi dasar minggu 1/2. Rujukan Word di bawah memakai nomor bab/tabel dan halaman naskah yang terlihat pada versi sempro; tidak menyatakan bahwa Word sumber telah diedit.

| Sumber | Bagian yang dipakai | Pemakaian |
|---|---|---|
| Proposal sempro | Bab 4; Subbab 5.1–5.3; Tabel 5.5–5.7; Tabel 6.2 dan kriteria Bab 6 | Kebutuhan, arsitektur, pesan/data, pengamatan/kalibrasi dan UJI-01–UJI-34 |
| SRS 0.1 minggu 1 | KF-01–KF-11, KNF-01–KNF-12, KJ-01–KJ-10; Bagian 8/9 | Batas prototipe, sumber daya, dataset, ketidakpastian dan keputusan terbuka |
| Pembagian kerja 0.1 minggu 1 | S01 minggu 3 / W03-T01–W03-T07 | PIC, keluaran, dependensi dan lokasi |
| Matriks kebutuhan 0.1 minggu 1 | Matriks dan KT-01–KT-08, catatan persamaan | Hubungan 33 kebutuhan dengan verifikasi/34 UJI |
| HLD 0.2 minggu 2 | Bagian 3 dan 4.1–4.4 | Host/Docker, AI, backend/MQTT, ESP32, pencatatan |
| Kanban Sprint 01–08 | S01 minggu 3 | Tujuh tugas, hasil/lokasi dan commit pelaporan |

Versi minggu 1/2 di atas adalah versi dokumen acuan penyusunan. Jika versi yang sudah di-push berubah, catat perbedaannya pada review berikutnya. Paket ini berisi hasil baru minggu 3 dan potongan pelaporan yang ditambahkan ke berkas bersama; SRS/HLD/berkas minggu sebelumnya tidak disertakan untuk ditimpa.

## 2. Indeks dokumen dan konfigurasi

| Path lengkap | Versi / lingkup | PIC |
|---|---|---|
| `KELOMPOK-10/docs/perencanaan/srs.md` | 0.1; acuan kebutuhan minggu 1 yang sudah ada | Nicy |
| `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md` | 0.1; acuan tugas/dependensi yang sudah ada | Nicy |
| `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md` | 0.1; acuan verifikasi/KT yang sudah ada | Nicy |
| `KELOMPOK-10/docs/perencanaan/hld.md` | 0.2; acuan HLD minggu 2 yang sudah ada | Semua PIC sesuai bidang |
| `KELOMPOK-10/docs/perangkat/perakitan.md` | 0.1; pin, daya, state/timing, statis dan OLED | Ramdhani |
| `KELOMPOK-10/docs/perangkat/skema-rangkaian.svg` | Pin map 0.1; 9 LED/resistor dan OLED | Ramdhani |
| `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md` | 0.1; kontrak schema 1.0, topik/validasi/duplikasi dan parameter | Putu |
| `KELOMPOK-10/configs/control.example.json` | schema 1.0; control-demo-w03-v1, demonstrasi nonaktif | Putu |
| `KELOMPOK-10/configs/mqtt/trigger.example.json` | schema 1.0; trigger giliran sasaran | Putu |
| `KELOMPOK-10/configs/mqtt/measurement.example.json` | schema 1.0; salinan hasil pengukuran valid | Putu |
| `KELOMPOK-10/configs/mqtt/plan.example.json` | schema 1.0; kandidat giliran sasaran | Putu |
| `KELOMPOK-10/configs/mqtt/ack.example.json` | schema 1.0; hasil penerimaan kandidat | Putu |
| `KELOMPOK-10/configs/mqtt/status.example.json` | schema 1.0; pelaksanaan giliran aktif | Putu; Ramdhani implementasi |
| `KELOMPOK-10/docs/perencanaan/prosedur-ai-dan-pengamatan.md` | 0.1; snapshot/ROI, pengamatan, kalibrasi dan split | Rizky |
| `KELOMPOK-10/data/templates/kalibrasi.csv` | Format header 0.1, 64 kolom, 0 baris pengamatan | Ikrom |
| `KELOMPOK-10/data/templates/pengujian.csv` | Format header 0.1, 64 kolom, 0 baris pengamatan | Ikrom |
| `KELOMPOK-10/data/templates/README.md` | 0.1; kamus seluruh kolom, status dan aturan analisis | Ikrom |
| `KELOMPOK-10/docs/pengujian/rencana-uji.md` | 0.1; 34 kasus, metrik/kriteria/prasyarat/bukti | Ikrom |
| `KELOMPOK-10/docs/perencanaan/indeks-perencanaan.md` | 0.1; indeks dan tindak lanjut ini | Nicy |
| `KELOMPOK-10/evidence/S01/hasil-pemeriksaan-minggu-3.txt` | Pemeriksaan format/kelengkapan paket aktual | Nicy mengoordinasikan review; hasil pemeriksaan paket tersimpan |
| `KELOMPOK-10/evidence/S01/README.md` | Bagian Minggu 3 ditambahkan dari potongan paket | Nicy mengoordinasikan |
| `KELOMPOK-10/evidence/S01/log-aktivitas.md` | Bagian Minggu 3 ditambahkan; kegiatan aktual tiap PIC ditambahkan saat dilakukan | Semua PIC |

README/log penuh sengaja tidak disertakan. Gunakan `TAMBAHAN_MINGGU_3/README_minggu_3.md` dan `log-aktivitas_minggu_3.md` untuk menambah/memperbarui hanya bagian Minggu 3 pada kedua berkas bersama.

## 3. Pemetaan keluaran tugas dan ketergantungan

| ID | Keluaran minggu 3 | Ketergantungan / pemakai berikutnya | Status |
|---|---|---|---|
| W03-T01 | Skema, GPIO, sambungan/daya, urutan lampu, lock/statis/OLED | HLD; inventaris minggu 4, perakitan minggu 5 dan firmware/integrasi | Review — isi rancangan lengkap |
| W03-T02 | Kontrak lima pesan dan lima JSON konsisten | HLD/Tabel 5.5; adapter AI, klien ESP32, logging | Review — kontrak lengkap |
| W03-T03 | Contoh konfigurasi kategori/durasi/fallback/timing | W03-T02; kalibrasi dan integrasi | Review — struktur lengkap, nilai hasil ukur menunggu kalibrasi |
| W03-T04 | LLD AI dan prosedur sampel/layanan | HLD dan kontrak; pemeriksaan sumber, AI dan pengamatan | Review — prosedur lengkap |
| W03-T05 | Dua CSV kosong dan kamus pengisian | W03-T04 dan kebutuhan data; kalibrasi/uji | Review — format lengkap |
| W03-T06 | Rencana 34 UJI berikut metrik dan bukti | SRS/matriks/LLD/prosedur; pelaksanaan uji bertahap | Review — semua kasus terinci |
| W03-T07 | Indeks, pemeriksaan konsistensi dan register tindak lanjut | Seluruh hasil minggu 1–3; review penerimaan PM | Review — catatan tersedia, persetujuan PM belum dicatat |

## 4. Hasil penyelarasan isi paket

Pemeriksaan ini adalah pemeriksaan rancangan/format dalam penyusunan paket, **belum persetujuan Nicy atas hasil anggota dan belum uji sistem**. PIC pada tabel adalah pemilik bidang menurut pembagian kerja.

| Butir | Hasil penyelarasan / bukti | Status |
|---|---|---|
| Pembagian host dan Docker | AI/reader/backend pada host; Mosquitto/Node-RED/InfluxDB di Docker satu server; ESP32 pelaksana timer | Selaras dengan HLD |
| Frame/ROI/kepadatan | Satu frame utuh/pemicu, bottom-center dalam/batas, empat kelas unit satu, k kendaraan/km/lajur | Selaras antara prosedur, pesan dan rencana uji |
| Nol versus gagal | Measurement valid nol berbeda dari invalid null/reason; OLED -- bila data tidak ada | Selaras |
| Antarmuka AI/backend | Internal untuk kendali; MQTT measurement salinan pencatatan | Selaras dengan Tabel 5.3/HLD |
| Identitas giliran | Target pada trigger/measurement/plan/ACK; aktif pada status, contoh target 42 dari aktif 41 | Selaras; startup status turn_id 0 dijelaskan |
| Waktu dan lock | Pemicu 1 s; target 3 s; kuning 3 s; merah bersama 1 s; lock sebelum merah bersama | Selaras, toleransi aktual masih terbuka |
| Contoh normal | ACK 1800 ms dan status hijau nominal +5 s; plan 20 s dari N=6/k=30 | Konsisten sebagai fixture demonstrasi |
| GPIO | Sembilan GPIO unik, I²C21/22, satu resistor/LED, GND bersama, satu suplai | Rancangan selaras; verifikasi fisik berikutnya |
| Statis/pemulihan | Statis lokal saat tanpa kandidat di lock; adaptif pulih giliran sah berikutnya; tidak memotong aktif | Selaras |
| Duplikasi | Satu pengukuran unik, plan/ACK identik digunakan kembali, tidak reset timer | Selaras; cache/restart implementasi diuji berikutnya |
| Kelompok awal dan split | Count frame terpisah dari antrean awal; hijau saja, unknown tetap penyebut; 45+45 hari berbeda | Selaras antara prosedur, CSV dan rencana uji |
| Kalibrasi dan metrik | Offline K-means/P90; freeze; E_N≤10% per kamera; coverage≥90% per kamera/kategori setelah clamp | Selaras; data/hasil tidak dikarang |
| Pelaporan | Potongan README/log minggu 3 terpisah dan URL commit belum diisi | Menjaga bagian minggu sebelumnya |

Rincian parsing JSON, pemeriksaan hubungan contoh, header CSV dan kelengkapan kasus/path dicatat pada `KELOMPOK-10/evidence/S01/hasil-pemeriksaan-minggu-3.txt` setelah pemeriksaan lokal. Hasil pemeriksaan berkas tidak menggantikan UJI-01–UJI-34.

## 5. Temuan, PIC dan tindak lanjut

| ID / acuan | Temuan atau keputusan tersisa | PIC | Tindak lanjut / batas tahap |
|---|---|---|---|
| RV-01 / KT-01 | Varian/bobot/inferensi YOLO belum dipilih | Rizky | Catat manifest dan bukti ketepatan/waktu/resource saat implementasi, bekukan sebelum uji akhir |
| RV-02 / KT-02 | Sumber aktual, ROI, L/lajur, time basis/ambang umur dan selang frame-ke-hijau belum ditetapkan | Rizky + Ikrom | Pemeriksaan sumber minggu 6 dan sebelum pengamatan/uji terkait |
| RV-03 / KT-03 | K1/K2, data kelompok/durasi/batas dan statis aktual belum tervalidasi | Putu + Rizky + Ikrom; Ramdhani statis | Kalibrasi sebelum operasi/uji final; semua angka contoh tetap nonoperasional |
| RV-04 / KT-04 | GPIO/kontrak telah dirancang, papan/pin/OLED aktual dan toleransi timing belum diverifikasi | Ramdhani + Putu + Ikrom | Inventaris/perakitan/integrasi; tetapkan toleransi sebelum uji |
| RV-05 / KT-05 | Server/versi layanan, GPU, TLS/ACL/volume, antrean log/deduplikasi dan interval status belum diimplementasikan | Putu + Rizky; Ikrom logging | Minggu 4 dan integrasi; verifikasi UJI-21–UJI-27 |
| RV-06 / KT-06 | Sumber berbeda tentang pembanding non-YOLO (2.1/4.1.2/BMC versus Tabel 1.3/6.1) | Nicy + Rizky | Selaraskan naskah/lingkup sebelum evaluasi final; belum menjadi pengujian wajib tambahan |
| RV-07 / KT-07 | Judul sampul dan Subbab 4.1.1 belum seragam | Nicy | Seragamkan pada revisi naskah akhir tanpa menimpa minggu 1 pada paket ini |
| RV-08 / KT-08 | Instruksi editorial 5.3 dan istilah frame/kelompok awal perlu penyuntingan sumber | Nicy + Rizky + Putu + Ikrom | Prosedur operasional telah dirinci; perbaiki naskah sumber sebelum pembekuan |
| RV-09 / matriks | Rujukan durasi pada UJI-11 memakai nomor persamaan lama | Nicy | Selaraskan rujukan Word; rencana uji memakai substansi base+tambahan/clamp |
| RV-10 / pelaporan | Review PM/commit minggu 3 belum dilakukan/diberikan dalam penyusunan paket | Nicy | Setelah review aktual dan push, catat keputusan/tindak lanjut/URL; tidak mengisi persetujuan fiktif |

## 6. Pemeriksaan penerimaan S01

- [x] Isi tujuh tugas minggu 3 tersedia di path yang ditentukan, termasuk contoh JSON, CSV dan rencana semua UJI sumber.
- [x] Rancangan antarbidang dan kebutuhan terbuka memiliki catatan/PIC/tahap penetapan.
- [x] Berkas minggu 1/2 tidak dimasukkan untuk diganti; pelaporan minggu 3 disediakan sebagai tambahan.
- [ ] Setiap PIC menelaah isi bidangnya dan menambahkan kegiatan aktual/revisi bila diperlukan.
- [ ] Nicy mencatat review penerimaan PM atas hasil minggu 3.
- [ ] Commit pelaporan minggu 3 sudah di-push dan URL aktual dicatat.
- [ ] Kelengkapan hasil/log/review/URL minggu 1, 2 dan 3 pada repositori telah diperiksa untuk menutup S01.

Isi rancangan lengkap memungkinkan persiapan lingkungan minggu 4 dilanjutkan sambil menyelesaikan keputusan sesuai tahapnya. Pekerjaan yang memerlukan alat/data/parameter aktual menunggu prasyarat terkait, bukan digantikan angka buatan.
