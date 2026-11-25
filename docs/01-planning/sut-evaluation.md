# Evaluasi System Under Test (SUT)

> Status: Draf evaluasi D01, diselaraskan dengan informasi SUT D03.
> Penanggung jawab: Fiyado Yudha Witama (FY)
> Peran: Domain Expert (D.2)
> Kelompok: 4
> Acuan proyek: ISO/IEC/IEEE 29119-5:2024

## 1. Pendahuluan

System Under Test (SUT) merupakan sistem atau aplikasi yang menjadi objek pengujian perangkat lunak.

Evaluasi SUT dilakukan untuk mengetahui karakteristik aplikasi, cakupan fitur, kebutuhan pengujian, ketersediaan lingkungan pengujian, serta batasan yang perlu diperhatikan selama pelaksanaan Software Testing dan Quality Assurance.

Sebagai Domain Expert, penulis bertanggung jawab dalam mengidentifikasi domain aplikasi, kebutuhan pengguna, proses bisnis, serta fitur yang menjadi dasar perancangan pengujian.

## 2. Tujuan Evaluasi

1. Mengidentifikasi karakteristik kandidat SUT.
2. Membandingkan kelayakan kandidat aplikasi.
3. Mengidentifikasi fitur dan proses bisnis SUT.
4. Menentukan cakupan awal pengujian.
5. Mengidentifikasi lingkungan dan batasan pengujian.
6. Mendukung penyusunan requirement dan test case.

## 3. Kandidat System Under Test

### 3.1 RealWorld Conduit

RealWorld Conduit merupakan aplikasi berbasis web yang menyediakan fitur registrasi, autentikasi, pengelolaan artikel, komentar, dan interaksi pengguna.

Aplikasi ini mendukung pengujian fungsional dan REST API.

### 3.2 OWASP Juice Shop

OWASP Juice Shop merupakan aplikasi yang dirancang untuk pembelajaran pengujian keamanan perangkat lunak.

Aplikasi ini menyediakan fitur autentikasi, katalog produk, keranjang belanja, dan berbagai skenario keamanan.

### 3.3 Restful-Booker

Restful-Booker merupakan layanan REST API yang menyediakan fungsi pengelolaan data pemesanan.

Aplikasi ini mendukung pengujian autentikasi, operasi CRUD, validasi request, dan response API.

### 3.4 Wave Projects Center.ID

Wave Projects Center.ID merupakan aplikasi berbasis web yang menyediakan informasi layanan proyek, portfolio, konsultasi berbasis AI, dan pemesanan layanan.

Aplikasi ini menjadi SUT yang tercatat dalam dokumen test-environment.md kelompok pada pembaruan D03.

## 4. Perbandingan Kandidat SUT

| Kriteria | Conduit | Juice Shop | Restful-Booker | Wave Projects |
|---|---|---|---|---|
| Antarmuka web | Ya | Ya | Fokus API | Ya |
| Pengujian fungsional | Ya | Ya | Ya | Ya |
| Pengujian API | Ya | Ya | Ya | Ya |
| Potensi pengujian keamanan | Ya | Ya | Ya | Ya, dengan batasan izin |
| Lingkungan lokal | Tersedia melalui implementasi | Tersedia | Tersedia | Tersedia menurut dokumen tim |
| Proses bisnis | Artikel | E-commerce | Pemesanan | Layanan proyek |
| Integrasi AI | Tidak menjadi fitur utama | Tidak menjadi fitur utama | Tidak | Ya |
| Integrasi pembayaran | Tidak | Simulasi | Tidak | Midtrans |

Perbandingan tersebut merupakan kajian awal berdasarkan karakteristik aplikasi dan dokumentasi kelompok, bukan hasil eksekusi pengujian langsung.

## 5. Profil System Under Test

| Item | Keterangan |
|---|---|
| Nama aplikasi | Wave Projects Center.ID |
| Jenis aplikasi | Website layanan proyek |
| URL produksi | https://wave-projects-center-id.vercel.app |
| Canonical domain | waveprojects.my.id |
| Frontend | Next.js dan Tailwind CSS |
| Database | TiDB/MySQL |
| Deployment | Vercel |
| Payment gateway | Midtrans |
| Artificial Intelligence | Gemini AI |
| Sandbox lokal | 127.0.0.1:3000 |
| Lingkungan isolasi | Docker Compose |

## 6. Inventarisasi Fitur SUT

