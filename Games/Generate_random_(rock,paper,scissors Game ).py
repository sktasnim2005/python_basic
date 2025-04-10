# importing random module
import random

options = ("rock","r", "paper", "p", "scissors", "s")

while True:
    you = input("Enter your choice (rock = r, paper = p, scissors = s ) or QQ to quit: ").lower()
    if you == "qq":
        print("Game Over! Thanks for playing!")
        break
    if you not in options:
        print("Invalid input!")
        continue
    
    computer = random.choice(options)
    
    # Convert shorthand to full form better output
    if you == "r":
        you = "rock"
    elif you == "p":
        you = "paper"
    elif you == "s":
        you = "scissors"
    print("Your choice:", you)
    
    if computer == "r":
        computer = "rock"
    elif computer == "p":
        computer = "paper"
    elif computer == "s":
        computer = "scissors"
    print("Computer's choice:", computer)

    if you == computer:
        print("It's a tie! 🤝")
        continue
    elif (you == "rock" and computer == "scissors") or (you == "scissors" and computer == "paper") or (you == "paper" and computer == "rock"):
        print("🎉 You win!")
    elif (you == "r" and computer == "scissors") or (you == "s" and computer == "paper") or (you == "p" and computer == "rock"):
        print("🎉 You win!")    
    else:
        print("😢 You lose!")
        continue

    print()