# Smoke Test Manual: D02
SUT: Wave Projects Center.ID v0.1.0 (sut-wave-projects:0.1.0-local + mysql:8.0.40) | URL: http://localhost:3000 | Penguji: Ghatfani | Tanggal: 2026-11-23

| # | Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---------|------------------|--------------|--------|
| 1 | Buka halaman utama (http://localhost:3000) | Halaman tampil tanpa error | Halaman beranda Wave Projects tampil lengkap beserta navigasi layanan dan AI chat | PASS |
| 2 | Panggil endpoint katalog paket (/api/v1/packages) | Daftar paket tampil dari DB | Endpoint /api/v1/packages mengembalikan HTTP 500 (Unknown column 'is_active') akibat perbedaan skema DB | FAIL |
| 3 | Pembuatan akun uji lokal pada tabel users | Akun tersimpan dengan password ter-hash | Aplikasi tidak menyediakan halaman /register publik; akun uji lokal (Super Admin) berhasil disiapkan di tabel users | PASS |
| 4 | Login melalui http://localhost:3000/login dengan akun uji | Login berhasil & masuk /dashboard | Autentikasi /api/v1/login mengembalikan JWT valid dan masuk ke portal /dashboard sebagai Super Admin | PASS |
| 5 | Login dengan password salah | Ditolak dengan pesan error | Sistem menolak kredensial salah dan menampilkan pesan error Kredensial tidak valid | PASS |
| 6 | Lakukan 1 aksi inti di portal/layanan (akses menu dashboard & /checkout) | Halaman merespons normal | Menu internal dashboard dan halaman /checkout dapat diakses tanpa error | PASS |
| 7 | Klik Log Out pada sidebar dashboard | Sesi berakhir | Token sesi dihapus dan pengguna keluar dari dashboard | PASS |
| 8 | Panggil endpoint API publik lewat curl.exe (/api/v1/portfolios) | HTTP 200, JSON valid | Mengembalikan HTTP 200 dengan payload JSON valid | PASS |

## Catatan / temuan awal
- **Temuan skema database (FAIL pada langkah #2):** Endpoint /api/v1/packages mencari kolom is_active pada tabel packages, sedangkan skrip inisialisasi database.sql mendefinisikan kolom status ENUM('active', 'inactive'). Temuan ini dicatat sebagai cacat sinkronisasi skema database untuk ditindaklanjuti pada pengujian fungsional.
- **Alur autentikasi & hak akses:** Halaman /register publik tidak tersedia (akun klien dibuat melalui alur pemesanan atau panel admin); form login berada di /login dan redirect ke /dashboard memerlukan kolom ole yang valid pada tabel users.
- **Ketergantungan API eksternal:** Fitur AI Chat, Cloudflare Turnstile, Midtrans, dan Upstash Redis memakai *dummy/test key* pada environment lokal agar isolasi pengujian tetap terjaga.
