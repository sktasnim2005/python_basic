#4 types of arguments 
# 1. positional arguments  2.Default arguments  3. keyword arguments  4.arbitary arguments


# *args    = allows you to pass multiple non-keyword arguments  # args means arguments
# **kwargs = allows you to pass multiple keyword arguments      # kwargs means keyword arguments
#           * unpacking operator

def show_address(**kwargs):
    print(type(kwargs)) # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_address(streer="123 street" ,
             appartment="Apt 200" ,
             city= "Khulna",
             zip="9100" ,
             country="Bangladesh" )