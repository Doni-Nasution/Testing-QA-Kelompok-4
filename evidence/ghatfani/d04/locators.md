# Locator Hasil Inspeksi: D04
Tanggal: 2026-11-25 | Penguji: Ghatfani | Metode: Gray-box (Chrome DevTools Inspect + inspeksi komponen Next.js)

| Elemen | Halaman | Locator terpilih | Alasan | Alternatif |
|--------|---------|------------------|--------|------------|
| Link menu "AI Chat" | `/` | `css=a[href$="/chat"] >> nth=0` | Atribut `href` stabil mengarah ke `/chat`; `nth=0` mencegah *strict mode violation* | `text=AI Chat` |
| Kolom input chat | `/chat` | `css=input[placeholder="Ceritakan proyek impian Anda..."]` | Elemen `<input>` di `/chat` tidak memiliki atribut eksplisit `type="text"` dan memakai class Tailwind dinamis; atribut `placeholder` unik dan stabil | `css=main input >> nth=0` |
