# LLD backend, konfigurasi kendali, dan kontrak MQTT

| Identitas | Nilai |
|---|---|
| Tim / sprint / minggu | KELOMPOK-10 / S01 / 3 |
| Tugas / PIC | W03-T02, W03-T03 / Putu Radit Ardika |
| Versi / tanggal | 0.1 / 29 Oktober 2026 |
| Status | Kontrak dan contoh lengkap untuk review; belum diuji publish/subscribe atau perangkat |
| Lokasi | `KELOMPOK-10/docs/operasional/konfigurasi-backend-dan-mqtt.md` |

## 1. Acuan dan batas antarmuka

Acuan: proposal sempro `FINAL INI A(1).docx` Subbab 5.2.2–5.2.3/Tabel 5.5–5.6, SRS KF-05–KF-11, dan HLD Bagian 4.2–4.4. AI/pembaca CCTV dan backend berjalan pada host Ubuntu; Mosquitto, Node-RED, dan InfluxDB memakai Docker di server yang sama. Pengukuran AI diserahkan ke backend melalui antarmuka internal; MQTT measurement adalah salinan metadata untuk pencatatan. Frame/video tidak masuk payload MQTT.

Keputusan LLD baru: JSON `schema_version` 1.0, QoS 1 dan retain false untuk kelima jenis pesan, ID/event tambahan untuk penelusuran, serta satu kandidat pertama yang sah per giliran. Kebutuhan sumber mewajibkan QoS 1 plan/ACK dan retain false plan; pilihan pesan lain di sini menjadi acuan implementasi yang perlu diverifikasi.

