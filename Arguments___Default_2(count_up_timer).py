import time

print("-------Part 1 -------")
def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("bro!")

count(1, 10)

print("\n-------Part 2 -------")

#def count(start=0, end):     # this is incorrect 
def count(end, start=0): # this is correct
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10)
#count(30,15) #it will start from 15 to 30