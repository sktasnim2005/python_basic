num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")
           )

for row in num_pad :
    print(row)

print("\n""-----Num Pad-----""\n")
for r in num_pad:
    for col in r :
        print(col, end = " ")    
    print()    