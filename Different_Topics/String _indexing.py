credit_number="1234-5678-9012-3456"

print(credit_number[0])

#print the first 4 digits
print(f"First 4 digits: {credit_number[0:4]}")

#print the first 4 digits another way
print(f"First 4 digits 2nd way: {credit_number[:4]}")

#print any digit in the middle
print(f"Middle digit: {credit_number[5:18]}")

#print the last 4 digits
print(f"Last 4 digits: {credit_number[-4:]}")

#print the last 4 digits another way
print(f"Last 4 digits 2nd way: {credit_number[-4:18]}")

#print any digit from the end
print(f"Digit from the end: {credit_number[-4]}")