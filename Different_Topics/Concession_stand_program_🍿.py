# Concession stand program

menu = {"pizza":3.00,
        "nachos":2.50,
        "popcorn":1.50,
        "soda":1.00,
        "candy":0.20,
        "fries":2.69,
        "chips":2.70,
        "burger":4.00,
        "lemonade":1.80,
        }

cart = []
total = 0

print("------ MENU ------")
for key,value in menu.items():
    print (f"{key:10} : ${value:.2f}")
print("-------------------")


while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None :
        cart.append(food)

for food in cart :
    total += menu[food]
    #total += menu.get(food)
    print(food , end=" ")

print(f"Total : {total:.2f}")
