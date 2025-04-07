#4 types of arguments 
# 1. positional arguments  2.Default arguments  3. keyword arguments  4.arbitary arguments


#default arguments = A default value for certain parameters
# default is used when that argument is ommited
# it makes function more flexible , reduces the number of arguments



def net_price(list_price, discount, tax):
    return list_price * (1-discount) * (1+tax)


print(f"net_1 = {net_price(500,0,0.05)}")



# default arguments here are discount and tax 
# # discount = 0, tax = 0.6
def net_price2(list_price, discount=0, tax=0.6):
    return list_price * (1-discount) * (1+tax)


print(f"net_2 = {net_price2(700)}")

print(f"net_3 = {net_price2(700,0.1)}") # it will change the price of discount to 0.1

print(f"net_4 = {net_price2(700,0.1,0.99)}") # it will change the tax to 0.08 and discount to 0.1

print(f"net_5 = {net_price2(700,tax=0.08)}") # it will change the tax to 0.08