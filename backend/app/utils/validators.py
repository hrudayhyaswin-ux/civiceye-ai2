def validate_complaint(payload):
    if not payload.get("title"):
        return "Missing required field: title"
    if not payload.get("description") and not payload.get("voice_note"):
        return "Missing required field: description (or voice note)"
    return None

