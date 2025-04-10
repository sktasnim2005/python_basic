

#part 1
print("\n-----Part 1 -------\n")

#num_doubles = [expression for value in  iterable   if      condition]
#num_doubles = [ x*2       for   x   in  range(1,5) if (condition is optional)  ] 
doubles = [x*2 for x in range(1,5)]

triples = [y*3 for y in range(1,5)]

squares = [z*z for z in range(2,6)]

print(f"Doubles = {doubles}")
print(f"Triples = {triples}")
print(f"Squares ={squares}")