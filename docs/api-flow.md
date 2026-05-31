# API Flow

## Submit Complaint

`POST /api/complaints`

1. Citizen app sends title, description, address, coordinates, language, and optional attachments.
2. Backend validates required fields.
3. Backend calls `POST /analyze` on the AI service.
4. Complaint is stored with AI category, department, priority, summary, and duplicate confidence.
5. Response returns `ticket_id` for tracking.

## Track Complaint

`GET /api/complaints/<ticket_id>`

Returns public complaint status, department, priority, and timeline.

## Admin Dashboard

`GET /api/admin/complaints`

Supports `status`, `priority`, `department`, and `q` filters.

