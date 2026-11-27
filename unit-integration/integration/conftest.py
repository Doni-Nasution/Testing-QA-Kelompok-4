"""Fixture & kebijakan keselamatan untuk integration test (D06, P6).

Default: read-only, throttle 1 detik, satu session, User-Agent teridentifikasi.
Tes bertanda `write` hanya jalan bila ALLOW_WRITE=1 (butuh izin pemilik / staging).
"""
import os
import time

import pytest
import requests

BASE_URL = os.getenv("SUT_BASE_URL", "https://wave-projects-center-id.vercel.app").rstrip("/")
ALLOW_WRITE = os.getenv("ALLOW_WRITE") == "1"
THROTTLE_SECONDS = float(os.getenv("THROTTLE_SECONDS", "1.0"))
TIMEOUT_SECONDS = 15
USER_AGENT = "QA-Student-Project/Kelompok4 (integration-test; read-only)"


def pytest_collection_modifyitems(items):
    """Semua tes di folder ini otomatis bertanda `integration`; `write` di-skip secara default."""
    skip_write = pytest.mark.skip(reason="tes write: set ALLOW_WRITE=1 setelah ada izin pemilik/staging")
    for item in items:
        item.add_marker(pytest.mark.integration)
        if item.get_closest_marker("write") and not ALLOW_WRITE:
            item.add_marker(skip_write)


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def http():
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    yield session
    session.close()


@pytest.fixture(autouse=True)
def throttle():
    """Jeda antar tes agar tidak membebani SUT produksi."""
    yield
    time.sleep(THROTTLE_SECONDS)


@pytest.fixture
def call(http, base_url):
    """call('GET', '/path', **kwargs) -> requests.Response, dengan timeout tetap."""

    def _call(method, path, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT_SECONDS)
        return http.request(method, f"{base_url}{path}", **kwargs)

    return _call
