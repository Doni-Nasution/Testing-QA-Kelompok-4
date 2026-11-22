# Peran & RACI

Acuan: ISO/IEC/IEEE 29119-5:2024 Annex D.

## Peran

| Anggota | Kode | Peran 29119-5 | Fokus |
|---|---|---|---|
| Doni Nasution | DN | QA Lead / Test Manager | Tata kelola repo, rilis, test plan, komunikasi eksternal, laporan final |
| Fiyado Yudha Witama | FY | Domain Expert [D.2] | Requirement & domain, reviewer PR DN |
| Fitrah Gisma Ripan | FG | Test Designer [D.3] | Desain uji, skenario, traceability |
| Ghatfani Muhammad Ilham | GI | Test Automation Expert [D.4] | Environment, runner, keyword library, otomasi |

## Rantai Review PR

| Penulis PR | Reviewer/Approver |
|---|---|
| DN | FY |
| GI | DN (Merge commit) |
| FG | [DISEPAKATI saat kick-off] |
| FY | [DISEPAKATI saat kick-off] |

## RACI (R=Responsible, A=Accountable, C=Consulted, I=Informed)

| Aktivitas | DN | FY | FG | GI |
|---|---|---|---|---|
| Setup repo & proteksi branch | A/R | I | I | I |
| Test plan & strategi (regresi, API, perf, security) | A/R | C | C | C |
| Requirement & traceability | A | R | R | C |
| Desain test case & skenario | A | C | R | C |
| Environment, framework & otomasi | A | I | C | R |
| Unit test | R | C | C | R |
| Wawancara & validasi QA profesional | A/R | C | R (pencatat) | I |
| Rilis & tagging milestone | A/R | I | I | I |
| Laporan final | A/R | R | R | R |

## Aturan Kerja
- Tidak ada push langsung ke `main`/`develop`.
- Push harian sebelum 21:00 WIB.
- Merge PR memakai Merge commit.
