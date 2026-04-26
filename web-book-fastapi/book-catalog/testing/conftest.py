import os
import pytest


def pytest_configure(config):
    if not os.getenv("TESTING"):
        pytest.exit("ERROR: Переменная TESTING не установлена. Запустите с TESTING=1")