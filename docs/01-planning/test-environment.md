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

## 7. SUT & Lingkungan Pengujian (Diperbarui D03)
| Item | Nilai |
|------|-------|
| SUT | Wave Projects Center.ID (Next.js, Tailwind, TiDB/MySQL, Vercel, Midtrans, Gemini AI) |
| URL Produksi (Utama) | https://wave-projects-center-id.vercel.app (canonical: waveprojects.my.id) |
| Sandbox Lokal (Isolasi) | Docker Compose (`automation/docker-compose.sut.yml`, `127.0.0.1:3000`, `mysql:8.0.40`) |
| Jenis akses | Remote black-box via browser/HTTP untuk produksi; white/grey-box terisolasi di Docker lokal |
| Halaman utama | `/` (beranda), `/chat` (konsultasi AI), `/checkout` (pemesanan), `/login` (portal internal) |
| Status izin pengujian | Menunggu konfirmasi tertulis pemilik untuk uji performa/security ringan pada URL produksi |
| Kode sumber | Tersedia secara lokal untuk analisis struktur & Docker sandbox (`sut/wave-projects/`, di-ignore Git) |
| Staging/preview | Belum ada URL preview Vercel terpisah; menggunakan Docker lokal sebagai lingkungan isolasi |
| Smoke manual | `evidence/ghatfani/d02/smoke-manual.md` |

### Pembatasan pengujian
- Tidak menyelesaikan pembayaran nyata (Midtrans) pada lingkungan produksi.
- `/chat` (AI): uji manual terbatas karena memakai kuota/biaya pemilik; verifikasi pada struktur & perilaku respons.
- Performance dan security test pada URL produksi hanya dilakukan setelah ada izin tertulis pemilik dengan laju rendah (non-destruktif), atau dijalankan pada sandbox Docker lokal.

## 8. Catatan Pembaruan
| Hari | Perubahan | Oleh |
|------|-----------|------|
| D01 | Draf awal toolchain | ghatfani |
| D02 | SUT lokal via Docker + smoke manual Wave Projects | ghatfani |
| D03 | Pembaruan profil SUT produksi Wave Projects & pembatasan pengujian | ghatfani |
