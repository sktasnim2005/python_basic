import random
import string

def generate_password(length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    #special = string.punctuation
    special = "!@#$%^&*()"


    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    if not characters:
        return "Choose at least one character type!"

    password = []
    if numbers:
        password.append(random.choice(digits))
    if special_characters:
        password.append(random.choice(special))
    password.append(random.choice(letters))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

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
