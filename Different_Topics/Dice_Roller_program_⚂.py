import random

# i'm using unicode here to get desired symbols

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")

# ● ┌ ─ ┐ │ └ ┘ 

#   "┌─────────┐"
#   "│         │"
#   "│         │"
#   "│         │"
#   "└─────────┘"

dice_Art = {
            1:( "┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2:( "┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3:( "┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4:( "┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5:( "┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6:( "┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
            }
dice = []
total = 0

num_of_dice = int(input("How many dice do you want to roll? "))

for i in range(num_of_dice):
    dice.append(random.randint(1,6))


# In this code i have showed the dise in both Vertical and Horizontal format

#PRINT Vertically

print("\n.....V e R t I c A l.....\n")
for i in range(num_of_dice):
    for j in dice_Art.get(dice[i]):
        print(j)


#PRINT Horizontally

print("\n.....H o R i Z o N t A l.....\n")
for i in range(5):
    for j in dice:
       print(dice_Art.get(j)[i], end=" ")
    print()

for i in dice:
    total += i
print(f"Total: {total}")
