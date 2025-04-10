# importing random module
import random

card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

while True:
    you = input("Please enter your card or QQ to quit: ").upper()

    if you == "QQ":
        print("Game Over! Thanks for playing!")
        break
    if you not in card:
        print("Invalid input!")
        continue

    option = random.choice(card)

    print("Your card is: ", you)
    print("Computer's card is: ", option)

    if you == option:
        print("🎉 You win!\n")
    else:
        print("😢 You lose!\n")

    