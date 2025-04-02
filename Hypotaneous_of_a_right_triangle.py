import math

a = float(input("Enter side A : "))

b = float(input("Enter side B : "))

c = math.sqrt(a**2 + b**2)

# c = math.sqrt(pow(a,2) + pow(b,2)) 


#print(f"The hypotaneous of the right triangle is {round(c,2)}")

print(f"Side C = {round(c,2)}")
