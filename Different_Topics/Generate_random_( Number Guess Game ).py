import random

low = 1
high = 100
number = random.randint(low, high)

while True:
    guess = input(f"Please enter a number between {low} and {high} or QQ to quit: ")

    if guess.lower() == "qq":
        print("Game Over! Thanks for playing!")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess < low or guess > high:
        print(f"Please enter a number between {low} and {high}.")
        continue

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed the number!")
        break