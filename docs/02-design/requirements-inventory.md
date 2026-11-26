# Requirements Inventory

## 1. Identitas Dokumen

| Keterangan              | Detail                                      |
| ----------------------- | ------------------------------------------- |
| Nama Proyek             | Testing & QA Kelompok 4                     |
| System Under Test (SUT) | Wave Projects Center.ID                     |
| Nama Penulis            | Fiyado Yudha Witama                         |
| NIM                     | 231011402181                                |
| Role                    | Domain Expert                               |
| Hari                    | D02                                         |
| Pertemuan               | P2                                          |
| Versi Dokumen           | 1.0                                         |
| Status                  | Draft - Menunggu Review                     |
| Reviewer                | Fitrah G. Ripan                             |
| Standar Acuan           | ISO/IEC/IEEE 29119-5:2024                   |
| URL SUT                 | https://wave-projects-center-id.vercel.app/ |

## 2. Pendahuluan

Wave Projects Center.ID merupakan platform berbasis web yang menyediakan layanan konsultasi teknologi, informasi layanan pengembangan website dan aplikasi, pemilihan paket, serta pemesanan proyek secara digital.

Dokumen Requirements Inventory disusun untuk mengidentifikasi kebutuhan sistem berdasarkan observasi antarmuka aplikasi dan alur bisnis yang tersedia. Hasil identifikasi digunakan sebagai dasar dalam perancangan skenario pengujian, test case, dan keyword-driven testing.

## 3. Tujuan

- Mengidentifikasi fitur utama pada sistem.
- Mengidentifikasi aktor yang berinteraksi dengan sistem.
- Mendokumentasikan kebutuhan fungsional dan nonfungsional.
- Menyusun User Story berdasarkan kebutuhan pengguna.
- Menentukan Acceptance Criteria untuk setiap kebutuhan.
- Menentukan prioritas pengujian.
- Mendukung keterlacakan antara requirement dan test case.

## 4. Ruang Lingkup

Ruang lingkup analisis meliputi:

1. Halaman utama.
2. Navigasi website.
3. Portofolio.
4. Informasi layanan.
5. Pemilihan paket.
6. Konsultasi AI.
7. Checkout pemesanan.
8. Validasi formulir pemesanan.
9. Autentikasi pengguna.
10. Pembayaran dan portal internal sebagai kebutuhan yang masih memerlukan konfirmasi.

## 5. Identifikasi Aktor

| ID     | Aktor         | Deskripsi                                                   | Status           |
| ------ | ------------- | ----------------------------------------------------------- | ---------------- |
| ACT-01 | Visitor       | Pengunjung yang mengakses informasi website.                | Terobservasi     |
| ACT-02 | Customer      | Pengguna yang memilih paket dan melakukan pemesanan proyek. | Teridentifikasi  |
| ACT-03 | Client        | Pengguna yang mengakses portal client.                      | Perlu verifikasi |
| ACT-04 | Administrator | Pengguna yang diperkirakan mengelola sistem dan pemesanan.  | Perlu konfirmasi |

## 6. Inventarisasi Fitur

| ID     | Fitur                      | Deskripsi                                                | Status Observasi      |
| ------ | -------------------------- | -------------------------------------------------------- | --------------------- |
| FT-001 | Homepage                   | Menampilkan informasi utama platform.                    | Terobservasi          |
| FT-002 | Portofolio                 | Menyediakan navigasi menuju informasi portofolio.        | Menu terobservasi     |
| FT-003 | Layanan                    | Menyediakan informasi layanan pengembangan teknologi.    | Menu terobservasi     |
| FT-004 | Paket                      | Menampilkan pilihan paket beserta harga.                 | Terobservasi          |
| FT-005 | Konsultasi AI              | Menyediakan konsultasi kebutuhan proyek melalui chatbot. | Terobservasi sebagian |
| FT-006 | Checkout                   | Menampilkan formulir pemesanan proyek.                   | Terobservasi          |
| FT-007 | Validasi Form              | Memeriksa kelengkapan dan format data pemesanan.         | Perlu pengujian       |
| FT-008 | Login                      | Menyediakan halaman autentikasi pengguna.                | Terobservasi          |
| FT-009 | Pembayaran                 | Mendukung proses pembayaran proyek.                      | Perlu verifikasi      |
| FT-010 | Portal Internal dan Client | Menyediakan akses ke portal pengguna terautentikasi.     | Perlu verifikasi      |

