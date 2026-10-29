# Bukti Pelaksanaan Sprint 01 — Analisis Kebutuhan dan Perancangan

| Keterangan | Isi |
|---|---|
| Tim | KELOMPOK-10 |
| Proyek | Estimasi Kepadatan Kendaraan dari CCTV untuk Pengendalian Lampu Lalu Lintas Adaptif pada Prototipe IoT |
| Periode sprint | Minggu 1–3 |
| Penanggung jawab sprint | Nicy Putra Pratama |
| Tanggal penyusunan draf pelaporan | 29 Oktober 2026 |
| Versi | 0.1 |
| Status pelaporan | Draf minggu 1; menunggu pemeriksaan Nicy, pengisian tanggal aktivitas aktual, dan pencatatan commit |
| Lokasi | `KELOMPOK-10/evidence/S01/README.md` |

## Acuan dan cara pencatatan

Acuan kebutuhan adalah proposal sempro **`FINAL INI A(1).docx`**, SRS, pembagian pekerjaan, matriks kebutuhan, dan Kanban Sprint 01–08 versi yang diselaraskan dengan sempro pada 29 Oktober 2026. Model tetap ditulis **YOLO**; variannya dipilih saat implementasi.

README ini merangkum hasil dan pemeriksaan sprint per minggu. Kegiatan pribadi masing-masing pelaksana dicatat pada [log-aktivitas.md](log-aktivitas.md). Tanggal penyusunan draf bukan pengganti tanggal kegiatan aktual yang belum dikonfirmasi.

Status tugas mengikuti **To do → In progress → Review → Done**. Pada draf ini, tiga dokumen minggu 1 sudah tersusun dan ditempatkan pada **Review**. Pemeriksaan/penerimaan oleh Nicy serta commit/push belum dicatat sebagai selesai. Bukti lama M01–M16 tetap dipertahankan dan baru ditautkan jika isi serta versinya relevan.

## Ringkasan sprint

| Minggu | Fokus | Status saat penyusunan draf ini |
|---|---|---|
| 1 | SRS, pembagian pekerjaan, matriks kebutuhan, dan pelaporan. | Review — draf hasil tersedia; pemeriksaan Nicy dan commit belum dikonfirmasi. |
| 2 | HLD dan pembagian fungsi komponen. | To do — belum dilaporkan dalam berkas ini. |
| 3 | Rancangan terperinci, prosedur pengamatan, dan rencana pengujian. | To do — belum dilaporkan dalam berkas ini. |

## Minggu 1

**PIC seluruh pekerjaan minggu 1:** Nicy Putra Pratama.

**Tanggal kegiatan aktual:** [Diisi Nicy sesuai pelaksanaan pada log aktivitas].  
**Status minggu:** Review; belum ditutup.

### Hasil pekerjaan

| ID tugas | PIC | Hasil aktual yang tersedia sebagai draf | Lokasi berkas/bukti | Status | Kendala dan tindak lanjut |
|---|---|---|---|---|---|
| W01-T01 | Nicy | SRS versi 0.1 memuat 11 KF, 12 KNF, 10 KJ, ruang lingkup, perangkat/server/software, antarmuka, data, waktu, serta maintenance. Model ditulis YOLO; keputusan terbuka dicatat pada Bagian 9. | `KELOMPOK-10/docs/perencanaan/srs.md` | Review | Nicy memeriksa kesesuaian naskah sempro dan mencatat keputusan/perbaikan yang diperlukan. |
| W01-T02 | Nicy | Pembagian kerja versi 0.1 mencakup 8 sprint/16 minggu, nama PIC, rincian pekerjaan, hasil, path lengkap, dan ketergantungan antarpekerjaan. | `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md` | Review | Nicy memeriksa pembagian terhadap peran tim dan Kanban; perubahan penugasan dicatat jika diperlukan. |
| W01-T03 | Nicy | Matriks versi 0.1 memetakan 33 kebutuhan dan 34 UJI dari proposal, PIC, cara verifikasi, kriteria, status penetapan, jadwal, serta rencana lokasi bukti. Kebutuhan layanan tanpa ID UJI khusus mempunyai metode review. | `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md` | Review | Nicy memeriksa pemetaan, parameter terbuka, serta rujukan naskah; tidak mengisi hasil pengujian yang belum dilaksanakan. |

### Hasil dan lokasi berkas minggu 1

