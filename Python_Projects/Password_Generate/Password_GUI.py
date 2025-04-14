import tkinter as tk
from tkinter import messagebox
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

def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for length.")
        return

    use_numbers = numbers_var.get()
    use_special = special_var.get()

    password = generate_password(length, use_numbers, use_special)
    result_var.set(password)

# GUI
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "10")  # Default length
length_entry.grid(row=0, column=1, padx=10)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)

tk.Button(root, text="Generate Password", command=on_generate).grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
