# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

def validate_complaint(payload):
    missing = []
    if not payload.get("title"):
        missing.append("title")
    if not payload.get("description") and not payload.get("voice_note"):
        missing.append("description")

    if missing:
        return f"Missing required field: {', '.join(missing)}"
    return None
