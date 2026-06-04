# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import json
import os

from flask import Blueprint, current_app, request

from ..services.complaint_service import create_complaint, get_complaint
from ..utils.response import fail, ok
from ..utils.validators import validate_complaint

complaint_bp = Blueprint("complaints", __name__)


@complaint_bp.post("/complaints")
def submit_complaint():
    if request.is_json:
        payload = request.get_json()
    else:
        # Handle multipart/form-data
        payload = request.form.to_dict()

        # Parse JSON string back to dict if it exists
        if "location" in payload and isinstance(payload["location"], str):
            try:
                payload["location"] = json.loads(payload["location"])
            except Exception:
                payload["location"] = {}

        # Handle attachments
        attachments = []
        upload_dir = os.path.join(current_app.root_path, "..", "uploads", "media")
        os.makedirs(upload_dir, exist_ok=True)

        for key in request.files:
            if key.startswith("attachment_"):
                file = request.files[key]
                if file.filename:
                    # Generate a safe filename to prevent overwrites or directory traversal
                    import uuid
                    ext = os.path.splitext(file.filename)[1]
                    safe_name = f"{uuid.uuid4().hex}{ext}"
                    file.save(os.path.join(upload_dir, safe_name))
                    attachments.append(safe_name)
        payload["attachments"] = attachments

        # Handle voice note
        if "voice_note" in request.files:
            payload["voice_note"] = request.files["voice_note"]

    # Debug log to see what the backend is actually receiving
    print(f"DEBUG: Received payload keys: {list(payload.keys())}")

    error = validate_complaint(payload)
    if error:
        return fail(error, 422)
    return ok(create_complaint(payload), "complaint submitted", 201)


@complaint_bp.get("/complaints/<ticket_id>")
def track_complaint(ticket_id):
    complaint = get_complaint(ticket_id.upper())
    if not complaint:
        return fail("Ticket not found", 404)
    return ok(complaint)

