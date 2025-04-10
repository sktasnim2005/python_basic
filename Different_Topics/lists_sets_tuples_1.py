#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# Here we will learn ------ List -----------


fruits = ["apple", "orange", "banana", "coconut"]

#Example 1
print("\n""Example 1")
print(fruits) #it will print all fruits

#Example 2
print("\n""Example 2")
print(fruits[0]) #it will print the first fruit

#Example 3
print("\n""Example 3")
print(fruits[0:2]) #it will print 0 to 1 index

#Example 4
print("\n""Example 4")
print(fruits[::2]) #it will print every 2nd element beginning 0 

#Example 5
print("\n""Example 5")
print(fruits[::-1]) # it willprint reverse 

#Example 6
print("\n""Example 6")
for x in fruits:
    print(x)

#Example 7 find the length of the list
print("\n""Example 7")
print(f"length= {len(fruits)}")   


#Example 8 using in operator
print("\n""Example 8")
print("banana" in fruits) #it will print True
print("pizza"in fruits) #it will print False


#Example 9 reassign an element
print("\n""Example 9")
fruits[0] = "grape"
print(fruits)


#Example 10 remove an element
print("\n""Example 10")
fruits.remove("banana")
print(fruits)


#Example 11 add an element end of the list
print("\n""Example 11")
fruits.append("mango")
print(fruits)


#Example 12 sort the list
print("\n""Example 12")
fruits.sort()
print(fruits)


#Example 13 insert method
print("\n""Example 13")
fruits.insert(1, "kiwi")
print(fruits)

#Example 14 reverse method
print("\n""Example 14")
fruits.reverse()
print(fruits)


#Example 15 index method
print("\n""Example 15")
print(fruits.index("mango"))
#print(fruits.index("watermelon"))


#Example 16 count method
print("\n""Example 16")
print(fruits.count("mango"))


#Example 17 clear method
print("\n""Example 17")
fruits.clear()
print(fruits)


#Example 16 pop method

#print(dir(fruits))
#print(help(fruits))