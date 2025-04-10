
#part 1
print("\n-----Part 1 -------\n")

fruits = ["apple", "orange", "banana", "mango"]

#I'm gonna take each string and make it uppercase 

upper_fruit = [x.upper() for x in fruits]

print(upper_fruit)

#-------------------------------------------------------------------------------------
#part 2
print("\n-----Part 2 -------\n")

class_room = ["teacher", "student", "book", "exam"]

#I'm gonna take each string and make it uppercase 

#we can also do it by just reassigning the name 
class_room = [x.upper() for x in class_room]

print(class_room)

#-------------------------------------------------------------------------------------
#part 3
print("\n-----Part 3 -------\n")

school = ["teacher", "student", "book", "exam"]

#I'm gonna take each 1st character of each string  

your_school = [x[0] for x in school]

print(your_school)



