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

