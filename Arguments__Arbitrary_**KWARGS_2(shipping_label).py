#4 types of arguments 
# 1. positional arguments  2.Default arguments  3. keyword arguments  4.arbitary arguments


#Example 1
print("---------Example 1---------\n")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("Dr.", "Sponge", "VimBar", "III",
                street= "1234 Ghost St.",
                city= "Dhaka City",
                zip= "9100",
                country= "Bangladesh",)


#Example 2
print("\n---------Example 2---------\n")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    #for key, value in kwargs.items():
    #    print(f"{key}: {value}")
    
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('zip')}, {kwargs.get('country')}")



shipping_label("Dr.", "Sponge", "VimBar", "III",
                street= "1234 Ghost St.",
                city= "Dhaka City",
                zip= "9100",
                country= "Bangladesh",)

#Example 3
print("\n---------Example 3---------\n")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    #for key, value in kwargs.items():
    #    print(f"{key}: {value}")
    
    if 'apt' in kwargs:
        print(f"{kwargs.get('apt')}")
    else:
          print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('zip')}, {kwargs.get('country')}")



shipping_label("Dr.", "Sponge", "VimBar", "III",
                street= "1234 Ghost St.",
                #apt= "Apt 2B",
                city= "Dhaka City",
                zip= "9100",
                country= "Bangladesh",)