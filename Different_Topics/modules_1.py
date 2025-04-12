# module = a file containing code you want to include in your program
#          use 'import' to include module (built-in or your own)
#          useful to breakup a large program reusable separate files

#print(help("modules"))

#  Part 1
print("\n------------------------------Part 1 ----------------------------------------\n")

# Now I'm gonna use the math module

import math

print(math.pi)


#  Part 2
print("\n------------------------------Part 2 ----------------------------------------\n")

import math as m

print(m.pi)

#  Part 3
print("\n------------------------------Part 3 ----------------------------------------\n")

from math import pi

print(pi)