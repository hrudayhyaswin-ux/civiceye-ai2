# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuditLog:
    actor: str
    action: str
    at: datetime

