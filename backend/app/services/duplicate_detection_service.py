def duplicate_hint(description):
    text = description.lower()
    if any(word in text for word in ("again", "same", "still", "repeated")):
        return 74
    return 18

