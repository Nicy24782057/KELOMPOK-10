# Indeks perencanaan dan penyelarasan proposal

| Identitas | Nilai |
|---|---|
| Tim | KELOMPOK-10 |
| Versi dan tanggal | 0.2 / 25 November 2026 |
| Acuan | FINAL INI A(2).docx; aturan bersama pada acuan-revisi.md |
| Status | Dokumen paket diselaraskan; penerimaan tim dan hasil perangkat mengikuti bukti aktual |

## Acuan dan dokumen kerja

| Dokumen | Versi | Pemakaian |
|---|---|---|
| [Acuan revisi](acuan-revisi.md) | 1.0 | Definisi frame, kelompok, waktu layanan, timing, pin, dan batas paket |
| [SRS](srs.md) | 0.2 | KF-01–KF-11, KNF-01–KNF-12, KJ-01–KJ-10 |
| [HLD](hld.md) | 0.3 | Arsitektur, alur AI/backend/perangkat/pencatatan |
| [Matriks kebutuhan](matriks-kebutuhan.md) | 0.2 | Hubungan 33 kebutuhan dengan UJI-01–UJI-34 |
| [Pembagian kerja](pembagian-kerja.md) | 0.2 | PIC, keluaran, dependensi, dan tahap S01–S08 |
| [Prosedur pengamatan](prosedur-ai-dan-pengamatan.md) | 0.2 | Frame sebelum hijau, kelompok tetap, waktu layanan, kalibrasi dan split |
| [Panduan dataset](../../data/templates/README.md) | 0.2 | Arti 64 kolom dan validasi awal |
| [Kontrak backend dan MQTT](../operasional/konfigurasi-backend-dan-mqtt.md) | 0.2 | Pemicu, pengukuran, rencana, ACK dan status |
| [Rangkaian](../perangkat/perakitan.md) | 0.2 | GPIO proposal revisi dan urutan lampu |
| [Rencana uji](../pengujian/rencana-uji.md) | 0.2 | Prosedur UJI-01–UJI-34; hasil pelaksanaan belum diisi |
| [Lingkungan server](../../infra/lingkungan-server.md) | 0.2 | Konfigurasi dan perintah dari root repositori |
| [Sinkronisasi kartu sprint](sinkronisasi-kanban-2026-11-25.md) | 1.0 | Uraian kartu yang harus mengikuti revisi berkas |

## Hasil penyelarasan paket

| Butir | Ketentuan revisi | Status |
|---|---|---|
| Frame kalibrasi | Sekitar lima detik sebelum hijau aktual; selang dicatat pada waktu yang sebanding | Diselaraskan dalam dokumen |
| Kelompok awal | Dari anotasi manual pada frame tersebut; keanggotaan tetap; initial_queue_count = manual_total pada anotasi sah | Diselaraskan dalam dokumen |
| Layanan | Dimulai saat hijau aktual; hanya hijau dijumlahkan; unknown bukan keberhasilan | Diselaraskan dalam dokumen |
| Operasi | Snapshot terbaru kamera fase berikutnya saat pemicu ditangani; fase ESP32 mandiri dari lampu CCTV | Diselaraskan dalam dokumen |
| Metadata | frame_id, waktu sumber bila tersedia, penerimaan, dan pemilihan dapat ditelusuri | Kontrak dan contoh tersedia |
| Timing | Pemicu saat sisa hijau 1 s; target respons 3 s; lock sebelum merah bersama; hijau berikutnya nominal +5 s | Rancangan; memerlukan pengukuran |
| GPIO | A 25/26/27, B 14/18/19, C 23/32/33; OLED21/22 | Sama pada proposal, tabel, SVG, dan contoh JSON; belum diuji fisik |
| Kalibrasi | K-means offline, 45+45 siklus rencana, freeze, E_N ≤10%, coverage ≥90% per kamera/kategori | Data/hasil aktual belum tersedia |

## Tindak lanjut dengan bukti aktual

| ID | Pekerjaan tersisa | PIC dan tahap |
|---|---|---|
| KT-01 | Memilih model/inferensi berdasarkan hitungan, waktu, dan sumber daya | Rizky; implementasi dan sebelum evaluasi |
| KT-02 | Menetapkan tiga sumber, ROI, panjang/lajur, timestamp dan ambang umur/offset | Rizky dan Ikrom; S04 sebelum pengamatan |
| KT-03 | Mengisi data kalibrasi, K1/K2, durasi/batas dan statis terverifikasi | Putu, Rizky, Ikrom dan Ramdhani; S04 dan sebelum operasi terkait |
| KT-04 | Memeriksa rangkaian aktual, kontrak pada perangkat, toleransi timing | Ramdhani, Putu dan Ikrom; S03 dan integrasi |
| KT-05 | Melengkapi inventaris dan bukti lingkungan target Ubuntu/GPU | Pemilik komponen; S02 dan integrasi |
| KT-06 | Menyamakan rumusan pembanding non-YOLO yang masih berbeda di proposal | Nicy dan Rizky; sebelum evaluasi final. Paket tidak menambahkan eksperimen non-YOLO wajib |
| KT-07 | Merapikan judul naskah akhir agar mengikuti sampul | Nicy; penyuntingan proposal |
| KT-08 | Menerapkan definisi revisi pada data/implementasi dan review tim | Penyelarasan berkas selesai dalam paket; pengamatan aktual tetap diperiksa |

## Riwayat dan pelaporan

Dokumen/log evidence/S01 dan evidence/S02 tetap memuat riwayat pada tanggal asal. Pernyataan yang merujuk versi lama tidak menjadi acuan metode terbaru. Gunakan dokumen kerja pada indeks ini untuk pelaksanaan baru. Hasil S01 digunakan sebagai acuan pelaksanaan. Tindak lanjut pemeriksaan berkas dicatat pada [rekap S02 Minggu 4](../../evidence/S02/README.md#tindak-lanjut-dokumen-minggu-4) dan [log aktivitas S02](../../evidence/S02/log-aktivitas.md), mengikuti susunan berkas sprint yang sudah tersedia.

Review penerimaan Nicy, kegiatan anggota, commit push, hasil layanan, foto rangkaian, dan hasil uji perangkat dicatat setelah benar-benar dilakukan. Pemeriksaan konsistensi berkas tidak menutup sprint atau meluluskan pengujian fisik.
