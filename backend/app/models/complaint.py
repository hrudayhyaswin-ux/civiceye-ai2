# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

from dataclasses import dataclass


@dataclass
class Complaint:
    ticket_id: str
    title: str
    description: str
    category: str
    department: str
    priority: str
    status: str
    summary: str
    duplicate_confidence: int

