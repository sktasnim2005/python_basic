item = input("What item would you like to purchase? : ")
price = float(input("What is the price? : "))
quantity = int(input("How many would you like to purchase? : "))

total = price * quantity

print(f"You have bough {quantity} x {item}/s")
print(f"Your total is {total}")
print(f"Your total is {round(total,3)}")