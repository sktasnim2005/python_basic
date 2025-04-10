#4 types of arguments 
# 1. positional arguments  2.Default arguments  3. keyword arguments  4.arbitary arguments


# we are going to create a function to generate a phone number
# we need to pass the country code, area code and first 3 digits and last 4 digits
# we will use keyword arguments to make it more readable

def phone_number(country_code, area_code, first_3_digits, last_4_digits):
    print(f"{country_code} ({area_code}) {first_3_digits}-{last_4_digits}")
    # this is the correct way to call the function

#1st way to call the function
phone_number("+1", "123", "456", "7890")

# 2nd way to call the function
phone_number(area_code="123", first_3_digits="456", last_4_digits="7890", country_code="+1")

# 3rd way to call the function
phone_number("+1", "123", last_4_digits="7890", first_3_digits="456")