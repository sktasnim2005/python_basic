#return = statement used to end a function and send a result back to the caller

def add(x,y):
    z = x+y
    return z

def substract(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z =x/y
    return z

print("---------Part 1-----------")
print(add(2,3))
print(f"Sum2 = {add(5,6)}")
result = add(1,2)
print(f"Sum3 = {result}")
print()

print("---------Part 2-----------")
print(f"Substract = {substract(5,2)}")
print(f"Multiply = {multiply(5,2)}")        
print(f"Divide = {divide(100,3)}")
print(f"Divide2 = {divide(100,3):.2f}")