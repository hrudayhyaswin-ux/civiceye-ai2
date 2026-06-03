# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

from flask import jsonify


def ok(data=None, message="ok", status=200):
    return jsonify({"success": True, "message": message, "data": data}), status


def fail(message, status=400):
    return jsonify({"success": False, "message": message, "data": None}), status

