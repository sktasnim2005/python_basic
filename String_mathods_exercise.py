user_name = input("Enter a username: ")

# 1. Check if the user name is more than 12 characters
# 2. Check if the user name contains a space
# 3. Check if the user name is a digit


if len(user_name) > 12:
    print("Your user name can't be more than 12 characters")

elif not user_name.find(" ") == -1:
    print("Your user name can't contain a space")

elif not user_name.isalpha():
    print("Your user name can't be a digit")
 
else:
    print(f"Welcome {user_name}!")