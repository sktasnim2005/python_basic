# password_generator.py
import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

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

    while len(password) < min_length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)
