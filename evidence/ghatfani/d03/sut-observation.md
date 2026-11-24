# Observasi SUT (Pasif): D03
Tanggal: 2026-11-24 | Penguji: Ghatfani | Metode: browser biasa + DevTools (tanpa beban) | URL: https://wave-projects-center-id.vercel.app

| Halaman | URL | Elemen/fitur teramati | Catatan untuk keyword |
|---|---|---|---|
| Beranda | `/` | Navigasi utama (Beranda, Layanan, AI Chat, Pesan), tombol CTA konsultasi & layanan, daftar portfolio/paket | Keyword navigasi & verifikasi elemen utama |
| AI Chat | `/chat` | Input pesan konsultasi, tombol kirim, area balasan asisten AI (streaming/pesan) | Respons nondeterministik; verifikasi status & struktur balasan |
| Checkout | `/checkout` | Form data klien, pilihan layanan/paket, tombol submit pemesanan ke Midtrans | Jangan lanjutkan ke pembayaran nyata |

## Endpoint yang terlihat di DevTools > Network (hanya amati)
| Method | Path | Terpicu oleh | Status |
|---|---|---|---|
| `GET` | `/api/v1/portfolios` | Memuat daftar portfolio di beranda | `200` |
| `GET` | `/api/v1/settings` | Memuat konfigurasi publik situs | `200` |
| `GET` | `/api/v1/packages` | Memuat katalog paket layanan | `200` (produksi) / `500` (schema lokal) |
| `POST` | `/api/v1/chat/send` | Mengirim pesan konsultasi di `/chat` | `200` |
| `POST` | `/api/v1/orders/checkout` | Mengirim form pemesanan di `/checkout` | `200` / `201` (tidak dilanjutkan bayar) |

## Teknologi (dari halaman publik)
Next.js, Tailwind CSS, TiDB, Vercel, Midtrans, dan integrasi AI konsultasi.
