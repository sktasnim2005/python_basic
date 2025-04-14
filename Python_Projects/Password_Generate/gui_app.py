# gui_app.py
import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password  # Importing the function

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

# GUI setup
root = tk.Tk()
root.title("Password Generator")


# Widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "10")
length_entry.grid(row=0, column=1, padx=10)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)

tk.Button(root, text="Generate Password", command=on_generate).grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
