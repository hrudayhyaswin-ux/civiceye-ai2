# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

def duplicate_confidence(description):
    text = description.lower()
    score = 12
    if any(term in text for term in ("same issue", "again", "still", "repeated", "already reported")):
        score += 58
    if len(text) < 40:
        score += 10
    return min(score, 95)

