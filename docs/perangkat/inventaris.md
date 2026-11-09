# Inventaris komponen prototipe

| Keterangan | Isi |
|---|---|
| Sprint dan minggu | S02, Minggu 4 |
| Tugas | W04-T03 — Pemeriksaan komponen |
| PIC | Ramdhani |
| Tanggal pemeriksaan | Belum dicatat |
| Status | Acuan rancangan tersedia. Hasil pemeriksaan aktual belum dicatat. |

## Daftar komponen

Jumlah dan spesifikasi acuan mengikuti Tabel 4.9 proposal dan [SRS §5.1](https://github.com/Nicy24782057/KELOMPOK-10/blob/main/docs/perencanaan/srs.md#L259-L271). Ukuran LED mengikuti RAB pada Tabel 2.3 proposal. Tanda `—` menunjukkan hasil pemeriksaan belum dicatat.

| Komponen | Spesifikasi rancangan | Jumlah acuan | Jumlah tersedia | Tipe dan kondisi aktual | Kekurangan dan tindak lanjut |
|---|---|---:|---|---|---|
| ESP32 | ESP32-DevKitC V4 dengan ESP32-WROOM-32D | 1 unit | — | — | — |
| LED merah | LED merah 5 mm | 3 buah | — | — | — |
| LED kuning | LED kuning 5 mm | 3 buah | — | — | — |
| LED hijau | LED hijau 5 mm | 3 buah | — | — | — |
| Resistor | 330 Ω, ¼ W | 9 buah | — | — | — |
| OLED | SSD1306 I²C, 0,96 inci, 128 × 64 piksel, mendukung suplai 3,3 V | 1 unit | — | — | — |
| Breadboard | 830 titik | 1 buah | — | — | — |
| Kabel jumper | Female-to-male | 40 buah | — | — | — |
| Kabel jumper | Male-to-male | 40 buah | — | — | — |
| Kabel USB data | Konektor sesuai papan ESP32 | 1 buah | — | — | — |
| Adaptor USB | Keluaran 5 V DC, 2 A | 1 unit | — | — | — |

## Pemeriksaan sebelum perakitan — Sprint 2

- Isi tanggal pemeriksaan dan jumlah komponen yang tersedia sebelum perakitan.
- Catat tipe komponen yang diperiksa dan kondisinya. Jika baru diperiksa secara visual, gunakan keterangan seperti `fisik baik, fungsi belum diuji`.
- Catat komponen yang kurang, bermasalah, atau berbeda spesifikasi beserta tindakan yang diperlukan sebelum perakitan. Rangkaian acuan memakai satu resistor seri untuk setiap LED.
- Tambahkan kegiatan yang sudah dilakukan ke `evidence/S02/log-aktivitas.md`. Ringkasan kesiapan untuk Ikrom menggunakan hasil aktual pada inventaris ini.

Pada Sprint 3, inventaris ini menjadi acuan perakitan. Catat komponen yang terpasang, sambungan, dan perubahan rangkaian di `docs/perangkat/perakitan.md`. [Kanban S03 #21](https://github.com/Nicy24782057/KELOMPOK-10/issues/21)

Acuan tugas [S02 #20, W04-T03](https://github.com/Nicy24782057/KELOMPOK-10/issues/20) dan [rancangan rangkaian ESP32](https://github.com/Nicy24782057/KELOMPOK-10/blob/main/docs/perangkat/perakitan.md).
