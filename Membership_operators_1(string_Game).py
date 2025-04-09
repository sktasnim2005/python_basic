# Membership operators = used to test whether a value or variable is found in a sequence
#                                             (string, list, tuple, set, or dictionary)
#                                             1. in
#                                             2. not in

#Part 1 
print("------Part 1 = Letter Guess-----")
word = "APPLE"
letter = input("Guess the letter on the secret word : ")

if letter not in word :
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")

#both way are same 

#if letter in word :
#    print(f"There is a {letter}")
#else:
#    print(f"{letter} was not found")

#Part 2
print("\n------Part 2 = Email Validation Game -----\n")

#email = "sktasnim@gmail.com"

email = input("Enater email : ")

if "@" in email and "." in email:
    print("Valid email.")
else:
    print("Invaild email!")