## 7. Functional Requirements

| ID     | Kebutuhan Fungsional                                                            | Prioritas | Status                |
| ------ | ------------------------------------------------------------------------------- | --------- | --------------------- |
| FR-001 | Sistem harus menampilkan halaman utama dan informasi platform.                  | Medium    | Terobservasi          |
| FR-002 | Sistem harus menyediakan akses menuju informasi portofolio.                     | Medium    | Perlu verifikasi      |
| FR-003 | Sistem harus menampilkan informasi layanan yang tersedia.                       | Medium    | Perlu verifikasi      |
| FR-004 | Sistem harus menampilkan pilihan paket dan harga.                               | High      | Terobservasi          |
| FR-005 | Sistem harus memungkinkan pengguna memilih paket proyek.                        | High      | Terobservasi sebagian |
| FR-006 | Sistem harus menyediakan kolom input konsultasi AI.                             | High      | Terobservasi          |
| FR-007 | Sistem harus memberikan respons terhadap pesan konsultasi pengguna.             | High      | Perlu pengujian       |
| FR-008 | Sistem harus menampilkan formulir checkout pemesanan.                           | High      | Terobservasi          |
| FR-009 | Sistem harus menyediakan input nama, email, WhatsApp, paket, dan tujuan proyek. | High      | Terobservasi          |
| FR-010 | Sistem harus memvalidasi kelengkapan data pemesanan.                            | High      | Perlu pengujian       |
| FR-011 | Sistem harus memvalidasi format email dan nomor WhatsApp.                       | High      | Perlu pengujian       |
| FR-012 | Sistem harus menyediakan halaman login dengan email dan password.               | High      | Terobservasi          |
| FR-013 | Sistem harus memverifikasi kredensial pengguna.                                 | High      | Perlu pengujian       |
| FR-014 | Sistem harus menolak kredensial yang tidak valid.                               | High      | Perlu pengujian       |
| FR-015 | Sistem harus mendukung proses pembayaran sesuai alur bisnis.                    | High      | Perlu konfirmasi      |
| FR-016 | Sistem harus membatasi akses portal berdasarkan hak akses pengguna.             | High      | Perlu konfirmasi      |

## 8. Non-Functional Requirements

| ID      | Aspek          | Kebutuhan Nonfungsional                                                             | Prioritas |
| ------- | -------------- | ----------------------------------------------------------------------------------- | --------- |
| NFR-001 | Usability      | Antarmuka harus mudah dipahami dan digunakan.                                       | High      |
| NFR-002 | Performance    | Sistem harus memberikan respons dalam batas waktu yang disepakati.                  | High      |
| NFR-003 | Security       | Sistem harus melindungi data dan kredensial pengguna.                               | High      |
| NFR-004 | Compatibility  | Sistem harus dapat digunakan pada browser yang didukung.                            | Medium    |
| NFR-005 | Responsiveness | Tampilan harus menyesuaikan ukuran layar desktop dan mobile.                        | Medium    |
| NFR-006 | Reliability    | Sistem harus menangani kesalahan tanpa menyebabkan kegagalan yang tidak terkendali. | High      |
| NFR-007 | Availability   | Sistem harus tersedia selama periode pengujian yang disepakati.                     | High      |
| NFR-008 | Data Integrity | Sistem harus menjaga konsistensi data pemesanan pengguna.                           | High      |

Catatan: Target kuantitatif dan batas penerimaan kebutuhan nonfungsional masih memerlukan persetujuan tim dan pemilik sistem.

## 9. User Story

