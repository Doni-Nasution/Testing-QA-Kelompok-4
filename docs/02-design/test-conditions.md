# Test Conditions

## 1. Identitas Dokumen

| Informasi | Keterangan |
|---|---|
| Nama Dokumen | Test Conditions |
| Sistem yang Diuji | Wave Projects Center.ID |
| Standar Acuan | ISO/IEC/IEEE 29119-5:2024 |
| Hari | Day 3 |
| Penyusun | Fitrah Gisma Ripan |
| Peran | Test Designer (D.3) |
| Status Dokumen | Draft untuk review |

## 2. Tujuan

Dokumen ini berisi kondisi pengujian yang diturunkan dari Functional Requirements (FR), Non-Functional Requirements (NFR), dan Acceptance Criteria (AC) pada dokumen requirements inventory.

Test conditions digunakan sebagai dasar penyusunan test case dan pengembangan keyword-driven testing.

## 3. Ruang Lingkup

Kondisi pengujian mencakup:

1. Homepage dan navigasi website.
2. Informasi portofolio dan layanan.
3. Informasi dan pemilihan paket.
4. Konsultasi AI.
5. Checkout dan validasi formulir.
6. Autentikasi pengguna.
7. Pembayaran.
8. Pembatasan hak akses portal.
9. Kebutuhan nonfungsional sistem.

Pengujian transaksi, pembayaran, dan portal internal hanya dilakukan setelah lingkungan serta akun pengujian mendapat izin.

## 4. Test Conditions Functional Requirements

| Test Condition ID | Requirement ID | Acceptance Criteria | Kondisi Pengujian | Jenis | Prioritas |
|---|---|---|---|---|---|
| TCN-011 | FR-001 | AC-001 | Memastikan homepage dapat diakses dan informasi utama ditampilkan. | Positive | Medium |
| TCN-012 | FR-002 | AC-002 | Memastikan pengguna dapat membuka halaman portofolio. | Positive | Medium |
| TCN-013 | FR-003 | AC-003 | Memastikan informasi layanan dapat ditampilkan. | Positive | Medium |
| TCN-014 | FR-004 | AC-004 | Memastikan pilihan paket dan harga ditampilkan dengan benar. | Positive | High |
| TCN-015 | FR-005 | AC-005 | Memastikan pengguna dapat memilih paket dan sistem menampilkan pilihan tersebut. | Positive | High |
| TCN-016 | FR-006 | AC-006, AC-007 | Memastikan kolom konsultasi menerima pesan dan mencegah pengiriman pesan kosong. | Positive dan Negative | High |
| TCN-017 | FR-007 | AC-006 | Memastikan sistem memberikan respons setelah pengguna mengirim pesan konsultasi. | Positive | High |
| TCN-018 | FR-008 | AC-008 | Memastikan formulir checkout dapat diakses melalui alur pemesanan. | Positive | High |
| TCN-019 | FR-009 | AC-008, AC-009 | Memastikan formulir menyediakan input nama, email, WhatsApp, paket, dan tujuan proyek. | Positive | High |
| TCN-020 | FR-010 | AC-009, AC-010 | Memastikan sistem memvalidasi kelengkapan data pemesanan. | Positive dan Negative | High |
| TCN-021 | FR-011 | AC-011, AC-012 | Memastikan sistem memvalidasi format email dan nomor WhatsApp. | Negative | High |
| TCN-022 | FR-012 | AC-013 | Memastikan halaman login menampilkan input email, password, dan tombol Sign In. | Positive | High |
| TCN-023 | FR-013 | AC-014 | Memastikan pengguna dengan kredensial valid dapat melakukan autentikasi. | Positive | High |
| TCN-024 | FR-014 | AC-015 | Memastikan sistem menolak kredensial yang tidak valid. | Negative | High |
| TCN-025 | FR-015 | AC-016 | Memastikan proses pembayaran dapat dilakukan pada lingkungan pengujian yang diizinkan. | Positive | High |
| TCN-026 | FR-016 | AC-017 | Memastikan pengguna tanpa hak akses tidak dapat membuka portal yang dilindungi. | Negative | High |

## 5. Test Conditions Non-Functional Requirements

