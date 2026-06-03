# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

def prioritize(title, description, category):
    text = f"{title} {description}".lower()
    high_terms = ("danger", "accident", "fire", "injury", "open", "school", "hospital", "urgent")
    low_terms = ("minor", "small", "request")
    if any(term in text for term in high_terms) or category == "Public Safety":
        return "High"
    if any(term in text for term in low_terms):
        return "Low"
    return "Medium"

