temperature = 25

#implementing the logical and

#if temperature > 15 & temperature < 30:
#if temperature > 15 and temperature < 30:
if 15 < temperature < 30:#This is the best way to write the code
    print("The temperature is perfect today!")
else:   
    print("The temperature is not perfect today!")

#implementing the logical or

if temperature < 0 or temperature > 35:
    print("The temperature is bad!")
else:
    print("The temperature is good!")

#implementing the logical not
sunny = True
if not sunny:
    print("The weather is bad!")
else:
    print("The weather is good!")