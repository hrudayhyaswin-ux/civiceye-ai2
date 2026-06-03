# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

def duplicate_hint(description):
    text = (description or "").lower()
    if any(word in text for word in ("again", "same", "still", "repeated")):
        return 74
    return 18

