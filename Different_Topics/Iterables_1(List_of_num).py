# Iterables = An object/collection that can return its elements one at a time,
#                    allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]

#Part 1
print("----- Part 1 -----")
for x in numbers:
    print(x)

print()

#Part 2
print("----- Part 2 -----")
for x in numbers:
    print(x,end=" ")
print()

#Part 3
print("----- Part 3 -----")
for x in reversed(numbers):
    print(x)

print()

#Part 4
print("----- Part 4 -----")
for x in reversed(numbers):
    print(x, end="-")

print()