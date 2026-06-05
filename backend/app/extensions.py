# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS complaints (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  category TEXT NOT NULL,
  department TEXT NOT NULL,
  priority TEXT NOT NULL,
  status TEXT NOT NULL,
  summary TEXT NOT NULL,
  duplicate_confidence INTEGER NOT NULL,
  language TEXT NOT NULL,
  citizen_name TEXT,
  phone TEXT,
  location_json TEXT NOT NULL,
  attachments_json TEXT NOT NULL,
  timeline_json TEXT NOT NULL,
  voice_note_path TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
"""


def get_connection(database_path):
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_database(database_path):
    Path(database_path).parent.mkdir(parents=True, exist_ok=True)
    with get_connection(database_path) as connection:
        connection.executescript(SCHEMA)