| ID     | User Story                                                                                               | Requirement    |
| ------ | -------------------------------------------------------------------------------------------------------- | -------------- |
| US-001 | Sebagai visitor, saya ingin melihat halaman utama agar mengetahui informasi platform.                    | FR-001         |
| US-002 | Sebagai visitor, saya ingin melihat portofolio agar mengetahui hasil proyek sebelumnya.                  | FR-002         |
| US-003 | Sebagai visitor, saya ingin melihat layanan agar mengetahui solusi yang tersedia.                        | FR-003         |
| US-004 | Sebagai customer, saya ingin melihat paket dan harga agar dapat menyesuaikan kebutuhan dengan anggaran.  | FR-004         |
| US-005 | Sebagai customer, saya ingin memilih paket agar dapat menentukan layanan yang dibutuhkan.                | FR-005         |
| US-006 | Sebagai customer, saya ingin berkonsultasi dengan AI agar memperoleh rekomendasi proyek.                 | FR-006, FR-007 |
| US-007 | Sebagai customer, saya ingin mengisi formulir checkout agar dapat mengajukan pemesanan proyek.           | FR-008, FR-009 |
| US-008 | Sebagai customer, saya ingin memperoleh informasi kesalahan input agar dapat memperbaiki data pemesanan. | FR-010, FR-011 |
| US-009 | Sebagai client, saya ingin melakukan login agar dapat mengakses portal.                                  | FR-012, FR-013 |
| US-010 | Sebagai client, saya ingin akun saya terlindungi dari akses tidak sah.                                   | FR-014, FR-016 |
| US-011 | Sebagai customer, saya ingin melakukan pembayaran sesuai paket yang dipilih.                             | FR-015         |

## 10. Acceptance Criteria

Acceptance Criteria berikut merupakan rancangan kondisi penerimaan yang akan digunakan sebagai dasar pengujian. Seluruh skenario belum dinyatakan lulus.

### AC-001 - Akses Homepage

Requirement: FR-001

- Given pengguna memiliki akses internet.
- When pengguna membuka URL website.
- Then sistem menampilkan halaman utama dan menu navigasi.

### AC-002 - Akses Portofolio

Requirement: FR-002

- Given pengguna berada pada halaman utama.
- When pengguna memilih menu Portofolio.
- Then sistem menampilkan informasi portofolio.

### AC-003 - Akses Layanan

Requirement: FR-003

- Given pengguna berada pada halaman utama.
- When pengguna memilih menu Layanan.
- Then sistem menampilkan informasi layanan yang tersedia.

### AC-004 - Informasi Paket

Requirement: FR-004

- Given pengguna mengakses bagian paket.
- When informasi paket ditampilkan.
- Then pengguna dapat melihat nama paket dan harga.

### AC-005 - Pemilihan Paket

Requirement: FR-005

- Given pengguna berada pada halaman pemilihan paket.
- When pengguna memilih salah satu paket.
- Then sistem menampilkan indikator paket yang dipilih.

### AC-006 - Konsultasi AI dengan Pesan Valid

Requirement: FR-006, FR-007

- Given pengguna berada pada halaman konsultasi AI.
- When pengguna memasukkan pesan kebutuhan proyek dan menekan tombol Kirim.
- Then sistem menampilkan pesan pengguna dan memberikan respons AI yang relevan.

### AC-007 - Konsultasi AI dengan Pesan Kosong

Requirement: FR-006

- Given pengguna berada pada halaman konsultasi AI.
- When pengguna tidak memasukkan pesan dan mencoba mengirimkannya.
- Then sistem mencegah pengiriman pesan kosong.

### AC-008 - Akses Checkout

Requirement: FR-008, FR-009

- Given pengguna berada pada halaman utama.
- When pengguna memilih tombol Mulai Proyek.
- Then sistem menampilkan formulir checkout beserta kolom data pemesanan.

### AC-009 - Checkout dengan Data Valid

Requirement: FR-009, FR-010

- Given pengguna berada pada halaman checkout di lingkungan pengujian yang diizinkan.
- When pengguna mengisi seluruh data wajib dengan benar dan mengirimkan formulir.
- Then sistem menerima data dan melanjutkan proses sesuai alur pemesanan.

### AC-010 - Checkout dengan Data Kosong

Requirement: FR-010

- Given pengguna berada pada halaman checkout.
- When pengguna mencoba mengirim formulir tanpa melengkapi data wajib.
- Then sistem menolak pengiriman dan menampilkan informasi validasi.

### AC-011 - Validasi Email

Requirement: FR-011

- Given pengguna berada pada halaman checkout.
- When pengguna memasukkan email dengan format tidak valid.
- Then sistem menolak input atau menampilkan pesan validasi email.

### AC-012 - Validasi WhatsApp

Requirement: FR-011

- Given pengguna berada pada halaman checkout.
- When pengguna memasukkan nomor WhatsApp dengan format tidak valid.
- Then sistem menampilkan informasi kesalahan dan mencegah pengiriman data yang tidak valid.

