# for loops = execute a block of code a fixed number of times.
#                     You can iterate over a range, string, sequence, etc.

# ---------------- EXAMPLE 1 ----------------

print("-+-+-+-+Example 1 -+-+-+-+")
for x in range(5):
    print(x)

# ---------------- EXAMPLE 2 ----------------

print("-+-+-+-+Example 2 -+-+-+-+")
for x in range(1, 11):
    print(x)

# ---------------- EXAMPLE 3 ----------------

print("-+-+-+-+Example 3 -+-+-+-+")
for x in reversed(range(1,5)):
    print(x)

# ---------------- EXAMPLE 4 ----------------

print("-+-+-+-+Example 4 -+-+-+-+")
for x in range(1, 11, 2):
    print(x)

# ---------------- EXAMPLE 5 ----------------
#its another way to do the same thing as example 3

print("-+-+-+-+Example 5 -+-+-+-+")
for x in range(10, 0, -1):
    print(x)

# ---------------- EXAMPLE 6 ----------------

print("-+-+-+-+Example 6 -+-+-+-+")
for x in range(1, 11):
    if x == 3:
        break
    print(x)

# ---------------- EXAMPLE 7 ----------------

print("-+-+-+-+Example 7 -+-+-+-+")
for x in range(1, 11):
    if x == 3:
        continue
    print(x)

# ---------------- EXAMPLE 8 ----------------

print("-+-+-+-+Example 8 -+-+-+-+")

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    if x == "-":
        continue
    print(x , end=" ")

print("\n")

# ---------------- EXAMPLE 9 ----------------

print("-+-+-+-+Example 9 -+-+-+-+")

card = "1234-5678-9012-3456"

for x in card:
    print(x , end=" ")
