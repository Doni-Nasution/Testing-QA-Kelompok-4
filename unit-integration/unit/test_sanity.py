"""Tes sanity runner (D05). Bukan unit test SUT."""
import sys

import pytest


def test_python_version_supported():
    assert sys.version_info >= (3, 10)


def test_pytest_is_available():
    assert pytest.__version__


def test_requests_importable():
    import requests  # dipakai integration test (D06)

    assert requests.__version__