| Path lengkap | Fungsi | PIC |
|---|---|---|
| `KELOMPOK-10/docs/perencanaan/srs.md` | Kebutuhan dan batasan sistem beserta sumber daya, jasa, maintenance, serta keputusan terbuka. | Nicy |
| `KELOMPOK-10/docs/perencanaan/pembagian-kerja.md` | Pembagian pekerjaan, hasil, jadwal, lokasi, dan ketergantungan anggota. | Nicy |
| `KELOMPOK-10/docs/perencanaan/matriks-kebutuhan.md` | Hubungan kebutuhan, PIC, metode verifikasi, UJI, kriteria, dan tindak lanjut penetapan. | Nicy |
| `KELOMPOK-10/evidence/S01/README.md` | Ringkasan mingguan, pemeriksaan, tindak lanjut, dan URL commit. | Nicy |
| `KELOMPOK-10/evidence/S01/log-aktivitas.md` | Rekap draf kegiatan untuk dikonfirmasi, kemudian catatan aktivitas aktual Nicy/anggota sesuai minggunya. | Setiap pelaksana; minggu 1 Nicy |

Tautan cepat: [SRS](../../docs/perencanaan/srs.md), [pembagian kerja](../../docs/perencanaan/pembagian-kerja.md), [matriks kebutuhan](../../docs/perencanaan/matriks-kebutuhan.md).

### Pemeriksaan kelengkapan draf

Pemeriksaan penyusunan telah memastikan bahwa ketiga draf menggunakan penyebutan YOLO, pembagian pekerjaan mencakup minggu 1–16, serta matriks mencakup 33 kode kebutuhan dan 34 UJI. Path dalam matriks telah dicocokkan dengan lokasi tujuan pada Kanban.

Pemeriksaan kelengkapan ini tidak merupakan hasil pengujian prototipe atau penerimaan PM oleh Nicy. Kondisi alat/server, tanggal kegiatan pribadi, jam kerja, dan tautan GitHub belum ditetapkan sebagai fakta aktual dalam pelaporan ini.

### Keputusan terbuka dan tindak lanjut

Daftar rinci tetap berada pada SRS Bagian 9 dan matriks Bagian 6. Tabel ini merangkum tindak lanjut, tanpa menyatakan bahwa semua nilai teknis harus selesai ditentukan pada minggu 1.

| ID | Pokok tindak lanjut | PIC sesuai tahap | Waktu yang dituju |
|---|---|---|---|
| KT-01 | Memilih varian/bobot YOLO dan konfigurasi inferensi berdasarkan hasil implementasi. | Rizky; Nicy memeriksa lingkup. | Implementasi AI; dicatat sebelum evaluasi akhir. |
| KT-02 | Menetapkan sumber/fase, ROI, panjang, lajur, metadata waktu, dan ambang validitas frame. | Rizky; Ikrom mencatat metadata. | Pemeriksaan sumber; sebelum pengujian terkait. |
| KT-03 | Melengkapi kalibrasi, parameter kategori/durasi, batas, dan statis lokal terverifikasi. | Putu; Rizky/Ikrom untuk data; Ramdhani untuk statis. | Kalibrasi, sebelum pembekuan dan evaluasi terpisah. |
| KT-04 | Merinci pin/catu daya, kontrak pesan, identitas, dan toleransi timing. | Ramdhani/Putu; Ikrom menyiapkan verifikasi. | LLD dan penyelesaian implementasi; sebelum uji terkait. |
| KT-05 | Mencatat penempatan server, versi lingkungan, ketersediaan alat, dan kecukupan kapasitas. | Putu/Rizky/Ramdhani sesuai komponen; Nicy mengoordinasikan. | Persiapan serta uji beban/integrasi. |
| KT-06 | Menyelaraskan rumusan pembanding non-YOLO yang berbeda antarbagian proposal. | Nicy bersama Rizky/tim. | Sebelum ruang lingkup evaluasi detektor difinalkan. |
| KT-07 | Menyeragamkan judul sampul dan penamaan pada bagian naskah. | Nicy. | Pemeriksaan dokumen kebutuhan/naskah. |
| KT-08 | Melengkapi instruksi editorial prosedur layanan dan membedakan hitungan frame dari kelompok awal. | Nicy bersama Putu/Rizky/Ikrom. | Sebelum prosedur pengamatan/kalibrasi dibekukan. |
| Catatan rujukan persamaan | Menyeragamkan rujukan durasi pada UJI-11 dan label persamaan evaluasi sesuai pembahasan matriks Bagian 6.2. | Nicy. | Pemeriksaan naskah; substansi kriteria tetap mengikuti SRS/proposal. |

**Kendala pelaksanaan aktual:** [Diisi Nicy bila ada; jika tidak ada, tulis “Tidak ada kendala yang dilaporkan pada periode ini” setelah diperiksa].

