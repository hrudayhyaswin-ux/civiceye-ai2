# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import os
from pathlib import Path


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://localhost:8001")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///civiceye.db")
    DATABASE_PATH = DATABASE_URL.replace("sqlite:///", "")
    if not os.path.isabs(DATABASE_PATH):
        DATABASE_PATH = str(Path(__file__).resolve().parents[1] / DATABASE_PATH)

