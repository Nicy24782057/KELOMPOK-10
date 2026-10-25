# M01 — Hasil Pemeriksaan dan Rencana Pelaksanaan

**PIC:** Nicy Putra Pratama  
**Tanggal:** 25/10/2026

## 1. Hasil Pemeriksaan Rencana Kerja

Pemeriksaan dilakukan terhadap kesesuaian rencana pekerjaan pada Kanban dengan kebutuhan dan batasan proposal serta hasil kesepakatan revisi.

| Aspek | Hasil pemeriksaan |
|---|---|
| Sumber CCTV | Rencana pembacaan tiga CCTV dari lokasi berbeda dan pemetaan ke fase virtual A/B/C sudah tercantum pada M06. |
| Area dan waktu pengamatan | Pembatasan pendekat lurus menuju garis henti serta pengamatan pagi, siang, dan sore sudah tercantum pada kartu terkait. |
| Deteksi dan penghitungan | Implementasi YOLO, empat kelas kendaraan, titik acuan bounding box, dan penghitungan satu snapshot sudah tercantum pada M07. |
| Kepadatan, kategori, dan durasi | Perhitungan kepadatan serta kalibrasi kategori dan durasi sudah dibagi pada M09 sesuai bidang pelaksana. |
| Integrasi dan perangkat | Perakitan, komunikasi MQTT, pelaksanaan rencana, OLED, dan pencatatan sistem sudah tercantum pada M05 serta M10–M11. |
| Pengujian | Pengukuran respons, evaluasi independen, pengujian gangguan, dan perbaikan sudah tercantum pada M12–M15. |
| Pembanding non-YOLO | Sesuai hasil kesepakatan revisi, perbandingan dengan detektor lain dilakukan melalui kajian literatur. Evaluasi implementasi difokuskan pada YOLO menggunakan data CCTV dan perangkat proyek. Redaksi proposal yang masih menyebut pengujian langsung pembanding dicatat sebagai temuan penyelarasan F01. |

Pemeriksaan ini menilai rencana pekerjaan. Keberhasilan implementasi diperiksa pada kartu pelaksanaan masing-masing.

## 2. Pembagian Tanggung Jawab

| Anggota | Tanggung jawab pelaksanaan |
|---|---|
| Nicy | Koordinasi, pemeriksaan kebutuhan dan hasil, pemantauan progres, serta tindak lanjut hambatan. |
| Putu/Radit | Backend, kategori kepadatan, penentuan durasi, komunikasi, dan integrasi. |
| Rizky | Pembacaan CCTV, konfigurasi ROI, deteksi, penghitungan, kepadatan, dan evaluasi AI. |
| Ramdhani | Rangkaian, firmware ESP32, LED, OLED, serta pelaksanaan urutan dan durasi lampu. |
| Ikrom | Data pengamatan, pengelolaan pencatatan sistem, skenario, bukti, dan dokumentasi pengujian. |

M01 dikerjakan oleh Nicy. Anggota lain melaksanakan pekerjaan pada kartu sesuai tanggung jawab masing-masing.

## 3. Kebutuhan dan Ketergantungan Pekerjaan

| Tahap | Kebutuhan dan ketergantungan |
|---|---|
| Penyiapan repositori dan format pesan — M02–M03 | Repositori menjadi tempat penyimpanan hasil. Format konfigurasi dan pesan menjadi acuan pertukaran data antarmodul. |
| Lingkungan dan perangkat — M04–M05 | Lingkungan server dan AI serta komponen perangkat disiapkan sesuai PIC. Perakitan perangkat dapat berjalan paralel dengan pengembangan AI. |
| Pembacaan CCTV, penghitungan, dan pengamatan — M06–M08 | Konfigurasi kamera dan ROI diperlukan untuk penghitungan serta pengumpulan data pengamatan yang konsisten. |
| Kalibrasi — M09 | Kalibrasi membutuhkan data pengamatan, hitungan manual, panjang area, dan jumlah lajur. |
| Integrasi — M10–M11 | Integrasi membutuhkan keluaran AI, backend, layanan komunikasi, dan perangkat yang dapat digunakan. |
| Pengujian — M12–M14 | Pengujian dilakukan pada versi yang dicatat. Evaluasi independen menggunakan parameter yang dibekukan dan data terpisah. |
| Perbaikan dan serah terima — M15–M16 | Perbaikan mengikuti temuan pengujian. Dokumentasi akhir disesuaikan dengan versi yang diserahkan. |

Daftar ini menjadi acuan urutan kerja dan kebutuhan awal. Status ketersediaan serta keberhasilan teknis dicatat pada kartu pelaksanaannya.

## 4. Prioritas Demonstrasi Awal

Target demonstrasi awal adalah alur CCTV → deteksi dan penghitungan → kepadatan → rencana durasi → MQTT → ESP32 dan LED.

| Bagian yang diprioritaskan | PIC |
|---|---|
| Lingkungan backend, layanan MQTT, dan pengiriman rencana. | Putu |
| Pembacaan CCTV, penghitungan kendaraan, dan perhitungan kepadatan. | Rizky |
| Rangkaian, urutan lampu, dan penerimaan rencana pada ESP32. | Ramdhani |
| Pencatatan hasil percobaan dan bukti demonstrasi sesuai pekerjaan terkait. | Ikrom |

Pekerjaan inti yang diperlukan untuk demo dapat didahulukan sesuai ketergantungannya. Hasil tetap dicatat pada kartu asal. Jadwal pengembangan keseluruhan tetap 16 minggu.

Parameter yang belum berasal dari kalibrasi diberi keterangan **parameter sementara untuk demo**.

## 5. Temuan dan Tindak Lanjut

Acuan pelaksanaan mengikuti hasil kesepakatan revisi: pembandingan detektor dilakukan melalui literatur, sedangkan evaluasi implementasi difokuskan pada YOLO. Pengujian hitungan, waktu pemrosesan, penggunaan sumber daya, serta integrasi tetap dilaksanakan sesuai kartu terkait.

| ID | Temuan | Tindak lanjut | Penanggung jawab | Status |
|---|---|---|---|---|
| F01 | Sebagian redaksi pada bagian keahlian, risiko, BMC, dan cakupan layanan proposal masih menyebut pembandingan langsung dengan detektor non-YOLO, sementara hasil kesepakatan revisi menetapkan pembandingan melalui literatur. | Menyelaraskan redaksi yang tersisa dengan hasil kesepakatan revisi. Rencana implementasi dan evaluasi detektor pada Kanban tetap berfokus pada YOLO. | Nicy mengoordinasikan penyelarasan dokumen. | Keputusan pelaksanaan sudah jelas; penyelarasan redaksi proposal masih perlu ditindaklanjuti. |

Kebutuhan atau hambatan lain ditambahkan berdasarkan kondisi aktual, disertai penanggung jawab dan tindak lanjutnya.

## 6. Pemantauan Setelah M01

Nicy memantau progres dan memeriksa hasil pada kartu yang sedang dikerjakan anggota. Catatan pemeriksaan ditempatkan pada bagian **Review PM** di README kartu terkait.

Hasil pemeriksaan repositori dicatat pada M02, kesiapan lingkungan pada M04, perangkat pada M05, dan seterusnya sesuai pekerjaan yang diperiksa.

Penyelesaian M01 mengikuti kelengkapan hasil pemeriksaan awal, pembagian tanggung jawab, kebutuhan, ketergantungan, prioritas, dan tindak lanjut yang telah dicatat.
