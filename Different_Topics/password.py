import random
import string


def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #print(letters, digits, special)
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = []
    if numbers:
        password.append(random.choice(digits))
    if special_characters:
        password.append(random.choice(special))
    password.append(random.choice(letters))

    while len(password) < min_length:
        password.append(random.choice(characters))

    random.shuffle(password) # shuffle the password. it means randomly arrange the password
    return ''.join(password) # join the password list to a string

# Example usage
print(f"1st Pass :{generate_password(10)}")

print(f"2nd Pass :{generate_password(10, numbers = False)}")

print(f"3rd Pass :{generate_password(10, special_characters = False)}")

print(f"4th Pass :{generate_password(10, numbers = False, special_characters = False)}")
