unit = input("Enter the unit of temperature (C/F): ")

temp = float(input("Enter the temperature: "))

if unit == 'C':
    fahrenheit = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit} F")
elif unit == 'F':       
    celsius = (temp - 32) * 5/9
    print(f"The temperature in Celsius is {celsius} C")
else:       
    print(f"{unit} is not a valid unit of temperature")