
my_dictionary = {"A":1 , "B":2 , "C":3}


#Part 1
print("----- Part 1 -----")
for key in my_dictionary:
    print(key)
print()

#Part 2
print("----- Part 2 -----")
for value in my_dictionary.values():
    print(value)
print()

#Part 3
print("----- Part 3 -----")
for key,value in my_dictionary.items():
    print(f"{key} = {value}")
print()