# Architecture

CivicEye AI uses a simple split-service architecture:

- React citizen app captures complaint content, voice, image metadata, and location.
- Flask backend validates payloads, creates public tracking IDs, and persists records.
- FastAPI AI service returns deterministic demo intelligence for category, department, priority, duplicate probability, and summary.
- React admin dashboard consumes backend admin APIs for triage and workflow visibility.

The implementation is intentionally lightweight for local demos and hackathon-style iteration. SQLite is the default persistence layer; the service boundary is ready for Postgres, object storage, and real AI providers later.

