## Minggu 3

### Ringkasan hasil

**Target:** LLD rangkaian/pin ESP32, komunikasi/konfigurasi, urutan lampu dan pemicu, prosedur pengamatan, template data, rencana uji serta penyelarasan dokumen.

**Status:** Review — seluruh isi W03-T01–W03-T07 tersedia dalam paket. PIC menunjukkan pemilik bidang sesuai rencana; paket disiapkan dengan bantuan penyusunan. Penelaahan masing-masing anggota, persetujuan PM, implementasi dan uji fisik dicatat saat benar-benar dilakukan.

| ID tugas | PIC bidang | Hasil / path lengkap | Status |
|---|---|---|---|
| W03-T01 | Ramdhani | `KELOMPOK-10/docs/perangkat/perakitan.md` dan `KELOMPOK-10/docs/perangkat/skema-rangkaian.svg`: 9 LED/resistor, OLED, daya, GPIO, urutan/timer/lock, statis dan pemulihan | Review — rancangan tersedia |
| W03-T02 | Putu Radit Ardika | `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md`; lima JSON di `KELOMPOK-10/configs/mqtt/`: topik, arah, field/versi/ID, validitas, QoS/TLS, duplikasi dan pesan terlambat | Review — kontrak/contoh tersedia |
| W03-T03 | Putu Radit Ardika | `KELOMPOK-10/configs/control.example.json` dan panduan backend: struktur fase/kategori/durasi/statis serta waktu; contoh nonaktif dan belum dikalibrasi | Review — struktur tersedia |
| W03-T04 | Rizky Bintang Fadillah | `KELOMPOK-10/docs/perencanaan/prosedur-ai-dan-pengamatan.md`: YOLO, satu snapshot, ROI/k, sampel pagi/siang/sore, kelompok awal dan layanan lintas hijau, split/freeze | Review — prosedur tersedia |
| W03-T05 | Ikrom Safei | `KELOMPOK-10/data/templates/kalibrasi.csv`, `KELOMPOK-10/data/templates/pengujian.csv`, dan `KELOMPOK-10/data/templates/README.md`: masing-masing 64 kolom, header kosong, kamus/panduan pengisian | Review — format tersedia |
| W03-T06 | Ikrom Safei | `KELOMPOK-10/docs/pengujian/rencana-uji.md`: UJI-01–UJI-34 dengan prasyarat, langkah, harapan/kriteria, PIC, metrik dan bukti | Review — seluruh kasus terinci |
| W03-T07 | Nicy Putra Pratama | `KELOMPOK-10/docs/perencanaan/indeks-perencanaan.md`: indeks sumber/SRS/HLD/LLD, pemeriksaan konsistensi dan RV-01–RV-10 | Review — catatan tersedia, penerimaan PM menunggu |

### Pemeriksaan berkas

Hasil pemeriksaan format lokal disimpan di `KELOMPOK-10/evidence/S01/hasil-pemeriksaan-minggu-3.txt`. Cakupannya parsing enam JSON, hubungan contoh pesan/config, konsistensi hitungan/durasi/waktu contoh, dua CSV kosong identik, kelengkapan 34 kasus dan paket khusus minggu 3. Ini tidak membuktikan MQTT/perangkat/pengujian sistem sudah berjalan.

### Kendala dan tindak lanjut

| Hal yang ditunggu | PIC | Tahap penetapan |
|---|---|---|
| Model/bobot/inferensi YOLO dan lingkungan aktual | Rizky | Implementasi, sebelum evaluasi akhir |
| Sumber, ROI/L/lajur, waktu/umur frame dan kelayakan rekaman | Rizky + Ikrom | Pemeriksaan sumber/pengamatan |
| K1/K2, durasi/batas dan statis lokal terverifikasi | Putu + Rizky + Ikrom + Ramdhani | Kalibrasi/operasi sebelum uji terkait |
| Papan/pin/OLED/daya aktual dan toleransi timing pra-uji | Ramdhani + Ikrom | Inventaris/perakitan/integrasi |
| Server/GPU, layanan/volume, TLS/ACL dan pencatatan aktual | Putu + Rizky + Ikrom | Minggu 4/integrasi |
| Penyelarasan pembanding non-YOLO, judul dan instruksi editorial sumber | Nicy bersama pemilik materi | Sebelum pembekuan/naskah akhir |

### Review PM — Minggu 3

Pemeriksaan penyelarasan rancangan tercatat di indeks dan hasil format. **Keputusan penerimaan oleh Nicy belum dicatat.** Isi tanggal/hasil/PIC tindak lanjut setelah review aktual, tanpa menandai persetujuan anggota yang belum dilakukan.

| Tanggal review | Pemeriksa | Keputusan penerimaan / temuan | PIC dan tindak lanjut | Bukti |
|---|---|---|---|---|
| Belum dilaksanakan/dicatat | Nicy Putra Pratama | Menunggu penelaahan hasil minggu 3 | RV-01–RV-10 pada indeks; PIC bidang menelaah masing-masing bagian | Tambahkan setelah pemeriksaan aktual |

### Commit pelaporan — Minggu 3

Pesan yang disarankan: `S01-W03: lengkapi LLD dan prosedur pengamatan`.

Cakupan: seluruh hasil baru minggu 3, bagian Minggu 3 README/log dan hasil pemeriksaan format. Bagian minggu 1/2 pada berkas bersama tetap dipertahankan.

**URL commit pelaporan:** Belum diisi — tempel URL aktual setelah push. Jika URL baru ditambahkan sesudah commit hasil terbentuk, catat pada pembaruan pelaporan berikutnya; jangan membuat URL contoh seolah sudah di-push.

### Kelengkapan minggu 3 dan penutupan S01

- [x] Isi dan lokasi hasil W03-T01–W03-T07 tersedia dalam paket.
- [x] Log penyusunan paket minggu 3 terisi; penelaahan/kegiatan aktual tiap anggota ditambahkan ketika dilakukan.
- [x] Catatan pemeriksaan rancangan dan tindak lanjut beserta PIC tersedia.
- [ ] Nicy telah mencatat review penerimaan PM.
- [ ] Hasil minggu 3 di-push dan URL commit pelaporan diisi.
- [ ] Hasil/log/review/URL minggu 1, 2 dan 3 di repositori lengkap sebelum S01 ditutup.
