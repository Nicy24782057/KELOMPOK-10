## Minggu 2

**Fokus:** HLD satu server, pembagian fungsi komponen, alur data, dan pengendalian.  
**Tanggal penyusunan paket lengkap:** 29 Oktober 2026.  
**Status hasil:** Review — isi seluruh tugas W02-T01–W02-T05 tersedia dan sudah tergabung.

### Ringkasan hasil seluruh anggota

| ID tugas | PIC | Hasil yang tersedia | Lokasi berkas/bagian | Status | Tindak lanjut |
|---|---|---|---|---|---|
| W02-T01 | Nicy | Arsitektur keseluruhan tiga CCTV, satu server, ESP32, lampu/OLED; pembagian host/Docker, fungsi/antarmuka/data, kondisi gagal, serta HLD gabungan. | `KELOMPOK-10/docs/perencanaan/hld.md` — Bagian 3 dan penyatuan dokumen. | Review | Memeriksa kesesuaian seluruh bagian dan mencatat Review PM. |
| W02-T02 | Rizky | Diagram CCTV/AI, tabel masukan/proses/keluaran, pemilihan frame, validasi, YOLO, hitungan ROI, kepadatan, metadata, serta hubungan backend/manual. | `KELOMPOK-10/docs/perencanaan/hld.md` — Bagian 4.1. | Review | Memeriksa bagian bidang AI; rincian prosedur/konfigurasi dilanjutkan pada minggu 3 dan implementasi. |
| W02-T03 | Putu | Diagram pertukaran MQTT, masukan/keluaran backend, kalibrasi offline versus operasi, aturan kategori/durasi, jenis pesan, validasi, duplikasi, dan keterlambatan. | `KELOMPOK-10/docs/perencanaan/hld.md` — Bagian 4.2. | Review | Memeriksa antarmuka AI–backend–ESP32; kontrak field/topic dirinci pada minggu 3. |
| W02-T04 | Ramdhani | Diagram blok perangkat, fungsi ESP32/LED/OLED, urutan keadaan, waktu nominal, lock, statis, duplikasi, dan pemulihan. | `KELOMPOK-10/docs/perencanaan/hld.md` — Bagian 4.3. | Review | Memeriksa kesesuaian perangkat; sambungan/pin dan toleransi diperinci sebelum perakitan/pengujian. |
| W02-T05 | Ikrom | Diagram Node-RED/InfluxDB, kelompok data, keterkaitan identitas/waktu, persistensi, penolakan data rusak, independensi kendali, serta rujukan dataset/bukti. | `KELOMPOK-10/docs/perencanaan/hld.md` — Bagian 4.4. | Review | Memeriksa keterlacakan pesan dan data; skema/template/rencana uji dirinci pada minggu 3. |

Seluruh bagian disusun dalam paket dokumen berdasarkan proposal sempro/SRS. PIC menunjukkan tanggung jawab bidang; status Review tidak menyatakan bahwa masing-masing anggota telah melakukan pemeriksaan mandiri atau bahwa implementasi sudah diuji.

### Hasil dan lokasi berkas minggu 2

| Path lengkap | Fungsi | PIC |
|---|---|---|
| `KELOMPOK-10/docs/perencanaan/hld.md` | HLD lengkap seluruh anggota, dengan lima diagram: arsitektur, CCTV/AI, komunikasi, perangkat, dan pencatatan. | Nicy mengoordinasikan; seluruh PIC pada bagiannya. |
| `KELOMPOK-10/evidence/S01/README.md` | Ringkasan semua tugas, lokasi hasil, tindak lanjut, Review PM, dan URL commit pelaporan. | Nicy. |
| `KELOMPOK-10/evidence/S01/log-aktivitas.md` | Rekap penyusunan paket lengkap menurut PIC dan kegiatan pelaporan. | PIC sesuai pembagian; Nicy mengoordinasikan. |

**Lokasi HLD:** `KELOMPOK-10/docs/perencanaan/hld.md`.

### Pemeriksaan konsistensi isi dan tindak lanjut

- AI/backend berada pada host Ubuntu; Mosquitto, Node-RED, dan InfluxDB pada Docker di server yang sama.
- AI menyediakan hitungan/kepadatan; backend menentukan kategori/durasi dari parameter tersimpan; ESP32 melakukan lock dan menjalankan timer/lampu/OLED serta statis lokal.
- Video menggunakan koneksi CCTV; pesan/metadata menggunakan antarmuka aplikasi dan MQTT sesuai kontrak. ACK penerimaan dibedakan dari pelaksanaan.
- Target respons tiga detik dibedakan dari lock sebelum merah bersama. Kegagalan pencatatan tidak menjadi penghambat pergantian lampu.
- Model tetap ditulis YOLO tanpa menetapkan varian baru; parameter kalibrasi dan rincian LLD yang belum ditetapkan tetap mengikuti SRS/matriks serta tahapnya.

Kelengkapan isi HLD telah disusun. Nicy mencatat penerimaan/temuan Review PM; pemilik bidang menindaklanjuti penjelasan teknis sesuai hasil review. Penyelesaian dokumen minggu 2 tidak mensyaratkan pengadaan alat atau hasil kalibrasi yang memang dijadwalkan kemudian.

### Review PM

- Pemeriksa: **Nicy Putra Pratama**.
- Tanggal pemeriksaan aktual: [Diisi saat Review PM dilakukan].
- Status: **Isi seluruh bidang tersedia; penerimaan PM belum dicatat**.
- Hasil yang diterima dan temuan: [Diisi berdasarkan pemeriksaan HLD lengkap].
- PIC tindak lanjut: Nicy mengoordinasikan; Rizky/Putu/Ramdhani/Ikrom menindaklanjuti sesuai bidang bila ada temuan.
- Status akhir: [Belum diperiksa / Perlu perbaikan / Diterima].

### Pengumpulan dan commit minggu 2

Cakupan commit adalah HLD lengkap beserta README dan log aktivitas yang diperbarui. Jika pekerjaan anggota dicatat terpisah, gunakan format konsisten berikut sesuai perubahan yang benar-benar dimasukkan:

| PIC | Contoh pesan commit pekerjaan |
|---|---|
| Nicy | `S01-W02: susun arsitektur keseluruhan sistem` |
| Rizky | `S01-W02: susun alur CCTV dan AI` |
| Putu | `S01-W02: susun alur backend dan MQTT` |
| Ramdhani | `S01-W02: susun diagram blok perangkat ESP32` |
| Ikrom | `S01-W02: susun alur pencatatan Node-RED dan InfluxDB` |

Pesan commit pelaporan gabungan:

```text
S01-W02: susun HLD sistem
```

**Commit pelaporan minggu 2:** [Tempel URL commit GitHub setelah di-push dan diperiksa].  
**Tempat pencatatan:** `KELOMPOK-10/evidence/S01/README.md`, bagian Minggu 2.

### Checklist minggu 2

- [x] W02-T01: arsitektur keseluruhan dan penyatuan HLD tersedia.
- [x] W02-T02: bagian CCTV dan AI tersedia.
- [x] W02-T03: bagian backend dan komunikasi tersedia.
- [x] W02-T04: bagian perangkat tersedia.
- [x] W02-T05: bagian pencatatan data tersedia.
- [x] Seluruh bagian berada pada satu berkas dan mengikuti batas fungsi proposal/SRS.
- [x] Ringkasan hasil dan log penyusunan paket diperbarui.
- [ ] Nicy telah mencatat penerimaan/temuan Review PM.
- [ ] Perubahan telah di-push dan URL commit pelaporan minggu 2 dicatat.


