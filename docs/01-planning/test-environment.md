# Test Environment (Draf, D01)

> Status: DRAF, diperbarui D02 (SUT lokal via Docker berjalan).
> Penanggung jawab: Ghatfani Muhammad Ilham (Test Automation Expert, D.4)
> Terkait: Pertemuan 1 | ISO/IEC/IEEE 29119-5:2024 Cl.7 (komponen framework, tailored)

## 1. Mesin Uji (Workstation Automation Expert)
| Item | Nilai |
|------|-------|
| OS | Windows 11 (64-bit) |
| RAM / CPU | Lenovo LOQ 15 (16 GB RAM) |
| Shell | PowerShell (5.1.26100.9818) |

## 2. Toolchain
| Tool | Versi terpasang | Fungsi | Pertemuan |
|------|-----------------|--------|-----------|
| Git | 2.56.1 | Version control, PR workflow | Semua |
| Python | 3.10.6 | Runtime Robot Framework & pytest | P5, P6, P10 |
| Node.js / npm | v26.13.1 / 11.20.0 | Runtime Browser library (Playwright) | P10 |
| Robot Framework | 7.5.1 | Execution engine keyword-driven | P10, P11 |
| robotframework-browser | 20.6.0 | Test Interface Layer (Web) | P10 |
| robotframework-seleniumlibrary | 6.9.0 | Alternatif Test Interface Layer (Web) | P10 |
| robotframework-requests | 0.9.7 | Test Interface Layer (API) | P12 |
| robotframework-datadriver | 1.11.2 | Data-driven dari CSV (Cl.5.4/6.4) | P10 |
| pytest + pytest-cov | 9.2.0 / 7.1.0 | Unit & integration test, coverage | P5, P6 |
| jsonschema | 4.26.0 | Validasi keywords.*.json vs kwd_schema.json | P16 |
| Docker Desktop | 29.9.3 | Menjalankan SUT lokal | P2 |
| k6 | v2.4.0 | Performance testing (lokal saja) | P13 |
| OWASP ZAP | 2.17.0 | Security scan baseline (lokal saja) | P14 |

## 3. Cara Reproduksi Environment
1. Instal tool di bagian 2 (winget).
2. python -m venv .venv lalu aktifkan (.\.venv\Scripts\Activate.ps1).
3. pip install -r automation/requirements.txt
4. fbrowser init
5. Verifikasi dengan perintah di bagian 4.

## 4. Verifikasi
Output verifikasi tersimpan di evidence/ghatfani/d01/env-versions.txt dan evidence/ghatfani/d01/pip-freeze.txt.

## 5. Batasan & Etika
- Performance dan security testing hanya pada instance lokal/Docker milik tim.
- Tidak melakukan load test atau scan terhadap situs pihak ketiga tanpa izin tertulis.

## 7. SUT Lokal (D02)
| Item | Nilai |
|------|-------|
| SUT | Wave Projects Center.ID v0.1.0 (sut-wave-projects:0.1.0-local + mysql:8.0.40) |
| Sumber | Source code lokal tim (sut/wave-projects/, di-ignore oleh Git) |
| Menjalankan | `docker compose -f automation/docker-compose.sut.yml up -d` |
| Menghentikan | `docker compose -f automation/docker-compose.sut.yml down` |
| URL UI | http://localhost:3000 (Login: http://localhost:3000/login) |
| URL API | http://localhost:3000/api/v1/portfolios (serta /api/v1/settings, /api/v1/login) |
| Binding | 127.0.0.1 saja (tidak terekspos jaringan) |
| Akun uji | Dibuat saat smoke test (data dummy lokal; kredensial nyata tidak disimpan di repo) |
| Reset data | `docker compose -f automation/docker-compose.sut.yml down -v` lalu `up -d` |
| Smoke manual | `evidence/ghatfani/d02/smoke-manual.md` |

## 8. Catatan Pembaruan
| Hari | Perubahan | Oleh |
|------|-----------|------|
| D01 | Draf awal toolchain | ghatfani |
| D02 | SUT lokal via Docker + smoke manual | ghatfani |
