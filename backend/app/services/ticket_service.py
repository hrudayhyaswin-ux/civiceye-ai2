# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import random
import string


def generate_ticket_id():
    token = "".join(random.choices(string.digits, k=6))
    return f"CE-{token}"

