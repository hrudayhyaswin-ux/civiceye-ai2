def validate_complaint(payload):
    missing = []
    if not payload.get("title"):
        missing.append("title")
    if not payload.get("description") and not payload.get("voice_note"):
        missing.append("description")
        
    if missing:
        return f"Missing required field: {', '.join(missing)}"
    return None
