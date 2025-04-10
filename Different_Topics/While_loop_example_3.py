food = input("What is your favorite food? (q to quit) ")

while not food == "q":
#while food != "q": # This is also correct
    print("You like", food)
    food = input("What is your favorite food? (q to quit) ")

print("Goodbye!")
