# Unit & Integration Testing (P5, P6)

Penanggung jawab runner/CI: Ghatfani (Test Automation Expert, D.4).

## Struktur
| Folder | Isi | Dijalankan di CI? |
|---|---|---|
| `unit/` | Unit test (pytest), tanpa jaringan | Ya |
| `integration/` | Integration test (D06), menyentuh SUT/API | Tidak (marker `integration`) |

## Menjalankan lokal (Windows/PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
cd unit-integration
pytest unit --cov --cov-config=.coveragerc --cov-report=term-missing --cov-report=html
start htmlcov\index.html
```

## Konvensi
- Berkas `test_*.py`, fungsi `test_*`; satu perilaku per tes, nama deskriptif.
- Tes unit tidak boleh memanggil jaringan/SUT live.
- Tes yang membutuhkan jaringan diberi `@pytest.mark.integration`.
- Hasil (`coverage.xml`, `htmlcov/`, `junit.xml`) tidak di-commit (lihat `.gitignore`).

## Target coverage
| Item | Nilai |
|---|---|
| Kode yang diukur | N/A, kode sumber SUT tidak tersedia di repositori (SUT berupa aplikasi web Next.js terpisah) |
| Baseline | N/A (hanya menjalankan `test_sanity.py` pada D05) |
| Ambang (`fail_under`) | Belum diaktifkan |

## CI
Workflow: `.github/workflows/ci-unit.yml` (PR ke `develop`/`main`, push ke `develop`).
Artefak: `unit-test-results` (junit, coverage xml, htmlcov).

## Keterkaitan standar
Unit level (Pertemuan 5) pada hierarki pengujian. Penyesuaian terhadap ketersediaan kode sumber SUT dinyatakan di `docs/01-planning/tailored-conformance.md`.