#4 types of arguments 
# 1. positional arguments  2.Default arguments  3. keyword arguments  4.arbitary arguments


# keyword arguments = arguments prefixed with the names of parameters
#                                        order of the arguments doesn’t matter
#                                        helps with readability

#Example 1
def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")

hello("Hello", "Mr.", "Sk", "Tasnim")  # Positional arguments
hello("Mr.", "Alex", "Dev", "Hello")  # Positional arguments (order changed)
hello(title="Mr.", first_name="Jonny", last_name="Sheikspear", greeting="Hello")  # Keyword arguments 


