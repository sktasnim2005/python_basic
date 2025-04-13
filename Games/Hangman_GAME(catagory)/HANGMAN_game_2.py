import random
import os
from Word_list import words_by_category
#dictionary of key : ()
hangman_art = { 0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")
                }

# Scoreboard
score = {
    "games_played": 0,
    "wins": 0,
    "losses": 0
}

def display_man(wrong_guesses):
    print("\n   +-------+")
    print("   |  | ")
    for line in hangman_art[wrong_guesses]:
        print("   | " + line)
    print("   ======\n")

def display_hint(hint):
    print("Word: " + " ".join(hint))

def display_answer(answer):
    print("Answer: " + " ".join(answer))

def clear_screen():
    os.system("clear")  

def play_game():
    category, word_list = random.choice(list(words_by_category.items()))
    answer = random.choice(word_list)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    print(f"\n🎯 Category: {category}")

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Invalid input. Enter a single alphabet.")
            continue
        if guess in guessed_letters:
            print("⚠️ Already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("🎉 You Win!")
            score["games_played"] += 1
            score["wins"] += 1
            break

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("💀 You Lose!")
            score["games_played"] += 1
            score["losses"] += 1
            break

def view_score():
    print("\n===== 📊 SCOREBOARD =====")
    print(f"Games Played: {score['games_played']}")
    print(f"Wins        : {score['wins']}")
    print(f"Losses      : {score['losses']}")
    print("==========================\n")

def main_menu():
    while True:
        print("🎮 Welcome to Hangman Game!")
        print("1. Play Game")
        print("2. View Score")
        print("3. Quit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            clear_screen()
            play_game()
        elif choice == "2":
            view_score()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
