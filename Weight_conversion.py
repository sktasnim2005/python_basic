weight = float(input("Enter your weight: "))

unit = input("Kilos or Pounds (K or L): ")

if unit.upper() == "K":
    weight = weight * 2.20462
    print(f"Your weight is {weight} pounds")
elif unit.upper() == "L":
    weight = weight / 2.20462
    print(f"Your weight is {weight} kilos")
else:
    print("Invalid unit")