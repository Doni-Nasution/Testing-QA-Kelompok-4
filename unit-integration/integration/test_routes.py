"""Integration test: rute halaman & aset frontend pada SUT (read-only).

Integrasi yang diuji: browser-facing route <-> server Next.js <-> aset statis (CDN Vercel).
"""
import re

import pytest

IT_ID = "IT-TBD"  # Menunggu sinkronisasi final integration-test-design.md (Fiyado)
ROUTES = ["/", "/chat", "/checkout"]


@pytest.mark.parametrize("path", ROUTES)
def test_route_returns_html_page(call, record_property, path):
    record_property("it_id", IT_ID)
    response = call("GET", path)
    assert response.status_code == 200
    assert "text/html" in response.headers.get("Content-Type", "")
    assert response.elapsed.total_seconds() < 10  # sanity saja; performa resmi di D15


def test_unknown_route_returns_404(call, record_property):
    record_property("it_id", IT_ID)
    response = call("GET", "/halaman-tidak-ada-qa-kelompok4")
    # Jika gagal (mis. 200 dengan halaman kustom), catat sebagai observasi, bukan otomatis bug.
    assert response.status_code == 404


def test_home_static_assets_are_served(call, record_property):
    record_property("it_id", IT_ID)
    home = call("GET", "/")
    assets = list(dict.fromkeys(re.findall(r"(/_next/static/[^\"'\s>]+\.(?:js|css))", home.text)))
    assert assets, "Tidak ada referensi aset /_next/static di HTML beranda"
    for asset in assets[:2]:
        response = call("GET", asset)
        assert response.status_code == 200, asset
