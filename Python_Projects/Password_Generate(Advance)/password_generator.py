import string
import random

def generate_password(length, use_numbers=True, use_special=True):
    chars = string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_+="
    return ''.join(random.choice(chars) for _ in range(length))

def get_strength(password):
    length = len(password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_+=" for char in password)

    if length < 6:
        return "Too Short", "red"
    elif has_number and has_special and length >= 12:
        return "Strong 💪", "green"
    elif has_number or has_special:
        return "Medium 🤏", "orange"
    else:
        return "Weak 😓", "red"
