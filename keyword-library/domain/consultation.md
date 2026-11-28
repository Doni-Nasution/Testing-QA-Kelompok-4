# Keyword Domain Layer: Consultation (AI Chat)

| Atribut | Nilai |
|---|---|
| Layer | Domain Layer (high-level / composite keyword) |
| Domain | Konsultasi AI (`/chat`) |
| Referensi | ISO/IEC/IEEE 29119-5:2024 Cl.7.2.8; Annex A (penamaan imperatif); Tabel F.1 |
| Pemilik | Ghatfani (D.4); validasi domain: Fiyado (D.2) |
| Status | DRAF v0.1, 2026-11-28 |

## 1. Daftar Keyword (format Tabel F.1)
| ID | Keyword | Tipe | Parameter (default) | Deskripsi |
|---|---|---|---|---|
| DK-CON-01 | Open Consultation Chat | Navigation | `entry` (`nav`; opsi `nav` / `cta`) | Membuka halaman AI chat dari beranda melalui menu navigasi (`nav`) atau tombol "Konsultasi Gratis" (`cta`) |
| DK-CON-02 | Enter Consultation Message | Navigation | `message` (wajib) | Mengetik pesan pada kolom chat tanpa mengirim |
| DK-CON-03 | Send Consultation Message | Navigation | `message` (wajib) | Mengetik dan mengirim pesan. **Menggunakan kuota AI pemilik: nonaktif di produksi** (butuh izin/staging, `ALLOW_WRITE=1`) |
| DK-CON-04 | Verify Consultation Page Is Displayed | Verification | `timeout` (`30s`) | Memastikan halaman chat tampil: URL memuat `/chat` dan kolom input terlihat |
| DK-CON-05 | Verify Consultation Message Is Entered | Verification | `expected_message` (wajib) | Memastikan kolom chat berisi teks yang diketik |
| DK-CON-06 | Verify Consultation Response Is Displayed | Verification | `timeout` (`30s`); `min_length` (`1`) | Memastikan area respons AI berisi teks (panjang >= `min_length`). **Tidak** membandingkan isi persis karena respons AI nondeterministik |

## 2. Komposisi & Ketergantungan
| Keyword | Disusun dari (Test Interface Layer) | Pra-kondisi | KTC / Requirement |
|---|---|---|---|
| Open Consultation Chat | `Open Page` (jika browser belum terbuka), `Click Element` | SUT dapat diakses | TBD (menunggu KTC D07) / FR-006 |
| Enter Consultation Message | `Input Text Into Field` | Halaman chat tampil | TBD (menunggu KTC D07) / FR-006 |
| Send Consultation Message | `Input Text Into Field`, `Click Element` | Halaman chat tampil; izin kuota | TBD (menunggu KTC D07) / FR-007 |
| Verify Consultation Page Is Displayed | `Verify URL Contains`, `Verify Element Is Visible` | Klik menu chat sudah dilakukan | TBD (menunggu KTC D07) / FR-006 |
| Verify Consultation Message Is Entered | `Verify Field Has Value` | Pesan sudah diketik | TBD (menunggu KTC D07) / FR-006 |
| Verify Consultation Response Is Displayed | `Wait For Element`, `Verify Element Text Is Not Empty` | Pesan terkirim (DK-CON-03) | TBD (menunggu KTC D07) / FR-007 |

## 3. Locator (disimpan sebagai variabel, bukan di test case)
| Variabel | Elemen | Nilai (hasil inspeksi D04/D07) |
|---|---|---|
| `${NAV_CHAT}` | Menu AI Chat | `css=a[href$="/chat"] >> nth=0` |
| `${CHAT_INPUT}` | Kolom pesan | `css=input[placeholder="Ceritakan proyek impian Anda..."]` |
| `${CHAT_SEND}` | Tombol kirim | `role=button[name="Kirim"]` |
| `${CHAT_RESPONSE}` | Area respons | `css=main div[class*="rounded-2xl"] >> nth=-1` |

## 4. Catatan Desain
- Navigation dan Verification **dipisah**: keyword `Open ...`/`Enter ...` tidak melakukan pengecekan; pengecekan ada di keyword `Verify ...`.
- Oracle respons AI: hanya struktur/perilaku (muncul, tidak kosong), bukan isi.
- Parameter locator tidak diekspos ke test case; test case hanya memakai nama bisnis di atas.

## 5. Riwayat Revisi
| Versi | Tanggal | Perubahan | Oleh |
|---|---|---|---|
| 0.1 | 2026-11-28 | Draf awal berdasarkan walkthrough D07 | ghatfani |

## 6. Ketergantungan pada Test Interface Layer
| Interface keyword | Status | Keterangan |
|---|---|---|
| Open Page | Ada (D04) | |
| Input Text Into Field | Ada (D04) | |
| Click Element | Ada (D04) | |
| Verify URL Contains | Ada (D04) | |
| Verify Field Has Value | Ada (D04) | |
| Verify Element Is Visible | **Direncanakan D08** | Dipakai DK-CON-04, DK-ORD-05/06/08 |
| Wait For Element | **Direncanakan D08** | Dipakai DK-CON-06 |
| Verify Element Text Is Not Empty | **Direncanakan D08** | Dipakai DK-CON-06 |
| Verify Element Text Contains | **Direncanakan D08** | Dipakai DK-ORD-08 |
