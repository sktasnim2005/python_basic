

#-------------------------------------------------------------------------------------
#part 1
print("\n-----Part 1 -------\n")

numbers = [1,-2,3,-4,5,-6,-7,8]
#Here I'm gonna make all the numbers in the list and  print them

positive_num = [ abs(x) for x in numbers]

print(positive_num)
print()


#-------------------------------------------------------------------------------------
#part 2
print("\n-----Part 2 -------\n")
#Here I'm gonna print only positive numbers 

#positive_num = [expression for value in  iterable  if  condition]
#positive_num = [     x     for   x   in   numbers  if    x>=0   ]

positive_num = [ x for x in numbers if x>=0]

print(positive_num)

#Here I'm gonna print only negative numbers 
negative_num = [ x for x in numbers if x<0]

print(negative_num)
print()


#-------------------------------------------------------------------------------------
#part 3
print("\n-----Part 3 -------\n")
#Here I'm gonna print even numbers 

even_num = [ x for x in numbers if x%2==0]

print(even_num)
print()


#-------------------------------------------------------------------------------------
#part 4
print("\n-----Part 4 -------\n")
#Here I'm gonna print odd numbers 

odd_num = [ x for x in numbers if x%2!=0]

print(odd_num)
print()