| ID | Fitur | Deskripsi | Potensi Pengujian |
|---|---|---|---|
| F-01 | Beranda | Menampilkan informasi utama website | Tampilan dan navigasi |
| F-02 | Navigasi | Mengarahkan pengguna ke halaman layanan | Validasi tautan |
| F-03 | Portfolio | Menampilkan daftar proyek | Tampilan dan pemuatan data |
| F-04 | Katalog layanan | Menampilkan paket layanan | Validasi informasi paket |
| F-05 | AI Chat | Menyediakan konsultasi berbasis AI | Struktur dan perilaku respons |
| F-06 | Form data klien | Menerima informasi calon pelanggan | Validasi input |
| F-07 | Pemilihan paket | Memilih paket layanan | Kesesuaian pilihan |
| F-08 | Checkout | Memproses pemesanan layanan | Validasi formulir |
| F-09 | Pembayaran | Integrasi pembayaran Midtrans | Pengujian sandbox |
| F-10 | Login | Portal internal | Autentikasi pada lingkungan berizin |

## 7. Identifikasi Halaman

| No | Halaman | Path |
|---|---|---|
| 1 | Beranda | / |
| 2 | Konsultasi AI | /chat |
| 3 | Pemesanan | /checkout |
| 4 | Portal internal | /login |

## 8. Identifikasi Endpoint API

Endpoint berikut bersumber dari dokumentasi observasi Ghatfani pada D03.

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | /api/v1/portfolios | Memuat daftar portfolio |
| GET | /api/v1/settings | Memuat konfigurasi publik |
| GET | /api/v1/packages | Memuat katalog paket |
| POST | /api/v1/chat/send | Mengirim pesan konsultasi |
| POST | /api/v1/orders/checkout | Mengirim data pemesanan |

## 9. Lingkungan Pengujian

### 9.1 Lingkungan Produksi

Lingkungan produksi digunakan untuk observasi pasif dan pengujian black-box terbatas sesuai izin.

### 9.2 Lingkungan Lokal

Lingkungan lokal menggunakan Docker Compose sebagai sandbox terisolasi untuk mendukung pengujian yang membutuhkan akses lebih mendalam.

Pengujian white-box, grey-box, performa, dan keamanan diarahkan pada lingkungan lokal yang diizinkan.

## 10. Batasan Pengujian

1. Tidak melakukan pembayaran nyata melalui Midtrans.
2. Tidak melakukan pengujian performa pada produksi tanpa izin tertulis.
3. Tidak melakukan security scanning pada produksi tanpa izin tertulis.
4. Pengujian AI Chat dilakukan secara terbatas dengan mempertimbangkan kuota dan biaya.
5. Pengujian yang berpotensi mengubah data dilakukan pada sandbox yang diizinkan.
6. Tidak menggunakan data pribadi pelanggan sebagai data pengujian.

## 11. Rekomendasi SUT

Wave Projects Center.ID direkomendasikan sebagai objek pengujian untuk menyelaraskan pekerjaan Domain Expert dengan lingkungan pengujian dan observasi yang telah didokumentasikan oleh anggota kelompok.

Aplikasi ini memiliki cakupan fitur yang mendukung penyusunan kebutuhan pengujian, pengujian fungsional, API, integrasi, dan keyword-driven testing.

Penetapan serta cakupan akhir pengujian mengikuti keputusan QA Lead dan izin pemilik sistem.

## 12. Kesimpulan

Berdasarkan kajian awal kandidat SUT dan dokumentasi lingkungan pengujian kelompok, Wave Projects Center.ID merupakan objek pengujian yang digunakan sebagai dasar penyusunan requirement dan rancangan pengujian selanjutnya.

Inventarisasi fitur dalam dokumen ini masih perlu diverifikasi melalui eksplorasi langsung dan konfirmasi kebutuhan sistem.

## 13. Referensi

- ISO/IEC/IEEE 29119-5:2024.
- README.md.
- CONTRIBUTING.md.
- docs/01-planning/roles-raci.md.
- docs/01-planning/test-environment.md.
- evidence/ghatfani/d03/sut-observation.md.
- https://wave-projects-center-id.vercel.app
- https://github.com/gothinkster/realworld
- https://owasp.org/www-project-juice-shop/
- https://restful-booker.herokuapp.com/

## 14. Riwayat Dokumen

| Tahap | Perubahan | Penulis |
|---|---|---|
| D01 | Penyusunan evaluasi kandidat SUT | FY |
| Penyesuaian D03 | Penyelarasan dengan dokumentasi Wave Projects Center.ID | FY |