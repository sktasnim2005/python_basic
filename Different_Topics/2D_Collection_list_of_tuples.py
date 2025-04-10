

groceries =[("apple", "orange", "banana","coconut"),
            ("celery","carrots","potatoes"),
            ("beef","chicken","fish")
            ]


# Print all groceries
print("\n""-----Groceries-----""\n")
for i in groceries :
    print(i)

#to print all elements
print("\n")
for i in groceries :
    for j in i:
        print(j, end=" ")
    print()     

