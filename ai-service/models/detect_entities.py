# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

def detect_entities(description, location):
    words = description.split()
    landmark = location.get("address") or " ".join(words[:4])
    return {
        "landmark": landmark,
        "mentioned_people": [word for word in words if word.istitle()][:3],
        "ward": location.get("ward") or "unknown",
    }

