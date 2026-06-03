# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

from flask import Blueprint, request

from ..services.complaint_service import list_complaints, stats, update_status
from ..utils.enums import STATUSES
from ..utils.response import fail, ok

admin_bp = Blueprint("admin", __name__)


@admin_bp.get("/complaints")
def complaints():
    filters = {
        "status": request.args.get("status"),
        "priority": request.args.get("priority"),
        "department": request.args.get("department"),
        "q": request.args.get("q"),
    }
    return ok(list_complaints({key: value for key, value in filters.items() if value}))


@admin_bp.patch("/complaints/<ticket_id>")
def patch_complaint(ticket_id):
    payload = request.get_json(silent=True) or {}
    status = payload.get("status")
    if status not in STATUSES:
        return fail("Invalid status", 422)
    complaint = update_status(ticket_id.upper(), status)
    if not complaint:
        return fail("Ticket not found", 404)
    return ok(complaint)


@admin_bp.get("/stats")
def dashboard_stats():
    return ok(stats())