Dasar protokol: [MQTT 3.1.1 OASIS](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html) §3.3 dan §4.3; QoS 1 dapat menghasilkan duplikasi, sehingga deduplikasi aplikasi tetap diperlukan. [Panduan Mosquitto](https://mosquitto.org/man/mosquitto-conf-5.html) menjadi acuan pengaturan autentikasi dan listener TLS. Diakses 29 Oktober 2026.

## 2. Topik, penerbit, pelanggan, dan pengiriman

`controller_id` pada topik wajib sama dengan payload. Nama tidak memuat slash/wildcard. Contoh pengendali adalah `esp32-01`.

| Jenis / topik | Penerbit | Pelanggan / penggunaan | QoS / retain |
|---|---|---|---|
| `traffic/{controller_id}/trigger` | ESP32 | Backend; Node-RED salinan peristiwa | 1 / false |
| `traffic/{controller_id}/measurement` | Backend setelah hasil internal AI | Node-RED; bukan input kedua backend | 1 / false |
| `traffic/{controller_id}/plan` | Backend | ESP32; Node-RED salinan | 1 / false |
| `traffic/{controller_id}/ack` | ESP32 | Backend dan Node-RED | 1 / false |
| `traffic/{controller_id}/status` | ESP32 | Backend dan Node-RED | 1 / false |

QoS publikasi dan QoS langganan sama-sama 1. Jangan mengandalkan retained plan untuk startup. Sebelum operasi, hapus retained plan lama bila pernah terbit, lalu verifikasi pelanggan baru tidak menerima plan lama. PUBACK protokol MQTT hanya membuktikan penerimaan transport, sedangkan pesan ACK aplikasi menyatakan hasil validasi kandidat.

## 3. Envelope, identitas, versi, dan jam

Semua pesan adalah objek JSON UTF-8; angka harus finite, bukan NaN/Infinity. Field kritis yang hilang/salah tipe ditolak. Field tambahan nonkritis boleh diabaikan pada schema 1.0; perubahan makna field membutuhkan revisi kontrak. Bool tidak diterima sebagai angka. Timestamp memakai RFC3339 dengan offset atau `Z`, atau null bila jam UTC tidak diketahui sesuai ketentuan berikut.

| Field umum | Tipe / aturan |
|---|---|
| `schema_version` | String `1.0`; versi mayor yang tidak didukung ditolak |
| `message_type` | `trigger`, `measurement`, `plan`, `ack`, atau `status`, cocok topik |
| `example_only` | Bool wajib; true menandai fixture demonstrasi, ditolak oleh jalur kendali produksi |
| `event_id` | String unik per peristiwa dalam sesi; retransmisi peristiwa sama memakai ID dan isi sama |
| `event_ts` | Timestamp waktu peristiwa; ESP boleh null jika jam UTC belum tersedia. Ingest server menyimpan waktu penerimaan terpisah |
| `controller_id` | Pengendali yang terdaftar dan cocok ACL/topik |
| `session_id` | ID baru tiap boot, tidak digunakan ulang; reconnect jaringan mempertahankan sesi boot |
| `turn_id` | Integer positif; sasaran pada trigger/measurement/plan/ACK, giliran aktif pada status |
| `control_config_version` | String versi konfigurasi bersama yang kompatibel; berubah pada batas aman, tidak di tengah giliran |

`measurement_id` mengidentifikasi satu snapshot; `plan_id` mengidentifikasi satu rencana. `config_version` menelusuri sumber/ROI/panjang/lajur dan `parameter_version` menelusuri ambang/durasi hasil kalibrasi kamera terkait. `model_version` dan `inference_version` mencatat model/bobot/konfigurasi inferensi aktual. Hash/bukti asal versi dicatat saat implementasi.

Backend memakai status sesi aktif yang sudah terikat melalui koneksi/peristiwa startup ESP32. Sesi lama ditutup ketika boot baru pengendali terdaftar; jangan menerima kembali sesi lama hanya karena sebuah trigger lama muncul. Selama backend belum mengenali status sesi dan giliran, tunggu status baru; ESP32 tetap statis. Prosedur sinkronisasi/restart ini diuji pada integrasi. Status dikirim pada startup, transisi, dan koneksi ulang; interval berkala dipilih saat implementasi, tidak menjadi pengganti status transisi.

`response_ms` dihitung ESP32: waktu monotonic penerimaan plan valid dikurangi waktu pengiriman trigger terkait. Timestamp server/UTC hanya untuk penelusuran. `frame_source_ts` adalah waktu gambar dari sumber jika ada; `frame_received_ts` adalah waktu server menerima/mendekode frame. Keduanya tidak dipertukarkan. Buffer residence tidak membuktikan umur gambar di sumber.

## 4. Field per jenis pesan

### 4.1 Trigger

| Field tambahan | Tipe / arti |
|---|---|
| `current_phase`, `next_phase` | Enum A/B/C; next wajib penerus A→B→C→A |
| `current_turn_id` | Integer positif, giliran aktif; `turn_id = current_turn_id + 1` |
| `remaining_s` | Nilai pemicu 1 detik nominal |
| `esp_monotonic_ms` | Integer nonnegatif, saat trigger dikirim dalam sesi boot |

Kunci proses trigger `(controller_id, session_id, turn_id)`. Fase tujuan diturunkan dari pemetaan kendali yang disepakati, bukan alamat kamera dari payload. Trigger hanya meminta satu kamera fase berikutnya.

### 4.2 Measurement

| Field tambahan | Tipe / aturan |
|---|---|
| `measurement_id`, `camera_id`, `phase`, `frame_id` | String identitas; phase enum; frame_id boleh null bila tidak ada frame |
| `valid` | Bool; true hanya bila frame, konfigurasi dan seluruh perhitungan sah |
| `reason` | Null jika valid; kode nonkosong jika invalid |
| `vehicle_count` | Integer ≥0 jika valid; null jika invalid |
| `class_counts` | Objek car/motorcycle/bus/truck integer ≥0 jika valid; jumlah = vehicle_count; null jika invalid |
| `density_k`, `density_unit` | Angka ≥0 jika valid; null bila invalid. Unit selalu `kendaraan/km/lajur` |
| `length_m`, `lanes` | Panjang positif dan integer lajur positif; boleh null pada konfigurasi gagal |
| `frame_source_ts` | Timestamp sumber atau null |
| `frame_received_ts`, `frame_selected_ts` | Timestamp penerimaan dan pemilihan frame; null bila belum ada |
| `frame_age_basis`, `frame_age_ms`, `source_age_known` | Dasar umur yang dinilai, umur nonnegatif atau null, dan bool; tidak menyatakan waktu sumber tersedia bila tidak ada |
| `config_version`, `model_version`, `inference_version` | String versi terkait, atau null hanya jika gagal sebelum tersedia |

Valid nol menghasilkan count/k = 0, class_counts seluruhnya 0 dan reason null. Frame gagal tidak diberi 0. Kode invalid antara lain `frame_unavailable`, `decode_failed`, `frame_stale`, `frame_dimension_mismatch`, `invalid_camera_config`, `inference_failed`, `non_finite_result`.

Contoh invalid dapat dibentuk dari measurement normal: ubah `valid` menjadi false, `reason` menjadi `decode_failed`, `vehicle_count`, `class_counts`, `density_k`, `frame_id` menjadi null, serta waktu/versi hanya dipertahankan jika memang diketahui. Gunakan measurement/event ID baru untuk **kejadian berbeda**, bukan mengubah isi ID yang sudah diterbitkan.

### 4.3 Plan

| Field tambahan | Tipe / aturan |
|---|---|
| `plan_id`, `measurement_id`, `camera_id`, `phase` | Identitas pengukuran/sasaran; phase enum A/B/C |
| `vehicle_count`, `density_k`, `density_unit` | Nilai valid dari measurement terkait; wajib tersedia |
| `category` | Enum `rendah`, `sedang`, `tinggi` |
| `green_proposed_s`, `green_s` | Integer detik, usulan dan akhir setelah clamp; green_s harus dalam batas fase lokal |
| `config_version`, `parameter_version` | Versi konfigurasi pengamatan dan parameter yang telah dibekukan untuk sasaran |

Backend hanya mengirim plan adaptif dari pengukuran/parameter sah. Jika gagal, publikasi measurement invalid/catat alasan; jangan menerbitkan plan berisi hitungan nol pengganti. ESP32 memilih statis lokal saat lock, sehingga tidak memerlukan pesan plan statis dari server.

### 4.4 ACK aplikasi

| Field tambahan | Tipe / aturan |
|---|---|
| `plan_id`, `phase` | Rencana dan sasaran yang diperiksa; null hanya bila pesan rusak sehingga identitas tidak dapat diperoleh |
| `accepted` | Bool; true berarti kandidat diterima, belum berarti dilaksanakan |
| `reason` | Kode keputusan, selalu nonkosong |
| `response_ms` | Integer nonnegatif bila trigger terkait dikenal; selain itu null |
| `response_target_met` | Bool bila accepted dan response_ms tersedia; selain itu null |
| `esp_received_monotonic_ms` | Waktu plan pertama kali ditangani pada ESP32; null bila tidak diketahui |

Kode: `accepted_candidate`, `malformed_payload`, `schema_unsupported`, `example_payload`, `controller_mismatch`, `session_mismatch`, `turn_mismatch`, `phase_mismatch`, `config_mismatch`, `invalid_value`, `duration_out_of_bounds`, `turn_locked`, `plan_id_conflict`, `candidate_already_set`.

Untuk JSON yang sama sekali tidak dapat diparse, catat penolakan lokal dan terbitkan status/event diagnostik bila jalur tersedia. ACK diterbitkan hanya bila identitas yang cukup dapat diambil dengan aman; ID yang tidak diketahui tidak direka. ACK diterima pertama dipertahankan pada duplikasi identik, termasuk nilai response_ms awal.

### 4.5 Status

| Field tambahan | Tipe / aturan |
|---|---|
| `phase` | Fase aktif/yang baru berakhir, A/B/C; null saat startup sebelum fase pertama |
| `lamp_state` | `green`, `yellow`, `all_red`, atau `config_fault` |
| `remaining_s` | Integer ≥0 dari timer aktual; null pada config_fault yang tanpa deadline |
| `mode` | `adaptive` atau `static`; null hanya startup/fault sebelum keputusan fase tersedia |
| `event` | Misalnya `startup`, `green_started`, `yellow_started`, `turn_locked`, `all_red_started`, `reconnected`, `config_fault` |
| `plan_id`, `measurement_id` | Rencana/pengukuran yang digunakan giliran aktif; null untuk statis tanpa plan |
| `esp_monotonic_ms` | Waktu lokal peristiwa |
| `vehicle_count`, `density_k`, `category` | Data plan aktif; null bila tidak tersedia. Unit tetap eksplisit |
| `config_version`, `parameter_version` | Versi plan aktif; null pada statis tanpa pengukuran |

Startup memakai turn_id 0 sebagai **pengecualian status saja** sebelum giliran pertama. Pada all_red, turn_id/phase masih giliran sebelumnya, plan_id/data masih miliknya; kandidat berikutnya belum dinyatakan terlaksana. Event `turn_locked` boleh menambah `locked_next_turn_id`, `locked_next_phase`, `locked_mode`, `locked_plan_id`. Pada `green_started`, turn_id/phase maju dan data plan berganti. Status statis menyertakan `local_static_config_version` sebagai field tambahan untuk menelusuri durasi lokal.

## 5. Validasi, duplikasi, dan kandidat

Urutan backend: parse/envelope/topik/ACL → sesi/giliran/next_phase → kunci deduplikasi → copy frame → validasi/inferensi sekali → hitung k → pilih parameter kamera → kategori/durasi → simpan hasil penanganan → kirim plan → kirim salinan log secara independen.

| Kondisi | Tindakan |
|---|---|
| Trigger baru sah | Tandai processing secara atomik; jalankan satu pengukuran |
| Trigger sama sedang processing | Tidak menjalankan AI kedua; tunggu hasil proses awal tanpa memblokir timer ESP32 |
| Trigger sama sudah selesai | Kirim ulang plan identik jika ada; jika hasil gagal, pakai hasil gagal yang sama tanpa inferensi baru |
| Trigger ID sama tetapi fase/isi kritis berbeda | Tolak konflik; jangan ganti kamera/hasil |
| Plan identik pernah ditangani | ACK awal digunakan kembali; timer, kandidat dan lock tetap |
| plan_id sama dengan isi berbeda | Tolak `plan_id_conflict` |
| Plan ID lain untuk giliran yang sudah punya kandidat sah | Tolak `candidate_already_set`; kebijakan satu rencana per trigger |
| Plan baru pada/sesudah lock | Tolak `turn_locked`; jangan memotong atau mengubah giliran |
| Plan sah >3000 ms tetapi sebelum lock aktual | Terima kandidat, response_target_met false |
| Tidak ada kandidat saat lock | Pilih statis lokal sah; status mode static |

ESP32 memeriksa identitas sesi/giliran/phase, versi kompatibel, kelengkapan/tipe, integer durasi/batas lokal, count/k/kategori sah, serta status lock sebelum menerima kandidat. Ia tidak menghitung ulang kepadatan dari video. Konflik versi pengamatan/parameter dihindari melalui konfigurasi yang telah diselaraskan sebelum operasi.

Simpan deduplikasi untuk seluruh giliran pending/aktif dan hasil yang masih mungkin diulang. Pesan giliran yang sudah lewat ditolak berdasarkan counter meskipun cache rinci telah dibersihkan. Restart backend tidak boleh membuat inferensi/rencana berbeda untuk trigger yang sudah selesai: gunakan cache hasil persisten atau rekonsiliasi status, dan bila tidak dapat dipastikan hentikan penerbitan ulang untuk giliran tersebut sampai status baru. Pengendalian tetap memakai kandidat/statis yang telah sah. Deduplikasi ACK/peristiwa logging menggunakan event_id; jangan menyamakan ACK diterima dengan status green_started.

## 6. Waktu dan contoh normal

Kelima JSON pada `KELOMPOK-10/configs/mqtt/` adalah fixture satu rantai demonstrasi untuk giliran 42 fase B. Seluruh timestamp dan nilai merupakan data buatan untuk memeriksa format, bukan log pengujian.

| Waktu contoh WIB | Peristiwa | Waktu monotonic ESP |
|---|---|---|
| 15:00:00.000 | Trigger dari A/giliran 41 untuk B/giliran 42 | 100000 ms |
| 15:00:00.020 | Server menyalin frame B yang diterima 14:59:59.900 | — |
| 15:00:01.100 | Measurement 6 kendaraan, k=30 | — |
| 15:00:01.400 | Plan kategori sedang, 20 detik | — |
| 15:00:01.800 | ESP32 menerima kandidat dan membuat ACK | 101800 ms, response=1800 ms |
| Sekitar 15:00:04.000 | Lock B, lalu merah bersama 1 detik | Sekitar 104000 ms |
| Sekitar 15:00:05.000 | B mulai hijau, status remaining_s 20 | 105000 ms |

Server/UTC contoh diselaraskan untuk mudah dibaca; pengukuran respons tetap selisih jam ESP. Plan yang diterima misalnya 3500 ms dapat lulus fungsi kandidat sebelum lock tetapi gagal target respons. Plan baru yang diterima setelah lock tidak dapat digunakan meski timestamp/TTL server tampak belum habis. Tidak ada TTL 60 detik yang mengalahkan batas lock.

## 7. Struktur konfigurasi dan penetapan parameter

`KELOMPOK-10/configs/control.example.json` memuat controller, urutan fase, timing, transport, pemetaan kamera/versi, ambang, dasar/tambahan, batas, statis, dan asal kalibrasi. `runtime_enabled: false`, `example_only: true`, `parameter_status: example_unverified`, serta `static_verified: false` menegaskan berkas belum layak operasi.

| Bagian | Aturan |
|---|---|
| phase_order / phases | Tepat A/B/C; satu kamera per fase, tidak ambigu |
| timing | Pemicu 1 detik, respons 3000 ms, kuning 3 detik, merah bersama 1 detik, lock sebelum merah bersama |
| observation_example | Struktur demo L/lajur/umur buffer, bukan pengganti konfigurasi ROI aktual minggu 6 |
| thresholds | `0 < k1 < k2`, finite; satuan kendaraan/km/lajur; tiap kamera punya hasil kalibrasi sendiri |
| green.base_s / add_s | g_usulan = base + tambahan; tambahan rendah 0; sedang/tinggi ≥0 dan tidak menurun |
| green.category_s | Nilai materialisasi `base_s + add_s` untuk audit; validator menolak ketidakcocokan, bukan memilih dua sumber berbeda |
| green.min_s / max_s | Integer positif, min ≤ max, cukup untuk pemicu; nilai min/max menunggu penetapan dan uji |
| green.static_s | Integer dalam batas; diverifikasi lokal sebelum operasi dan diarsipkan versinya |
| calibration | Dataset/report, tiga pusat, ukuran kelompok, setting K-means dan cakupan final; null berarti belum ada hasil |
| timing_tolerance_ms | Null sekarang; metode dan toleransi diisi sebelum uji timing oleh Ramdhani/Ikrom |

Untuk contoh B, N=6, L=100 m, lajur=2 memberi k=30, kategori sedang karena 20≤30<40, g_usulan=10+10=20, dan clamp(20,5,40)=20. Nilai sama dipakai semua kamera pada fixture hanya agar pembaca dapat mengikuti format, bukan hasil kalibrasi tiga lokasi.

Kalibrasi offline: masukan manual per kamera → K-means 1D tiga kelompok tidak kosong dengan pusat berbeda/terurut → titik tengah K1/K2 → kategori manual → layanan kelompok awal → kandidat P90/coverage → susun durasi tidak menurun → base/tambahan → clamp → cek ulang cakupan ≥90% per kamera/kategori → bekukan versi. Tidak ada K-means pada setiap pemicu. Parameter belum tervalidasi menghentikan pembentukan plan adaptif, sementara ESP32 dapat beroperasi statis bila statis lokal telah sah.

## 8. Autentikasi, TLS, dan penempatan rahasia

Rancang listener TLS (contoh port 8883), sertifikat server dengan hostname sesuai, CA dipercaya klien, verifikasi sertifikat/hostname aktif, serta akun pengguna berbeda untuk ESP32, backend, dan pencatatan. `allow_anonymous false`. Pilihan LLD: autentikasi username/password di dalam TLS; mTLS bukan syarat tambahan saat ini. Jangan memakai mode TLS tanpa verifikasi. Jam perangkat untuk validasi sertifikat disiapkan saat startup; jika koneksi belum dapat dipercaya, timer tetap statis lokal.

| Akun | Publish yang diizinkan | Subscribe yang diizinkan |
|---|---|---|
| ESP32 pengendali | trigger, ack, status miliknya | plan miliknya |
| Backend | measurement, plan | trigger, ack, status pengendali terdaftar |
| Node-RED pencatatan | Tidak perlu menerbitkan kendali | Lima topik peristiwa pengendali yang dikelola |

Username/password, private key dan token InfluxDB disimpan pada lingkungan/berkas privat yang dikecualikan dari Git; contoh hanya memuat nama variabel. CA publik boleh didistribusikan sesuai rancangan, private key server tidak. Detail compose, mosquitto.conf, sertifikat, volume, ACL dan `.env.example` dikerjakan minggu 4; kontrak ini menetapkan perilakunya.

## 9. Pencatatan dan kegagalan layanan

Kelompok data mengikuti Tabel 5.6 proposal: `traffic_measurement`, `traffic_plan`, `controller_event`, `traffic_execution`. ID kamera/phase/controller dapat menjadi tag; ID unik seperti plan_id/event_id, nilai, alasan dan versi menjadi field agar cardinality terkendali sesuai versi InfluxDB yang dipilih. Peristiwa status/pemicu/ACK dihubungkan dengan ID dan waktu. Rancangan deduplikasi log harus mempertahankan satu record per event_id tanpa menimpa peristiwa berbeda yang timestamp-nya sama; identitas storage/precision diputuskan dan diuji saat implementasi.

InfluxDB tidak menyimpan field null sebagai nilai numerik: tulis valid=false/reason dan hilangkan field count/k pada point invalid. Volume persisten diuji melalui restart. Jalur log menggunakan antrean/penanganan gagal terpisah sehingga kegagalan log tidak menunggu/menunda plan atau timer. Pesan hilang selama log mati dicatat sebagai gap; replay penuh belum dijanjikan tanpa implementasi/bukti. Masa simpan, versi InfluxDB, batas antrean dan interval status diputuskan minggu 4/integrasi, kemudian dicatat sebelum uji terkait.

## 10. Pemeriksaan sebelum implementasi

- Enam JSON dapat diparse dan cross-reference sesi/giliran/kamera/versi konsisten.
- UJI-09–UJI-11 memeriksa aritmetika dan batas; UJI-13–UJI-19 memeriksa respons/lock/duplikasi/fallback.
- UJI-21–UJI-26 memeriksa trace, persistensi, independensi, beban dan autentikasi/TLS.
- Hasil pemeriksaan format pada paket minggu 3 hanya bukti berkas; keberhasilan runtime dan perangkat dibuktikan pada tahap berikutnya.
