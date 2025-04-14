import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password, get_strength

def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a positive number.")
        return

    password = generate_password(length, numbers_var.get(), special_var.get())
    result_var.set(password)

    # Show strength
    strength, color = get_strength(password)
    strength_label.config(text=f"Strength: {strength}", fg=color)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard! 🥳")

# GUI Setup
root = tk.Tk()
root.title("✨ Cute Password Generator ✨")

tk.Label(root, text="Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, padx=10)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)

tk.Button(root, text="Generate Password", command=on_generate).grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30, font=("Arial", 12)).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="📋 Copy", command=copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=5)

strength_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
strength_label.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
