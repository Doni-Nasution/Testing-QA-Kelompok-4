# Pemetaan STLC ke ISO/IEC/IEEE 29119-2 dan Bab Laporan

**Versi**: 0.1 | **Penulis**: Doni Nasution (QA Lead) | **Hari**: D02 | **Pertemuan**: P2

## 1. Tujuan
Menyelaraskan fase *Software Testing Life Cycle* (STLC) dengan proses uji pada
ISO/IEC/IEEE 29119-2 (Test Processes), lalu menautkannya ke bab laporan dan
artefak repositori, agar setiap aktivitas proyek dapat ditelusuri.

## 2. Pemetaan Utama

| Fase STLC | Proses 29119-2 | Kelompok Proses | Artefak Proyek | Bab Laporan | Hari | Penanggung Jawab |
|---|---|---|---|---|---|---|
| Analisis kebutuhan | Test Planning (analisis konteks & risiko) | Test Management | requirement, traceability-matrix | Bab 2-3 | D03, D08 | FY, DN |
| Perencanaan uji | Test Planning Process | Test Management | test-plan.md, tailored-conformance.md, nfr-test-plan.md, uat/UAT-plan.md | Bab 3-4 | D03, D04, D07, D09 | DN |
| Strategi & kontrol | Test Monitoring and Control Process | Test Management | logs/daily/*, regression-strategy.md, defect-process.md | Bab 4, 10 | D01-D21, D12, D17 | DN |
| Desain & implementasi uji | Test Design & Implementation Process | Dynamic Test | system-test-scenarios.md, unit-strategy.md, keyword library, framework-architecture.md | Bab 5-7 | D05, D08, D10 | FG, GI, DN |
| Setup environment & data | Test Environment & Data Management Process | Dynamic Test | Docker environment, test data | Bab 6 | D02, D10 | GI |
| Eksekusi uji | Test Execution Process | Dynamic Test | execution-logs/, unit-integration/ | Bab 8 | D11-D16 | GI, FG, DN |
| Pelaporan insiden/defect | Test Incident Reporting Process | Dynamic Test | bug-reports/, GitHub Issues, bug-summary.csv | Bab 9 | D14, D17 | DN, semua |
| Penutupan uji | Test Completion Process | Test Management | test-summary.md, laporan-final.pdf, tag v1.0.0 | Bab 10-11 | D18, D21 | DN |
| Tata kelola uji organisasi | Organizational Test Process | Organizational | CONTRIBUTING.md, roles-raci.md, aturan Git | Bab 1 | D01 | DN |

## 3. Pemetaan Bab Laporan (usulan)

| Bab | Judul | Sumber Artefak |
|---|---|---|
| 1 | Pendahuluan & tata kelola proyek | README, CONTRIBUTING, roles-raci |
| 2 | Objek uji & analisis kebutuhan | requirement, traceability-matrix |
| 3 | Perencanaan pengujian | test-plan, tailored-conformance |
| 4 | Strategi uji (regresi, API, UAT) | regression-strategy, api-test-strategy, UAT-plan |
| 5 | Desain uji unit & sistem | unit-strategy, system-test-scenarios |
| 6 | Arsitektur framework & environment | framework-architecture, environment |
| 7 | Pengujian non-fungsional (performa, keamanan) | nfr-test-plan, performance & security plan |
| 8 | Eksekusi pengujian | execution-logs |
| 9 | Manajemen defect | defect-process, bug-summary |
| 10 | Ringkasan hasil uji & metrik | test-summary |
| 11 | Kesimpulan & pembelajaran | - |
| 12 | Wawancara QA profesional | interview-guide, interview-notes |
| 13 | Validasi oleh QA profesional | validation-package, validation-feedback |
| 14 | Tren masa depan QA | bab-14 |

## 4. Catatan Kesesuaian (Conformance)
- Klaim kesesuaian bersifat *tailored* dan difinalisasi pada D04 (`tailored-conformance.md`).
- Pemetaan ini akan diperbarui bila ada perubahan struktur laporan dari dosen.

## 5. Riwayat Revisi

| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1 | [DD-MM-2026] | Draf awal pemetaan STLC, 29119-2, dan bab laporan |
