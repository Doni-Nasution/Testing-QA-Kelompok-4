"""Integration test berbasis data: kontrak endpoint API (status, content-type, kunci JSON).

Endpoint dibaca dari api_endpoints.csv. Baris enabled=1 saja yang dijalankan.
Baris write=1 hanya jalan jika ALLOW_WRITE=1 (lihat conftest.py).
"""
import csv
from pathlib import Path

import pytest

CSV_PATH = Path(__file__).with_name("api_endpoints.csv")


def _rows():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r["enabled"].strip() == "1"]


def _params():
    params = []
    for row in _rows():
        marks = [pytest.mark.write] if row["write"].strip() == "1" else []
        params.append(pytest.param(row, id=row["id"], marks=marks))
    return params


@pytest.mark.parametrize("row", _params())
def test_api_endpoint_contract(call, record_property, row):
    record_property("it_id", row["it_id"])
    kwargs = {}
    if row["body_json"].strip():
        import json

        kwargs["json"] = json.loads(row["body_json"])

    response = call(row["method"].strip().upper(), row["path"].strip(), **kwargs)

    assert response.status_code == int(row["expect_status"])
    expected_type = row["expect_content_type"].strip()
    if expected_type:
        assert expected_type in response.headers.get("Content-Type", "")

    keys = [k for k in row["required_json_keys"].split("|") if k.strip()]
    if keys:
        payload = response.json()
        if isinstance(payload, list):
            assert payload, "Respons list kosong; tidak bisa memeriksa kunci"
            payload = payload[0]
        for key in keys:
            assert key in payload, f"Kunci '{key}' tidak ada di respons"
