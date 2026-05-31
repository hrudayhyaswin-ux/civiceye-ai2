def duplicate_confidence(description):
    text = description.lower()
    score = 12
    if any(term in text for term in ("same issue", "again", "still", "repeated", "already reported")):
        score += 58
    if len(text) < 40:
        score += 10
    return min(score, 95)