### AC-013 - Akses Halaman Login

Requirement: FR-012

- Given pengguna mengakses halaman login.
- When halaman selesai dimuat.
- Then sistem menampilkan kolom email, password, dan tombol Masuk.

### AC-014 - Login dengan Kredensial Valid

Requirement: FR-013

- Given pengguna memiliki akun pengujian yang valid.
- When pengguna memasukkan email dan password yang benar.
- Then sistem memberikan akses ke portal sesuai hak akses pengguna.

### AC-015 - Login dengan Kredensial Tidak Valid

Requirement: FR-014

- Given pengguna berada pada halaman login.
- When pengguna memasukkan kredensial yang tidak valid.
- Then sistem menolak autentikasi dan tidak memberikan akses ke portal.

### AC-016 - Pembayaran

Requirement: FR-015

- Given pengguna memiliki pemesanan yang valid pada lingkungan pengujian.
- When pengguna menyelesaikan simulasi pembayaran sesuai prosedur.
- Then sistem menampilkan status pembayaran yang sesuai.

Catatan: Skenario ini memerlukan konfirmasi alur pembayaran dan lingkungan sandbox.

### AC-017 - Pembatasan Hak Akses

Requirement: FR-016

- Given pengguna tidak memiliki hak akses terhadap suatu halaman portal.
- When pengguna mencoba mengakses halaman tersebut.
- Then sistem menolak akses dan tidak menampilkan informasi yang dilindungi.

## 11. Prioritas Pengujian

| Prioritas | Fitur           | Alasan                                         |
| --------- | --------------- | ---------------------------------------------- |
| High      | Konsultasi AI   | Merupakan salah satu layanan utama platform.   |
| High      | Pemilihan Paket | Berkaitan dengan keputusan pemesanan pengguna. |
| High      | Checkout        | Berkaitan dengan proses bisnis utama.          |
| High      | Validasi Form   | Mencegah data pemesanan yang tidak valid.      |
| High      | Login           | Berkaitan dengan keamanan akses pengguna.      |
| High      | Pembayaran      | Berkaitan dengan transaksi keuangan.           |
| High      | Hak Akses       | Berkaitan dengan perlindungan data pengguna.   |
| Medium    | Homepage        | Menyediakan informasi awal kepada pengguna.    |
| Medium    | Portofolio      | Mendukung penyampaian informasi proyek.        |
| Medium    | Layanan         | Mendukung pemahaman pengguna terhadap produk.  |

## 12. Requirement Traceability Matrix

| Requirement | User Story | Acceptance Criteria |
| ----------- | ---------- | ------------------- |
| FR-001      | US-001     | AC-001              |
| FR-002      | US-002     | AC-002              |
| FR-003      | US-003     | AC-003              |
| FR-004      | US-004     | AC-004              |
| FR-005      | US-005     | AC-005              |
| FR-006      | US-006     | AC-006, AC-007      |
| FR-007      | US-006     | AC-006              |
| FR-008      | US-007     | AC-008              |
| FR-009      | US-007     | AC-008, AC-009      |
| FR-010      | US-008     | AC-009, AC-010      |
| FR-011      | US-008     | AC-011, AC-012      |
| FR-012      | US-009     | AC-013              |
| FR-013      | US-009     | AC-014              |
| FR-014      | US-010     | AC-015              |
| FR-015      | US-011     | AC-016              |
| FR-016      | US-010     | AC-017              |

## 13. Evidence

Evidence akan dikumpulkan dan disimpan pada direktori:

`evidence/fy/d02/`

| No  | Evidence yang Direncanakan | Requirement            | Status  |
| --- | -------------------------- | ---------------------- | ------- |
| 1   | 01-navigation.jpg          | FR-001, FR-002, FR-003 | Pending |
| 2   | 02-package-selection.jpg   | FR-004, FR-005         | Pending |
| 3   | 03-ai-consultation.jpg     | FR-006, FR-007         | Pending |
| 4   | 04-checkout-form.jpg       | FR-008, FR-009         | Pending |
| 5   | 05-form-validation.jpg     | FR-010, FR-011         | Pending |
| 6   | 06-login-page.jpg          | FR-012                 | Pending |

## 14. Keterbatasan

