# Walkthrough Manual Keyword Domain: D07
Tanggal: 2026-11-28 | Penguji: Ghatfani | SUT: https://wave-projects-center-id.vercel.app

| # | Langkah | Hasil teramati | Locator terbaik (DevTools) |
|---|---|---|---|
| 1 | Beranda -> klik "Lihat Layanan" | Tidak ke `#packages`; halaman menggulir ke bagian **Fitur Utama** dan URL menjadi `.../#features#features` (observasi duplikasi hash) | `css=a[href="#features"]` |
| 2 | Beranda -> klik menu "Pesan" | Pindah ke `/checkout` | `css=a[href$="/checkout"] >> nth=0` |
| 3 | Di `/checkout`: catat SEMUA field form (label, tipe, wajib?) | 1) **Nama Lengkap *** (`input[type="text"]`, wajib); 2) **Email (Wajib Gmail aktif) *** (`input`, wajib); 3) **WhatsApp (Nomor Indonesia Aktif) *** (`input[type="text"]`, wajib, `pattern="^(?:\+62|62|0)8[1-9][0-9]{6,10}$"`); 4) **Pilih Paket *** (kartu pilihan paket, default: *Starter / Landing Page*) | Nama: `css=input[placeholder="Ariyas Pratama"]`; Email: `css=input[placeholder="ariyas@gmail.com"]`; WA: `css=input[placeholder="081234567890"]`; Paket: `css=form button[type="button"]`; Submit: `css=form button[type="submit"]` (tidak diklik) |
| 4 | Di `/checkout`: klik di field lalu keluar tanpa mengisi (lihat pesan validasi, tanpa submit) | Tidak muncul elemen pesan error DOM saat blur; form memakai validasi HTML5 native (`required` & `pattern` dengan atribut `title="Masukkan nomor WA Indonesia yang valid (contoh: 0812... atau 62812...)"`) yang muncul saat submit dicoba | Validasi native browser (tidak ada selector DOM terpisah) |
| 5 | Beranda -> klik menu "AI Chat" | Pindah ke `/chat` | `css=a[href$="/chat"] >> nth=0` |
| 6 | Di `/chat`: ketik 1 kalimat di kolom pesan | Teks terlihat di kolom input | `css=input[placeholder="Ceritakan proyek impian Anda..."]` |
| 7 | Di `/chat`: catat locator tombol kirim dan area respons | Tombol `button.bg-primary...` dengan role `button` dan nama aksesibilitas `Kirim`; area respons berupa gelembung pesan di dalam `<main>` | Kirim: `role=button[name="Kirim"]`; Respons: `css=main div[class*="rounded-2xl"] >> nth=-1` |
