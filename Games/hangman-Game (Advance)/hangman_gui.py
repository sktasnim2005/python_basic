# hangman_gui.py

import tkinter as tk
from tkinter import PhotoImage
import random
import os     # os handles paths (important for locating images).
from wordCollection import words_by_category

# defining a class to handle the whole game.
class HangmanApp:
    def __init__(self, master): # This is the constructor – it sets everything up when the app starts. here master is the main window and self is the instance of the class.
        self.master = master    # master is the main window. I set the title to "Hangman Game".
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
        self.image_label = tk.Label(master)  # This label will hold the hangman image.
        self.image_label.pack(pady=10)       # Adding some space around the image.

        # Category and word setup
        self.category = ""                  # This will hold the current category.
        self.word = ""                      # This will hold the current word.
        self.guessed = set()                # This will hold the letters guessed by the user.
        self.wrong_guesses = 0              # This will count the number of wrong guesses.

        # Category label
        self.label = tk.Label(master, text="", font=("Arial", 16)) # This label will show the current category.
        self.label.pack(pady=10)                                   # Adding some space around the label. pady=10 gives vertical space (padding).

        # Hint label
        self.hint_var = tk.StringVar()      # This variable will hold the hint (the word with guessed letters).
        self.hint_label = tk.Label(master, textvariable=self.hint_var, font=("Arial", 20)) # This label will show the hint.
        self.hint_label.pack(pady=10)       # Adding some space around the label.

        # Entry box
        self.entry = tk.Entry(master, font=("Arial", 16))   # This is where the user will type their guesses.
        self.entry.pack()                                   # Adding some space around the entry box.
        self.entry.bind("<Return>", self.guess_letter)      # This binds the Enter key to the guess_letter function.

        # Message label
        self.message = tk.Label(master, text="", font=("Arial", 12))  # This label will show messages to the user (like win/loss messages).
        self.message.pack(pady=5)                                     # Adding some space around the label.

        # Reset button
        self.reset_button = tk.Button(master, text="New Game", command=self.new_game) # This button will start a new game.
        self.reset_button.pack(pady=10)                                               # Adding some space around the button.

        # Start first game
        self.new_game()               # This function starts the first game when the app opens.


    def update_hint(self):            # This function updates the hint label with the current guessed letters.
        hint = [letter if letter in self.guessed else "_" for letter in self.word]  # This creates a list where each letter is replaced by "_" if it hasn't been guessed yet.
        self.hint_var.set(" ".join(hint))                                           # This joins the list into a string with spaces in between each letter.


    def update_image(self):           # This function updates the hangman image based on the number of wrong guesses.
        self.image_label.config(image=self.hangman_images[self.wrong_guesses]) # This sets the image of the label to the current hangman image based on the number of wrong guesses.

    def guess_letter(self, event=None):     # This function handles the user's guess when they press Enter.
        guess = self.entry.get().lower()    # This gets the letter from the entry box and converts it to lowercase.
        self.entry.delete(0, tk.END)        # This clears the entry box after the user presses Enter.

        if not guess.isalpha() or len(guess) != 1:      # This checks if the input is a single letter.
            self.message.config(text="⚠️ Enter a valid single letter.") # If not, it shows a warning message.
            return                                                      # Exit the function if the input is invalid.
        
        if guess in self.guessed:                       # This checks if the letter has already been guessed.
            self.message.config(text=f"⚠️ You already guessed '{guess}'.") 
            return

        self.guessed.add(guess)            # This adds the guessed letter to the set of guessed letters.

        if guess in self.word:                      # This checks if the guessed letter is in the word.
            self.update_hint()                      # This updates the hint with the new guessed letter.
            if "_" not in self.hint_var.get():      # This checks if there are any "_" left in the hint.
                self.message.config(text="🎉 You win!") 
                self.entry.config(state="disabled") # Disable the entry box if the user wins.
        else:
            self.wrong_guesses += 1
            self.update_image()
            self.message.config(text=f"❌ Wrong: {self.wrong_guesses}/{self.max_wrong}") # This shows the number of wrong guesses.
            if self.wrong_guesses >= self.max_wrong:                      # This checks if the user has reached the maximum number of wrong guesses.
                self.hint_var.set(" ".join(self.word))                    # This reveals the word.
                self.message.config(text=f"💀 You lost! Word was '{self.word}'.")   
                self.entry.config(state="disabled") 

    def new_game(self):            # This function starts a new game.
        self.category = random.choice(list(words_by_category.keys())) # This randomly selects a category from the words_by_category dictionary.
        self.word = random.choice(words_by_category[self.category])   # This randomly selects a word from the selected category.
        self.guessed.clear()                                          # This clears the set of guessed letters.
        self.wrong_guesses = 0                                        # This resets the number of wrong guesses.
        self.label.config(text=f"📂 Category: {self.category}")                        
        self.hint_var.set("")                                         # This clears the hint label.
        self.message.config(text="")                                  # This clears the message label.
        self.entry.config(state="normal")       # This enables the entry box for the user to guess letters.
        self.update_hint()                      # This updates the hint with the new word.
        self.update_image()                     # This updates the hangman image to the initial state.

if __name__ == "__main__":        # This is the main function that runs the app.
        root = tk.Tk()            # This creates the main window.Here tk means tkinter .
        app = HangmanApp(root)    # This creates an instance of the HangmanApp class, passing the main window as an argument.
        root.mainloop()           # This starts the main loop of the app, which keeps it running until the user closes it.
