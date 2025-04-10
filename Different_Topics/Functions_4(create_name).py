
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()    
    #return first + " " + last
    return f"{first} {last}" # both way is correct
print(create_name("john","doe"))

full_name = create_name("sk","tasnim")
print(full_name)