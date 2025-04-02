# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 12.96
price2 = -80038.5 
price3 = 100341.0001

# Example 1 it is round to that many decimal places
print(f"Example 1")
print(f"price 1 :{price1:.2f}")
print(f"price 2 :{price2:.2f}")
print(f"price 3 :{price3:.2f}""\n")

# Example 2 it is allocate that many spaces

print(f"Example 2")
print(f"price 1 :{price1: 6}")
print(f"price 2 :{price2: 6}")
print(f"price 3 :{price3: 6}""\n")

# Example 3 it is zero pad

print(f"Example 3")
print(f"price 1 :{price1: 09}")
print(f"price 2 :{price2: 09}")
print(f"price 3 :{price3: 09}""\n")

# Example 4 it is left align

print(f"Example 4")
print(f"price 1 :{price1: <10}")
print(f"price 2 :{price2: <10}")
print(f"price 3 :{price3: <10}""\n")

# Example 5 it is right align

print(f"Example 5")
print(f"price 1 :{price1: >10}")
print(f"price 2 :{price2: >10}")
print(f"price 3 :{price3: >10}"'\n')

# Example 6 it is center align

print(f"Example 6")
print(f"price 1 :{price1: ^10}")
print(f"price 2 :{price2: ^10}")
print(f"price 3 :{price3: ^10}""\n")

# Example 7 it is use a plus sign to indicate positive value

print(f"Example 7")
print(f"price 1 :{price1: }")
print(f"price 2 :{price2: }")
print(f"price 3 :{price3: }""\n")

# Example 8 it is place sign to leftmost position

print(f"Example 8")
print(f"price 1 :{price1: =}")
print(f"price 2 :{price2: =}")
print(f"price 3 :{price3: =}""\n")

# Example 9 it is insert a space before positive numbers

print(f"Example 9")
print(f"price 1 :{price1: }")
print(f"price 2 :{price2: }")
print(f"price 3 :{price3: }""\n")

# Example 10 it is comma separator

print(f"Example 10")
print(f"price 1 :{price1: ,}")
print(f"price 2 :{price2: ,}")
print(f"price 3 :{price3: ,}""\n")

# Example 11 it is percentage format

print(f"Example 11")
print(f"price 1 :{price1: %}")
print(f"price 2 :{price2: %}")
print(f"price 3 :{price3: %}""\n")

# Example 12 it is percentage format    

print(f"Example 12")
print(f"price 1 :{price1: .2%}")
print(f"price 2 :{price2: .2%}")
print(f"price 3 :{price3: .2%}"'\n')


# Example 13 its a combination of flags

print(f"Example 13")    
print(f"price 1 :{price1:+,.2f}")
print(f"price 2 :{price2:+,.2f}")
print(f"price 3 :{price3:+,.2f}")