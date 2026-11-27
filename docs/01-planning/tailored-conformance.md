# Klaim Tailored Conformance (Draf D03)

| Item | Nilai |
|---|---|
| Standar | ISO/IEC/IEEE 29119-5:2024 (2nd ed.), Keyword-driven testing |
| Standar terkait | 29119-1:2022, 29119-2:2021, 29119-3:2021, 29119-4:2021 |
| Penyusun draf | Ghatfani Muhammad Ilham (GI — Test Automation Expert [D.4]) |
| Reviewer / finalisasi | Doni Nasution (DN — QA Lead / Test Manager), target D04 |
| Status | DRAF v0.1, 2026-11-24 |

> Redaksi klaim dan nomor klausul dicocokkan dengan salinan standar resmi sebelum final.

## 1. Pernyataan Klaim (Cl.4.3)
Kelompok 4 mengklaim **tailored conformance** terhadap ISO/IEC/IEEE 29119-5:2024
untuk kegiatan pengujian berbasis keyword pada SUT Wave Projects. Komponen framework
(Clause 7) yang digunakan, disesuaikan, atau dihilangkan beserta justifikasinya
dinyatakan pada Bagian 4. Klaim tidak mencakup apa pun yang tidak tercantum di
Bagian 4, dan keterbatasannya dinyatakan di Bagian 6.

## 2. Objek yang Diuji dan Konteks Tailoring
| Faktor | Kondisi | Pengaruh ke tailoring |
|---|---|---|
| SUT | Web app skala kecil-menengah (beranda `/`, `/chat` AI, `/checkout`) | Cakupan keyword terbatas pada 3 area fungsi utama |
| Akses | Remote black-box di produksi (`wave-projects-center-id.vercel.app`) + sandbox Docker lokal | Pengujian destruktif/otomasi berat diisolasi ke Docker lokal |
| Lingkungan | Deployment produksi bersama (Vercel + TiDB + Midtrans), izin pemilik dalam konfirmasi | Performa/security di produksi hanya laju rendah dengan izin tertulis |
| Tim & waktu | 4 mahasiswa, 21 hari | Framework off-the-shelf; peran merangkap |
| Dinamika SUT | AI chat (Gemini) nondeterministik; pembayaran pihak ketiga (Midtrans) | Oracle berbasis struktur/perilaku; tidak ada transaksi nyata |

## 3. Peran (Annex D, selaras dengan `roles-raci.md`)
| Peran 29119-5 | Anggota (Kode) | Penyesuaian |
|---|---|---|
| QA Lead / Test Manager | Doni Nasution (DN) | Tata kelola repo, rilis, test plan, komunikasi eksternal, laporan final |
| Domain Expert [D.2] | Fiyado Yudha Witama (FY) | Requirement & domain, reviewer PR DN, merangkap UAT |
| Test Designer [D.3] | Fitrah Gisma Ripan (FG) | Desain uji, skenario, traceability |
| Test Automation Expert [D.4] | Ghatfani Muhammad Ilham (GI) | Environment, runner, keyword library, otomasi, merangkap performa/security |

Penyesuaian: satu orang memegang lebih dari satu aktivitas karena jumlah tim 4 orang.

## 4. Komponen Framework (Clause 7): Status & Justifikasi
Status: **Dipakai** / **Disesuaikan** / **Dihilangkan**.

