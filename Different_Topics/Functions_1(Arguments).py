
#Part 1
print("---------Part 1-----------")
def happy_birthday():
    print ("Happy Birthday to you ....")
    print("You are old..")
    print("Happy Birthday!!")
    print()

happy_birthday()   
# this will call the function happy_birthday
happy_birthday()

#Part 2
print()
print("---------Part 2-----------")
print()
def happy_birthday(name, age):
    print ("Happy Birthday to you ....")
    print(f"You are {age} years old..")
    print(f"Happy Birthday {name}!!")
    print()

happy_birthday("Tasnim", 23)
happy_birthday("Alex", 24)