### Review PM

- Pemeriksa: **Nicy Putra Pratama**.
- Tanggal pemeriksaan aktual: [Diisi setelah pemeriksaan].
- Status pemeriksaan: **Belum dicatat oleh Nicy**.
- Hasil yang diterima: [Diisi setelah isi dan lokasi hasil diperiksa].
- Temuan/perubahan yang diperlukan: [Diisi berdasarkan pemeriksaan aktual; rujuk KT atau bagian dokumen terkait].
- PIC dan tindak lanjut: [Nama, pekerjaan, serta waktu tindak lanjut yang disepakati].
- Status akhir: [Belum diperiksa / Perlu perbaikan / Diterima].

### Pengumpulan dan commit minggu 1

Cakupan pelaporan adalah **lima berkas** pada tabel lokasi minggu 1: SRS, pembagian pekerjaan, matriks, README, dan log aktivitas.

Pesan commit pelaporan mengikuti Kanban:

```text
S01-W01: susun SRS dan pembagian pekerjaan
```

Commit pekerjaan terpisah untuk pembaruan pelaporan dapat menggunakan:

```text
S01-W01: lengkapi pelaporan minggu 1
```

**Commit pelaporan minggu 1:** [Tempel URL commit GitHub setelah di-push dan diperiksa].  
**Pencatat URL:** Nicy Putra Pratama.

Commit kerja anggota boleh lebih dari satu. Commit pelaporan yang dipilih harus berada pada riwayat yang telah menggabungkan hasil minggu 1. URL tersebut dicatat melalui pembaruan berikutnya setelah commit terbentuk; jangan membuat tautan atau SHA perkiraan.

### Checklist penutupan minggu 1

- [x] Draf SRS tersedia pada lokasi hasil.
- [x] Draf pembagian pekerjaan tersedia pada lokasi hasil.
- [x] Draf matriks kebutuhan tersedia pada lokasi hasil.
- [x] Draf README dan log aktivitas disiapkan.
- [ ] Nicy telah memeriksa isi ketiga dokumen dan mencatat hasil Review PM.
- [ ] Tanggal, pelaksana, kegiatan, dan hasil aktual pada log telah dikonfirmasi Nicy.
- [ ] Parameter/rumusan yang masih terbuka memiliki tindak lanjut; keputusan yang belum waktunya ditetapkan tetap berstatus terbuka.
- [ ] Lima berkas telah dimasukkan ke repositori pada path yang benar dan di-push.
- [ ] URL commit pelaporan minggu 1 sudah dicatat dan menunjuk hasil yang diperiksa.
- [ ] Status tugas diperbarui menjadi Done setelah hasil diterima; minggu 1 ditutup.

## Minggu 2

**Fokus:** HLD satu server dan pembagian fungsi komponen.  
**PIC:** Nicy, Rizky, Putu, Ramdhani, dan Ikrom sesuai tugas Kanban.  
**Status:** To do — hasil aktual belum dilaporkan.

Bagian ini dilengkapi saat pekerjaan minggu 2 dilaksanakan, dengan tabel hasil per PIC dan Review PM mengikuti format minggu 1.

**Commit pelaporan minggu 2:** [Tempel URL commit GitHub setelah di-push].  
**Contoh pesan commit:** `S01-W02: susun HLD sistem`.

## Minggu 3

**Fokus:** Rancangan terperinci, kontrak komunikasi, prosedur pengamatan, template data, serta rencana uji.  
**PIC:** Ramdhani, Putu, Rizky, Ikrom, dan Nicy sesuai tugas Kanban.  
**Status:** To do — hasil aktual belum dilaporkan.

Bagian ini dilengkapi saat pekerjaan minggu 3 dilaksanakan, dengan tabel hasil per PIC dan Review PM mengikuti format minggu 1.

**Commit pelaporan minggu 3:** [Tempel URL commit GitHub setelah di-push].  
**Contoh pesan commit:** `S01-W03: lengkapi LLD dan prosedur pengamatan`.

## Kriteria selesai Sprint 01

- [ ] Hasil minggu 1, 2, dan 3 tersedia serta dapat ditelusuri ke dokumen perencanaan.
- [ ] Fungsi server/perangkat, hubungan pesan, dan prosedur pengamatan konsisten.
- [ ] Parameter yang belum ditetapkan ditandai dengan PIC serta waktu tindak lanjut.
- [ ] Nicy mencatat pemeriksaan dan penyelesaian/tindak lanjut temuan.
- [ ] URL commit pelaporan tiap minggu sudah dicatat sesuai hasil yang diperiksa.

