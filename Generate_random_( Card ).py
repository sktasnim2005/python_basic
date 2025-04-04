# importing random module
import random

card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
option = random.choice(card)
print("Computer's card is: ", option, "\n")


# Randomly shuffle the card
# it will change the order of the elements in the list
random.shuffle(card)
print(card)
