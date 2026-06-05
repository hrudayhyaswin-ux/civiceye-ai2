# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

from flask import Blueprint, request

from ..utils.response import ok

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    print(f"DEBUG: Login request headers: {dict(request.headers)}")
    return ok({"token": "demo-admin-token", "role": "admin"}, "demo login")

