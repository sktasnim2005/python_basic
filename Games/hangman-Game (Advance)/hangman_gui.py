# hangman_gui.py

import tkinter as tk
from tkinter import PhotoImage
import random
import os
from wordCollection import words_by_category

class HangmanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.max_wrong = 6

        # Load hangman images
        script_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(script_dir, "assets")

        self.hangman_images = [
            PhotoImage(file=os.path.join(assets_dir, f"hangman{i}.png"))
            for i in range(7)
        ]

        # Hangman image display
        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        # Category and word setup
        self.category = ""
        self.word = ""
        self.guessed = set()
        self.wrong_guesses = 0

        # Category label
        self.label = tk.Label(master, text="", font=("Arial", 16))
        self.label.pack(pady=10)

        # Hint label
        self.hint_var = tk.StringVar()
        self.hint_label = tk.Label(master, textvariable=self.hint_var, font=("Arial", 20))
        self.hint_label.pack(pady=10)

        # Entry box
        self.entry = tk.Entry(master, font=("Arial", 16))
        self.entry.pack()
        self.entry.bind("<Return>", self.guess_letter)

        # Message label
        self.message = tk.Label(master, text="", font=("Arial", 12))
        self.message.pack(pady=5)

        # Reset button
        self.reset_button = tk.Button(master, text="New Game", command=self.new_game)
        self.reset_button.pack(pady=10)

        # Start first game
        self.new_game()

    def update_hint(self):
        hint = [letter if letter in self.guessed else "_" for letter in self.word]
        self.hint_var.set(" ".join(hint))

    def update_image(self):
        self.image_label.config(image=self.hangman_images[self.wrong_guesses])

    def guess_letter(self, event=None):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            self.message.config(text="⚠️ Enter a valid single letter.")
            return
        if guess in self.guessed:
            self.message.config(text=f"⚠️ You already guessed '{guess}'.")
            return

        self.guessed.add(guess)

        if guess in self.word:
            self.update_hint()
            if "_" not in self.hint_var.get():
                self.message.config(text="🎉 You win!")
                self.entry.config(state="disabled")
        else:
            self.wrong_guesses += 1
            self.update_image()
            self.message.config(text=f"❌ Wrong: {self.wrong_guesses}/{self.max_wrong}")
            if self.wrong_guesses >= self.max_wrong:
                self.hint_var.set(" ".join(self.word))
                self.message.config(text=f"💀 You lost! Word was '{self.word}'.")
                self.entry.config(state="disabled")

    def new_game(self):
        self.category = random.choice(list(words_by_category.keys()))
        self.word = random.choice(words_by_category[self.category])
        self.guessed.clear()
        self.wrong_guesses = 0
        self.label.config(text=f"📂 Category: {self.category}")
        self.hint_var.set("")
        self.message.config(text="")
        self.entry.config(state="normal")
        self.update_hint()
        self.update_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
