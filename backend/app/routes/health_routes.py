# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

from flask import Blueprint

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    return {"status": "healthy", "service": "civiceye-backend"}

