
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) :")
    if food.lower() =="q" :
        break
    else :
        price = float(input("Enter the price of {food} :"))
        prices.append(price)
        foods.append(food)

print("\n""------ Your Cart ------""\n")

for f in foods :
    print(f)

for p in prices :
    total += p

print()
print(f"Total price : {total: .2f}")