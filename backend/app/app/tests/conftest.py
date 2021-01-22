from typing import Generator

import pytest
from fastapi.testclient import TestClient

import os
os.environ["ENV_FILE"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..', '..', '.env.test.personal')

from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
