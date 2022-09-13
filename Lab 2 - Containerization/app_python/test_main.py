from datetime import datetime

from fastapi.testclient import TestClient
from pytz import timezone

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    moscow = timezone('Europe/Moscow')
    assert response.json() == {"Moscow time": datetime.now(moscow).strftime("%H:%M:%S")}
