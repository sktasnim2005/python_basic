#4 types of arguments 
# 1. positional arguments  2.Default arguments  3. keyword arguments  4.arbitary arguments


# *args    = allows you to pass multiple non-keyword arguments  # args means arguments
# **kwargs = allows you to pass multiple keyword arguments      # kwargs means keyword arguments
#           * unpacking operator

# # *args and **kwargs are used to pass a variable number of arguments to a function


#here we will learn about *args

#example 1
print("---------Example 1---------")
def add(a,b):
    return a + b

print(f"add(2,3) = {add(2,3)}") 

#example 2
print("---------Example 2---------")
def add(*args):
    print(type(args)) # args is a tuple
    return sum(args)
print(f"add(2,3,1) = {add(2,3,1)}") 

#example 3
print("---------Example 3---------")
def MyAdd(*args):
    total = 0
    for i in args:
        total += i
    return total
print(f"Example 3 = {MyAdd(2,3,4)}")

# we can use name as we like insted of args
print("---------Example 4---------")
def MyAdd(*numbers):
    return sum(numbers)
print(f"Example 4 = {MyAdd(1,2,3,4,5)}")