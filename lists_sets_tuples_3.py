#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# Here we will learn ------ Tuple -----------


fruits = ("apple", "orange", "banana", "coconut","orange")

#Example 1
print("\n""Example 1")
print(fruits) #it will print all fruits

#Example 2
print("\n""Example 2")
for x in fruits:
    print(x)

#Example 3 find the length of the list
print("\n""Example 3")
print(f"length= {len(fruits)}")   


#Example 4 using in operator
print("\n""Example 4")
print("banana" in fruits) #it will print True
print("pizza"in fruits) #it will print False


#Example 5 
print("\n""Example 5")
print(fruits.count("mango"))
print(fruits.count("orange"))


#Example 6 clear method
print("\n""Example 6")
print(fruits.index("banana"))
#print(fruits.index("watermelon"))
