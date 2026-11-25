# Lingkungan server dan layanan pendukung

| Keterangan | Nilai |
|---|---|
| Versi dan tanggal | 0.2 / 25 November 2026 |
| Lingkungan yang tercatat pada bukti S02 | Windows 11, Ubuntu WSL2, Docker Desktop |
| Target implementasi | Satu server Ubuntu/GPU mengikuti SRS; diperiksa pada lingkungan aktual |
| Status panduan | Perintah dan lokasi konfigurasi diselaraskan; layanan tidak dijalankan ulang dalam penyusunan paket |

## Acuan bukti dan batasnya

[Laporan S02](../evidence/S02/status-layanan.txt) mencatat Mosquitto, Node-RED dan InfluxDB berjalan secara lokal; publish/subscribe pada 1883 dan TLS pada 8883 berhasil. Versi Docker/Compose lengkap, hasil pada server target, dan kelengkapan konfigurasi lokal tetap dicatat oleh pelaksana. Akses Node-RED/InfluxDB belum menjadi bukti flow pencatatan atau integrasi AI–ESP32 tersedia.

AI dan backend berjalan pada host. Mosquitto, Node-RED, dan InfluxDB dijalankan melalui infra/compose.yaml. Contoh konfigurasi rahasia ada pada .env.example dan diisi pada .env lokal.

## Persiapan dari root repositori

Perintah berikut dijalankan pada shell Linux/WSL dari folder KELOMPOK-10.

```bash
cp .env.example .env
mkdir -p infra/mosquitto/certs
```

Isi nilai kosong pada .env. MQTT_USERNAME/MQTT_PASSWORD dipakai ketika membuat passwordfile dan menguji klien; Mosquitto membaca passwordfile, bukan variabel .env secara otomatis. NODE_RED_CREDENTIAL_SECRET melindungi kredensial flow dan tidak menggantikan pengaturan login editor Node-RED.

Sediakan berkas lokal berikut sesuai identitas host layanan:

| Berkas | Pemakaian |
|---|---|
| infra/mosquitto/config/passwordfile | Database pengguna Mosquitto |
| infra/mosquitto/certs/ca.crt | CA yang dipercaya klien |
| infra/mosquitto/certs/server.crt | Sertifikat server untuk hostname yang diakses klien |
| infra/mosquitto/certs/server.key | Kunci privat server |

Konfigurasi tersebut tidak disertakan dalam ZIP. Putu menyiapkan sertifikat/izin baca sesuai lingkungan dan menyimpan kredensial di luar berkas publik. Klien menggunakan verifikasi CA serta hostname sesuai kontrak. Identitas host dan cara penerbitan sertifikat dicatat pada pelaksanaan.

Untuk membuat file pengguna pada pemasangan baru, isi nama pengguna yang sesuai .env pada perintah berikut. Password diminta secara interaktif oleh mosquitto_passwd.

```bash
docker run --rm -it --mount "type=bind,source=$PWD/infra/mosquitto/config,target=/mosquitto/config" eclipse-mosquitto:2 mosquitto_passwd -c /mosquitto/config/passwordfile kelompok10
```

Opsi -c membuat database baru dan digunakan pada pembuatan awal. Untuk menambahkan pengguna pada database yang sudah ada, jalankan perintah yang sama tanpa -c. Periksa pengguna sebelum mengubah file yang telah digunakan oleh tim.

## Pemeriksaan dan menjalankan layanan

```bash
docker --version
docker compose version
docker compose --env-file .env -f infra/compose.yaml config --quiet
docker compose --env-file .env -f infra/compose.yaml up -d
docker compose --env-file .env -f infra/compose.yaml ps
docker compose --env-file .env -f infra/compose.yaml logs --tail 100
```

--env-file menunjuk .env pada root, sedangkan -f menunjuk Compose dalam infra/. Bind mount ./mosquitto/... dalam Compose relatif terhadap folder infra. config --quiet memeriksa konfigurasi tanpa mencetak hasil interpolasi nilai rahasia. Port Node-RED/InfluxDB pada host mengikuti .env; antarkontainer memakai hostname mosquitto, nodered, dan influxdb pada jaringan backend.

| Layanan | Alamat host default |
|---|---|
| MQTT uji lokal | localhost:1883, autentikasi wajib |
| MQTT operasional TLS | Host layanan:8883 dengan CA dan hostname yang sesuai |
| Node-RED | http://localhost:1880 |
| InfluxDB | http://localhost:8086 |

Port 1883 disediakan untuk pemeriksaan lokal pada rancangan S02. Jalur pengendalian operasional mengikuti TLS pada 8883 sesuai SRS/kontrak.

Untuk menghentikan layanan dan mempertahankan volume data:

```bash
docker compose --env-file .env -f infra/compose.yaml down
```

Data layanan memakai volume mosquitto_data, nodered_data, influxdb_data, dan influxdb_config. Setelah setup awal InfluxDB, perubahan kredensial pada .env tidak otomatis menulis ulang akun yang tersimpan dalam volume; perubahan pada instalasi yang sudah berisi data ditangani melalui administrasi layanan.

## Pemeriksaan pada lingkungan pelaksana

| Pemeriksaan | Bukti terdahulu | Yang dicatat saat pelaksanaan berikutnya |
|---|---|---|
| Layanan berjalan dan dapat diakses | Dilaporkan berhasil lokal pada S02 | Versi Docker/Compose, tanggal, host, status/log aktual |
| MQTT autentikasi/TLS | Dilaporkan berhasil lokal pada S02 | Identitas host/CA, hasil klien sah dan penolakan kredensial tidak sah |
| Persistensi | Konfigurasi volume tersedia | Data uji tetap ada setelah layanan dijalankan ulang |
| AI/ESP32/flow pencatatan | Belum dibuktikan oleh laporan layanan | Bukti integrasi pada sprint terkait |
| Server Ubuntu/GPU target | Belum diverifikasi pada bukti ini | Versi, kapasitas, lingkungan dan hasil beban aktual |

Simpan keluaran aktual pada evidence/S02/ atau bukti sprint pelaksanaan berikutnya. Riwayat laporan lama dipertahankan.