- Analisis awal dilakukan berdasarkan observasi antarmuka website.
- Dokumentasi kebutuhan resmi dari pemilik sistem masih diperlukan.
- Akses akun pengujian portal internal dan client belum terverifikasi.
- Mekanisme pembayaran dan pengelolaan hak akses masih memerlukan konfirmasi.
- Pengujian yang menghasilkan transaksi atau perubahan data hanya boleh dilakukan pada lingkungan yang diizinkan.
- Prioritas dan Acceptance Criteria masih memerlukan review tim.
- Status terobservasi tidak berarti fitur telah lulus pengujian.

## 15. Kesimpulan

Berdasarkan identifikasi awal kebutuhan sistem Wave Projects Center.ID, diperoleh inventarisasi yang terdiri atas 10 fitur, 16 Functional Requirements, 8 Non-Functional Requirements, 11 User Story, dan 17 Acceptance Criteria.

Dokumen ini digunakan sebagai dasar penyusunan skenario pengujian, test case, requirement traceability, dan pengembangan keyword-driven testing pada tahapan berikutnya.

## 16. Referensi

1. Wave Projects Center.ID. https://wave-projects-center-id.vercel.app/
2. ISO/IEC/IEEE 29119-5:2024, Software and systems engineering - Software testing - Part 5: Keyword-driven testing.
3. Rencana Kerja Testing & QA Kelompok 4.
4. CONTRIBUTING.md - Testing-QA-Kelompok-4.

---

Disusun oleh:

Fiyado Yudha Witama

Domain Expert - Testing & QA Kelompok 4

## 17. Hasil Observasi dan Pemetaan Requirement D.3

Bagian ini merupakan tambahan hasil eksplorasi dan analisis Test Designer (D.3) pada D02 untuk mendukung inventarisasi kebutuhan dan penyusunan test condition.

### 17.1 Hasil Observasi Awal

| Requirement ID | Fitur     | Hasil Observasi                                                        | Pemetaan Functional Requirement |
| -------------- | --------- | ---------------------------------------------------------------------- | ------------------------------- |
| REQ-001        | Layanan   | Bagian layanan dapat diakses dan ditampilkan.                          | FR-003                          |
| REQ-002        | AI Chat   | Antarmuka AI Chat dapat diakses. Respons AI belum diverifikasi.        | FR-006, FR-007                  |
| REQ-003        | Pemesanan | Bagian pemesanan dapat diakses. Pengiriman pesanan belum diverifikasi. | FR-008, FR-009                  |

### 17.2 Pemetaan Kandidat Kebutuhan Fungsional

| Requirement ID | Kandidat Kebutuhan                                   | Pemetaan               |
| -------------- | ---------------------------------------------------- | ---------------------- |
| REQ-004        | Sistem menyediakan navigasi antarbagian website.     | FR-001, FR-002, FR-003 |
| REQ-005        | Sistem menerima pesan konsultasi dari pengguna.      | FR-006                 |
| REQ-006        | Sistem memberikan respons terhadap pesan konsultasi. | FR-007                 |
| REQ-007        | Sistem menerima data pemesanan pengguna.             | FR-009                 |
| REQ-008        | Sistem memvalidasi data pemesanan.                   | FR-010, FR-011         |
| REQ-009        | Sistem menyediakan halaman checkout.                 | FR-008                 |
| REQ-010        | Sistem menyediakan mekanisme pembayaran.             | FR-015                 |

### 17.3 Pemetaan Kandidat Kebutuhan Nonfungsional

| Kandidat      | Pemetaan NFR |
| ------------- | ------------ |
| Usability     | NFR-001      |
| Compatibility | NFR-004      |
| Performance   | NFR-002      |
| Security      | NFR-003      |
| Reliability   | NFR-006      |

### 17.4 Catatan Validasi

1. Hasil observasi REQ-001 sampai REQ-003 menunjukkan akses terhadap bagian antarmuka, bukan bukti bahwa seluruh proses bisnis telah berhasil.
2. Respons AI, pengiriman formulir pemesanan, checkout, dan pembayaran masih memerlukan pengujian lebih lanjut.
3. Pemetaan requirement merupakan pemetaan awal dan perlu ditinjau bersama Domain Expert serta QA Lead.
4. Prioritas dan kriteria penerimaan tetap mengikuti dokumen utama sampai memperoleh persetujuan tim.
