name = input("Enter your full name: ")

#find the length of the name
length = len(name)
print("Length of your name is: ", length)

# find method
result = name.find(" ")
print("The position of the space is: ", result)

# rfind() method
result = name.rfind("a")
print("The position of the last a is: ", result)

# capitalize() method
result = name.capitalize()
print("The capitalized name is: ", result)

# upper() method
result = name.upper()
print("The uppercase name is: ", result)

# lower() method
result = name.lower()
print("The lowercase name is: ", result)

# isdigit() method  
# returns True if all the characters are digits
#  it works like boolean
result = name.isdigit()
print("Is the name a digit? ", result) # aswer will be False if all the characters are not digits

# isalpha() method
# returns True if all the characters are alphabets
#answer will be False if all the characters are not alphabets 
#it also considers the space as a character
result = name.isalpha()
print("Is the name an alphabet? ", result)

#count() method
result = name.count("a")
print("The number of a in the name is: ", result)

#replace() method
result = name.replace("a", "z")
print("The name after replacing a with z is: ", result)

