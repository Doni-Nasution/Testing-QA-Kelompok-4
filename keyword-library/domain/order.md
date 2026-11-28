# Keyword Domain Layer: Order (Layanan & Pemesanan)

| Atribut | Nilai |
|---|---|
| Layer | Domain Layer (high-level / composite keyword) |
| Domain | Layanan (`#features`) dan pemesanan (`/checkout`) |
| Referensi | ISO/IEC/IEEE 29119-5:2024 Cl.7.2.8; Annex A; Tabel F.1 |
| Pemilik | Ghatfani (D.4); validasi domain: Fiyado (D.2) |
| Status | DRAF v0.1, 2026-11-28 |

## 1. Daftar Keyword (format Tabel F.1)
| ID | Keyword | Tipe | Parameter (default) | Deskripsi |
|---|---|---|---|---|
| DK-ORD-01 | Open Service Packages Section | Navigation | - | Menuju bagian layanan lewat tombol/tautan layanan di beranda (hasil walkthrough D07 mengarah ke `#features`) |
| DK-ORD-02 | Open Order Page | Navigation | - | Menuju halaman pemesanan lewat menu "Pesan" (`/checkout`) |
| DK-ORD-03 | Fill Order Form | Navigation | `nama` (wajib), `email` (wajib), `whatsapp` (wajib), `paket` (`Starter / Landing Page`) | Mengisi field form pemesanan pada `/checkout` sesuai hasil inspeksi walkthrough D07 |
| DK-ORD-04 | Submit Order | Navigation | - | Mengirim pemesanan. **Nonaktif di produksi**: dapat memicu transaksi/pembayaran (Midtrans). Hanya untuk staging/sandbox dengan izin |
| DK-ORD-05 | Verify Service Packages Section Is Displayed | Verification | - | Memastikan URL memuat anchor layanan (`#features`) dan bagian layanan terlihat |
| DK-ORD-06 | Verify Order Page Is Displayed | Verification | `timeout` (`30s`) | Memastikan URL memuat `/checkout` dan form pemesanan terlihat |
| DK-ORD-07 | Verify Order Field Has Value | Verification | `field` (wajib); `expected` (wajib) | Memastikan field form (`nama`, `email`, atau `whatsapp`) berisi nilai yang diketik |
| DK-ORD-08 | Verify Order Validation Message Is Displayed | Verification | `expected_message` (wajib) | Memastikan validasi sisi klien aktif untuk input tidak valid. Form memakai validasi HTML5 native (`required` & `pattern` WA) tanpa pesan teks DOM terpisah saat blur |

## 2. Komposisi & Ketergantungan
| Keyword | Disusun dari (Test Interface Layer) | Pra-kondisi | KTC / Requirement |
|---|---|---|---|
| Open Service Packages Section | `Click Element` | Beranda terbuka | TBD (menunggu KTC D07) / FR-003, FR-004 |
| Open Order Page | `Click Element` | Beranda terbuka | TBD (menunggu KTC D07) / FR-008 |
| Fill Order Form | `Input Text Into Field`, `Click Element` | Halaman pemesanan tampil | TBD (menunggu KTC D07) / FR-005, FR-009 |
| Submit Order | `Click Element` | Form terisi; **staging/izin** | TBD (menunggu KTC D07) / FR-010, FR-015 |
| Verify Service Packages Section Is Displayed | `Verify URL Contains`, `Verify Element Is Visible` | DK-ORD-01 sudah dilakukan | TBD (menunggu KTC D07) / FR-003, FR-004 |
| Verify Order Page Is Displayed | `Verify URL Contains`, `Verify Element Is Visible` | DK-ORD-02 sudah dilakukan | TBD (menunggu KTC D07) / FR-008 |
| Verify Order Field Has Value | `Verify Field Has Value` | Field sudah diisi | TBD (menunggu KTC D07) / FR-009 |
| Verify Order Validation Message Is Displayed | `Verify Element Is Visible`, `Verify Element Text Contains` | Input tidak valid sudah dimasukkan | TBD (menunggu KTC D07) / FR-010, FR-011 |

## 3. Locator
| Variabel | Elemen | Nilai |
|---|---|---|
| `${BTN_VIEW_SERVICES}` | Tautan/Tombol Layanan | `css=a[href="#features"]` |
| `${NAV_ORDER}` | Menu "Pesan" | `css=a[href$="/checkout"] >> nth=0` |
| `${ORDER_FIELD_NAMA}` | Field Nama Lengkap | `css=input[placeholder="Ariyas Pratama"]` |
| `${ORDER_FIELD_EMAIL}` | Field Email (Gmail aktif) | `css=input[placeholder="ariyas@gmail.com"]` |
| `${ORDER_FIELD_WHATSAPP}` | Field WhatsApp Indonesia | `css=input[placeholder="081234567890"]` |
| `${ORDER_PACKAGE_STARTER}` | Kartu Paket Starter | `css=form button:has-text("Starter / Landing Page")` |
| `${ORDER_SUBMIT}` | Tombol submit pemesanan | `css=form button[type="submit"]` *(hanya dicatat, tidak diklik di produksi)* |
| `${ORDER_VALIDATION_MSG}` | Pesan validasi | Validasi native HTML5 browser (`required` & `pattern` attribute `title`) |

## 4. Catatan Desain
- `Submit Order` didefinisikan agar library lengkap, tetapi **tidak diimplementasikan untuk produksi**. Ini dicatat di klaim tailored conformance (batasan klaim).
- Tidak ada keyword pembayaran. Midtrans di luar cakupan.
- Daftar keyword Test Interface Layer yang dibutuhkan dirujuk pada Bagian 6 dokumen `keyword-library/domain/consultation.md`.

## 5. Riwayat Revisi
| Versi | Tanggal | Perubahan | Oleh |
|---|---|---|---|
| 0.1 | 2026-11-28 | Draf awal berdasarkan walkthrough D07 | ghatfani |