| # | Komponen | Klausul | Status | Implementasi di proyek | Justifikasi |
|---|---|---|---|---|---|
| 1 | Keyword Library / Dictionary | 7.2.8 | Dipakai | `keyword-library/` | Inti pendekatan keyword-driven; memuat nama, parameter, default, deskripsi |
| 2 | Domain Layer (composite/high-level keyword) | 7.2.8 / `<..>` | Dipakai | `keyword-library/domain/`, `automation/resources/domain/` | Menjaga test case terbaca oleh Domain Expert |
| 3 | Test Interface Layer (simple/low-level keyword): Web | 7.3.2 | Dipakai | `keyword-library/interface/web.md`, Robot Browser/Selenium | UI web adalah antarmuka utama SUT |
| 4 | Test Interface Layer: API | 7.3.2 | Disesuaikan | `interface/api.md`, RequestsLibrary | Endpoint dipetakan lewat observasi DevTools & inspeksi rute (`/api/v1/*`); tidak ada dokumen OpenAPI resmi |
| 5 | Pemisahan Navigation (input) vs Verification (output) | `<..>` | Dipakai | Tiap keyword diberi tipe | Memudahkan penggunaan ulang dan analisis kegagalan |
| 6 | Konvensi nama keyword (kata kerja imperatif) | Annex A | Dipakai | `keyword-library/README.md` | Konsistensi dan keterbacaan |
| 7 | Dokumentasi keyword (nama, parameter, default, deskripsi) | Tabel F.1 | Dipakai | `keyword-library/*.md` | Syarat dosen dan keterlacakan |
| 8 | Keyword Test Cases (TD3) | 6.6.4 | Dipakai | `test-cases/keyword-test-cases/` | Menurunkan uji dari requirement |
| 9 | Test Procedures (TD4) | 6.6.5, Tabel F.4 | Dipakai | `test-cases/test-procedures/` | Pemisahan prosedur dan data |
| 10 | Data-Driven Testing | 5.4, 6.4 | Dipakai | `test-data/*.csv` + DataDriver | Kombinasi data tanpa duplikasi prosedur |
| 11 | Execution engine & adapter | `<..>` | Disesuaikan | Robot Framework (off-the-shelf) | Tidak membangun engine sendiri: skala kecil, 21 hari; Robot native keyword-driven |
| 12 | Status hasil eksekusi | 5.3.4 | Dipakai | `execution-logs/*.csv` | PASS / FAIL / BLOCKED |
| 13 | Format pertukaran keyword (JSON) | Annex G | Dipakai | `keyword-library/keywords.*.json`, divalidasi vs `kwd_schema.json` | Interoperabilitas; divalidasi D19 |
| 14 | Pengelolaan keyword (repositori/versi) | `<..>` | Disesuaikan | Git + PR + review silang | Cukup untuk skala tim; tanpa tool KM khusus |
| 15 | Tool manajemen uji khusus | `<..>` | Dihilangkan | GitHub Issues + Markdown/CSV | Biaya/kompleksitas tidak sebanding dengan skala |
| 16 | Pembuatan keyword otomatis berbasis AI/model | - | Dihilangkan | - | Di luar lingkup standar dan proyek |

## 5. Keterkaitan dengan Bagian Standar Lain
| Standar | Dipakai untuk | Artefak |
|---|---|---|
| 29119-1:2022 | Konsep dan terminologi | Glosarium, Bab II |
| 29119-2:2021 | Proses uji (perencanaan, desain, eksekusi, pelaporan) | `test-plan.md`, `stlc-mapping.md` |
| 29119-3:2021 | Dokumentasi uji | Test plan, test summary |
| 29119-4:2021 | Teknik desain uji (EP, BVA, decision table, state transition) | `bb-test-design-techniques.md` |

## 6. Keterbatasan Klaim
- Klaim hanya berlaku untuk 3 area fungsi SUT yang disebut di Bagian 2.
- Uji performa/security hanya dalam batas izin pemilik dan pada laju rendah.
- Fitur AI chat diuji pada perilaku/struktur respons, bukan akurasi isi.
- Pembayaran nyata (Midtrans) tidak diuji.

## 7. Butir Terbuka
| # | Butir | PIC | Status |
|---|---|---|---|
| 1 | Izin tertulis pemilik SUT untuk uji performa/security ringan | Doni (DN) | Menunggu |
| 2 | Konfirmasi URL preview/staging Vercel & Midtrans sandbox | Doni (DN) / Fiyado (FY) | Menunggu |
| 3 | Isi kolom `<..>` dari standar resmi ISO/IEC/IEEE 29119-5:2024 | Ghatfani (GI) | Menunggu |
| 4 | Cocokkan nama komponen dengan judul Clause 7 | Ghatfani (GI) | Menunggu |

## 8. Riwayat Revisi
| Versi | Tanggal | Perubahan | Oleh |
|---|---|---|---|
| 0.1 | 2026-11-24 | Draf awal | ghatfani |
