from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import create_app


class TestConfig:
    TESTING = True
    AI_SERVICE_URL = "http://localhost:9999"
    DATABASE_PATH = str(Path("/tmp/civiceye-test.db"))


def test_submit_and_track_complaint():
    Path(TestConfig.DATABASE_PATH).unlink(missing_ok=True)
    client = create_app(TestConfig).test_client()
    response = client.post("/api/complaints", json={"title": "Open drain", "description": "Danger near school", "category_hint": "Drainage"})
    assert response.status_code == 201
    ticket_id = response.json["data"]["ticket_id"]

    tracked = client.get(f"/api/complaints/{ticket_id}")
    assert tracked.status_code == 200
    assert tracked.json["data"]["priority"] == "High"
