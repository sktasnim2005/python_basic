#it's  just another way of Generate_random_(rock,paper,scissors Game 1 )

import random

options = {"rock": "r", "paper": "p", "scissors": "s"}
reverse_options = {v: k for k, v in options.items()}  # Reverse mapping

while True:
    you = input("Enter your choice (rock = r, paper = p, scissors = s) or QQ to quit: ").lower()
    
    if you == "qq":
        print("Game Over! Thanks for playing!")
        break

    # Convert shorthand (r, p, s) to full form
    if you in reverse_options:
        you = reverse_options[you]

    if you not in options:
        print("Invalid input! Try again.")
        continue

    computer = random.choice(list(options.keys()))  # Computer selects full-form choice

    print("Your choice:", you)
    print("Computer's choice:", computer)

    if you == computer:
        print("It's a tie! 🤝")
    elif (you == "rock" and computer == "scissors") or \
         (you == "scissors" and computer == "paper") or \
         (you == "paper" and computer == "rock"):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

    print()
