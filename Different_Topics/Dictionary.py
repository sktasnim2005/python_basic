# dictionary =  a collection of {key:value} pairs
#                        ordered and changeable. No duplicates

capitals = {"Bangladesh":"Dhaka",
            "China":"Beijing",
            "Russia":"Moscow",
            "Japan":"Tokyo", 
            }

#print(dir(capitals))
#print(help(capitals))


# get() method 
print("\n----- get method -----\n")
print(capitals.get("Russia"))

# get
#f capitals.get("China"):
 #  print("That capital exists")
 #else:
  #  print("That capital does not exist")

# update() method you can add new or update existing
print("\n----- update Methods -----\n")
capitals.update({"France":"Paris"})
capitals.update({"China":"Shanghai"})
print(capitals)


# pop() method
print("\n""-----Pop mathod-----""\n")
capitals.pop("Russia")
print(capitals)

# popitem() method 
#it wil pop the latest item , here the latest item was France 
print("\n""----- popitem method-----""\n")
print(capitals.popitem())
print(capitals)


#keys method
print("\n""----- keys method-----""\n")
print(capitals.keys())

#keys method for loop
print("\n""----- keys method foor loop-----""\n")
for key in capitals.keys():
    print(key)


# values method 
print("\n""----- values method-----""\n")
print(capitals.values())


# values method for loop
print("\n""----- values method foor loop-----""\n")
for value in capitals.values():
    print(value)


# items method 
#it resembles  a 2D list of touples
print("\n""----- items method (2D list of touples) -----""\n")
print(capitals.items())

# for loop to print every key, val
print("\n""----- items method for loop-----""\n")
for key, value in capitals.items():
    print(f"{key} : {value}")


# copy() method

# clear() method
#it will clear the list 
print("\n""----- clear method-----""\n")
capitals.clear()
print(capitals)
