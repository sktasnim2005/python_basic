#4 types of arguments 
# 1. positional arguments  2.Default arguments  3. keyword arguments  4.arbitary arguments


# This code demonstrates the use of *args


def display_names(*names):
    for name in names:
        print(name,end=" ")
    print()

print("---------Example 5---------")
display_names("Sk.", "Tasnim", "Ur", "Rahman")