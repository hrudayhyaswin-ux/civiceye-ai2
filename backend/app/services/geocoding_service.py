# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

def normalize_location(location):
    location = location or {}
    return {
        "address": location.get("address", "").strip(),
        "lat": location.get("lat", ""),
        "lng": location.get("lng", ""),
        "ward": infer_ward(location.get("address", "")),
    }


def infer_ward(address):
    if "ward" in address.lower():
        return address
    return "Ward pending"

