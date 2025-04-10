# List comprehension = A concise way to create lists in Python
#                                        Compact and easier to read than traditional loops
#                                        [expression for value in iterable if condition]

#part 1
print("\n-----Part 1 Normal Way-------\n")

doubles = []
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

#part 2
print("\n-----Part 2 comprehension -------\n")

#num_doubles = [expression for value in  iterable   if      condition]
#num_doubles = [ x*2       for   x   in  range(1,5) if (condition is optional)  ] 
num_doubles =  [ x*2       for   x   in  range(1,5) ]

print(num_doubles)