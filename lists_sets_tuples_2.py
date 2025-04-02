#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER



# Here we will learn ------ Set -----------


fruits = {"apple", "orange", "banana", "coconut"}

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


#Example 5 remove an element
print("\n""Example 5")
fruits.remove("banana")
print(fruits)


#Example 6 pop method but it will pop random elements
print("\n""Example 6")
fruits.pop()
print(fruits)


#Example 7 clear method
print("\n""Example 7")
fruits.clear()
print(fruits)

