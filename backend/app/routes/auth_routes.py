from flask import Blueprint

from ..utils.response import ok

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    return ok({"token": "demo-admin-token", "role": "admin"}, "demo login")

