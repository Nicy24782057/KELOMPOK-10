# Inventaris komponen prototipe

| Keterangan | Isi |
|---|---|
| Sprint dan minggu | S02, Minggu 4 |
| Tugas | W04-T03 — Pemeriksaan komponen |
| PIC | Ramdhani |
| Tanggal acuan pemeriksaan | 9 November 2026, berdasarkan [commit inventaris Dhani `87b3443`](https://github.com/Nicy24782057/KELOMPOK-10/commit/87b3443978af21637ef2c93f43c1a5001c7e4d7b). |
| Status | Ketersediaan komponen untuk uji dasar tercatat berdasarkan daftar Dhani dan konfirmasi tim. |

## Daftar komponen

Jumlah dan spesifikasi acuan mengikuti Tabel 4.9 proposal dan [SRS §5.1](https://github.com/Nicy24782057/KELOMPOK-10/blob/main/docs/perencanaan/srs.md#L259-L271). Ukuran LED acuan mengikuti RAB pada Tabel 2.3 proposal. Daftar komponen dan hasil uji nyala berasal dari konfirmasi tim pada 28 November 2026. Tanggal pelaksanaan uji fisik belum tercatat.

| Komponen | Spesifikasi rancangan | Jumlah acuan | Jumlah tersedia | Tipe dan kondisi aktual | Kekurangan dan tindak lanjut |
|---|---|---:|---|---|---|
| ESP32 | ESP32-DevKitC V4 dengan ESP32-WROOM-32D | 1 unit | 1 unit | Tim mengonfirmasi tipe sesuai proposal. Papan menjalankan kode uji nyala LED. | — |
| LED merah | LED merah 5 mm | 3 buah | 3 buah | Ketiganya berhasil menyala saat uji. | — |
| LED kuning | LED kuning 5 mm | 3 buah | 3 buah | Ketiganya berhasil menyala saat uji. | — |
| LED hijau | LED hijau 5 mm | 3 buah | 3 buah | Ketiganya berhasil menyala saat uji. | — |
| Resistor | 330 Ω, ¼ W | 9 buah | 9 buah | Nominal 330 Ω sesuai konfirmasi tim. | Daya nominal aktual belum dicatat. |
| OLED | SSD1306 I²C, 0,96 inci, 128 × 64 piksel, mendukung suplai 3,3 V | 1 unit | 1 unit | OLED I²C 0,96 inci tercantum dalam daftar Dhani. | Uji tampilan dan catat tipe modul di S03. |
| Breadboard | 830 titik | 1 buah | Tersedia | Tim mengonfirmasi breadboard tersedia untuk prototipe. | Ukuran aktual belum dicatat. |
| Kabel jumper | Female-to-male dan male-to-male | 40 buah per jenis | Secukupnya | Tersedia sesuai daftar Dhani. | Jumlah per jenis belum dirinci. |
| Kabel USB data | Konektor sesuai papan ESP32 | 1 buah | 1 buah digunakan | Menghubungkan ESP32 ke laptop dan memasok daya saat uji. | — |
| Adaptor USB | Keluaran 5 V DC, 2 A | 1 unit | Belum dikonfirmasi | Daya uji awal berasal dari port USB laptop. | Konfirmasi adaptor saat menyiapkan catu daya mandiri. |

## Tindak lanjut pemeriksaan

Ikrom memakai catatan ini untuk [rekap kesiapan](../../evidence/S02/README.md#minggu-4) dan [log aktivitas S02](../../evidence/S02/log-aktivitas.md). Pemeriksaan urutan fase, interval transisi, dan keluaran OLED dicatat saat uji prototipe dasar di S03.

Pada Sprint 3, cocokkan pemetaan GPIO dari kode uji Dhani dengan firmware yang diunggah ke ESP32 dan sambungan fisik. Catat komponen yang terpasang, sambungan, serta perubahan rangkaian di `docs/perangkat/perakitan.md`. [Kanban S03 #21](https://github.com/Nicy24782057/KELOMPOK-10/issues/21)

Acuan tugas [S02 #20, W04-T03](https://github.com/Nicy24782057/KELOMPOK-10/issues/20) dan [rancangan rangkaian ESP32](https://github.com/Nicy24782057/KELOMPOK-10/blob/main/docs/perangkat/perakitan.md).
