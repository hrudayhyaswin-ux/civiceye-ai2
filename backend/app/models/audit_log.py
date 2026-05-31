from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuditLog:
    actor: str
    action: str
    at: datetime

