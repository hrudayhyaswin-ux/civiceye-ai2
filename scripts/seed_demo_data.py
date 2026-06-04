# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "backend"))

from app import create_app  # noqa: E402
from app.services.complaint_service import create_complaint  # noqa: E402

DEMO_COMPLAINTS = [
    {"title": "Open manhole near bus stop", "description": "Danger near school gate and bus stop. Needs urgent barricading.", "category_hint": "Road Damage", "location": {"address": "MG Road, Ward 12"}},
    {"title": "Garbage overflow", "description": "Same issue again, waste is blocking the footpath.", "category_hint": "Garbage", "location": {"address": "Lake View Colony"}},
    {"title": "Street light not working", "description": "Dark stretch near metro station after 8 PM.", "category_hint": "Street Light", "location": {"address": "Metro Pillar 44"}},
]


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        for payload in DEMO_COMPLAINTS:
            complaint = create_complaint(payload)
            print(f"Seeded {complaint['ticket_id']}: {complaint['title']}")

