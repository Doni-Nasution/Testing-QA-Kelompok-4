# Panduan Kontribusi

## 1. Branching
- **Dilarang push langsung** ke `main` dan `develop`.
- Setiap hari buat branch baru dari `develop`:
  `feat/<kode>/dXX-<topik-singkat>`, contoh `feat/doni/d03-test-plan`.

```bash
git checkout develop
git pull --rebase origin develop
git checkout -b feat/<kode>/dXX-<topik>
```

## 2. Commit
Format: `<type>(<scope>): <deskripsi imperatif singkat> [Dxx][P<n>][<kode>]`

Type: `docs` | `feat` | `test` | `fix` | `chore` | `ci` | `data`

Contoh: `docs(plan): add test plan v0.1 [D03][P3][doni]`

## 3. Sinkronisasi & Deadline
- Minimal **1 commit bermakna per hari**.
- Jalankan `git pull --rebase origin develop` sebelum push.
- Push sebelum **21:00 WIB**.

## 4. Pull Request
- PR dari branch harian ke `develop`, isi sesuai template.
- Minta approval reviewer yang ditetapkan (lihat `docs/01-planning/roles-raci.md`).
- Merge dengan **Merge commit**. **Dilarang squash/rebase merge** agar riwayat commit individu terlihat.

## 5. Artefak Harian (Anti-Conflict)
- Bukti: `evidence/<kode>/dXX/`
- Log harian: `logs/daily/<kode>/dXX.md`
- Jangan mengedit file milik anggota lain tanpa koordinasi.

## 6. Rilis
Hanya QA Lead yang menggabungkan `develop` ke `main` dan membuat tag
(`v0.1`, `v0.2`, `v0.3`, `v1.0.0`).
