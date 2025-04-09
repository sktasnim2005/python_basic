
#part 1
print("\n-----Part 1 -------\n")

#Here I'm gonna print the marks of those who passed in the exam

grades = [85,90,51,40,69,30]

passing_grade = [x for x in grades if x>=40]

print(passing_grade)