| Test Condition ID | Requirement ID | Kondisi Pengujian | Jenis Pengujian | Prioritas | Kriteria Tambahan |
|---|---|---|---|---|---|
| TCN-027 | NFR-001 | Mengevaluasi kemudahan pengguna memahami navigasi, informasi, dan formulir website. | Usability | High | Skenario dan kriteria penilaian perlu disepakati. |
| TCN-028 | NFR-002 | Mengukur waktu respons sistem ketika pengguna mengakses fitur utama. | Performance | High | Target waktu respons belum ditentukan. |
| TCN-029 | NFR-003 | Memeriksa perlindungan data pengguna dan kredensial pada proses autentikasi serta pemesanan. | Security | High | Ruang lingkup dan metode pengujian keamanan perlu disetujui. |
| TCN-030 | NFR-004 | Memeriksa kompatibilitas tampilan dan fungsi pada browser yang didukung. | Compatibility | Medium | Daftar browser yang didukung perlu dikonfirmasi. |
| TCN-031 | NFR-005 | Memeriksa penyesuaian tampilan website pada ukuran layar desktop dan mobile. | Responsive | Medium | Ukuran viewport pengujian perlu disepakati. |
| TCN-032 | NFR-006 | Memeriksa kemampuan sistem menangani kesalahan dan mempertahankan kondisi yang terkendali. | Reliability | High | Skenario kegagalan perlu ditentukan. |
| TCN-033 | NFR-007 | Memeriksa ketersediaan sistem selama periode pengujian yang disepakati. | Availability | High | Periode dan target ketersediaan belum ditentukan. |
| TCN-034 | NFR-008 | Memeriksa konsistensi data pemesanan setelah proses pengiriman dan pemrosesan data. | Data Integrity | High | Akses verifikasi data dan lingkungan pengujian diperlukan. |

## 6. Prioritas Pengujian

Prioritas kondisi pengujian mengikuti prioritas requirement pada dokumen requirements inventory.

- High: fitur utama yang berkaitan dengan konsultasi, pemilihan paket, checkout, validasi, autentikasi, pembayaran, keamanan, dan integritas data.
- Medium: homepage, portofolio, layanan, kompatibilitas, dan responsiveness.

Prioritas ini masih berupa rancangan dan memerlukan persetujuan tim.

## 7. Pemetaan Requirement dan Acceptance Criteria

| Requirement ID | Test Condition ID | Acceptance Criteria |
|---|---|---|
| FR-001 | TCN-011 | AC-001 |
| FR-002 | TCN-012 | AC-002 |
| FR-003 | TCN-013 | AC-003 |
| FR-004 | TCN-014 | AC-004 |
| FR-005 | TCN-015 | AC-005 |
| FR-006 | TCN-016 | AC-006, AC-007 |
| FR-007 | TCN-017 | AC-006 |
| FR-008 | TCN-018 | AC-008 |
| FR-009 | TCN-019 | AC-008, AC-009 |
| FR-010 | TCN-020 | AC-009, AC-010 |
| FR-011 | TCN-021 | AC-011, AC-012 |
| FR-012 | TCN-022 | AC-013 |
| FR-013 | TCN-023 | AC-014 |
| FR-014 | TCN-024 | AC-015 |
| FR-015 | TCN-025 | AC-016 |
| FR-016 | TCN-026 | AC-017 |
| NFR-001 | TCN-027 | Perlu kriteria terukur |
| NFR-002 | TCN-028 | Perlu target waktu respons |
| NFR-003 | TCN-029 | Perlu kriteria keamanan |
| NFR-004 | TCN-030 | Perlu daftar browser |
| NFR-005 | TCN-031 | Perlu ukuran viewport |
| NFR-006 | TCN-032 | Perlu skenario kegagalan |
| NFR-007 | TCN-033 | Perlu target ketersediaan |
| NFR-008 | TCN-034 | Perlu kriteria konsistensi data |

## 8. Asumsi dan Keterbatasan

1. Test conditions disusun berdasarkan requirements inventory yang tersedia pada repository.
2. Kondisi pengujian merupakan rancangan awal dan belum berarti fitur telah diuji atau dinyatakan lulus.
3. Test condition untuk AI Chat memerlukan verifikasi respons aktual.
4. Pengujian checkout memerlukan lingkungan yang diizinkan.
5. Pengujian pembayaran memerlukan konfirmasi mekanisme sandbox atau simulasi.
6. Pengujian autentikasi memerlukan akun pengujian yang valid dan tidak valid.
7. Pengujian hak akses memerlukan akun dengan tingkat akses berbeda.
8. Kriteria kuantitatif NFR belum ditetapkan sehingga tidak boleh diasumsikan sebagai batas penerimaan final.
9. Requirement kandidat dari observasi awal masih memerlukan validasi Domain Expert dan QA Lead.

## 9. Status dan Review

Seluruh test conditions pada dokumen ini berstatus Draft.

Review diperlukan untuk:

- Memvalidasi kesesuaian test conditions dengan kebutuhan sistem.
- Mengonfirmasi prioritas pengujian.
- Menetapkan kriteria penerimaan NFR.
- Mengonfirmasi ketersediaan lingkungan dan akun pengujian.
- Memastikan kondisi pengujian siap diturunkan menjadi test case.

## 10. Kesimpulan

Dokumen ini memuat 16 test conditions untuk Functional Requirements dan 8 test conditions untuk Non-Functional Requirements.

Total terdapat 24 test conditions yang menjadi dasar penyusunan test case pada tahap berikutnya. Seluruh kondisi masih memerlukan review dan validasi sebelum digunakan sebagai dasar pengujian final.
