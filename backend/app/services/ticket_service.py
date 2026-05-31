import random
import string


def generate_ticket_id():
    token = "".join(random.choices(string.digits, k=6))
    return f"CE-{token}"

