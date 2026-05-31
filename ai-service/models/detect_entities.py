def detect_entities(description, location):
    words = description.split()
    landmark = location.get("address") or " ".join(words[:4])
    return {
        "landmark": landmark,
        "mentioned_people": [word for word in words if word.istitle()][:3],
        "ward": location.get("ward") or "unknown",
    }

