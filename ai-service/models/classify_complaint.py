DEPARTMENTS = {
    "Road Damage": "Roads",
    "Garbage": "Sanitation",
    "Street Light": "Utilities",
    "Water Leak": "Water",
    "Drainage": "Water",
    "Public Safety": "Public Safety",
    "Other": "General",
}


def classify(category_hint, description):
    text = description.lower()
    if any(word in text for word in ("garbage", "trash", "waste")):
        return "Garbage", "Sanitation"
    if any(word in text for word in ("pothole", "road", "manhole")):
        return "Road Damage", "Roads"
    if any(word in text for word in ("light", "lamp", "dark")):
        return "Street Light", "Utilities"
    if any(word in text for word in ("water", "leak", "pipe", "drain")):
        return "Drainage", "Water"
    category = category_hint if category_hint in DEPARTMENTS else "Other"
    return category, DEPARTMENTS[category]

