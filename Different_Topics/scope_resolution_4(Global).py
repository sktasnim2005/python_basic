#Part 1
print("\n-------------- Part 1 -----------------------\n")
def func1():
    print(x)

def func2():
    print(x)

x = 10 # here  a global version of x = 10  

func1()
func2()


#Part 2
print("\n-------------- Part 2 -----------------------\n")
def func1():
    x = 1        # here x has a local version so it will print 1
    print(x) 

def func2():
    x = 2       # here x has a local version so it will print 2
    print(x)

x = 10 # here  a global version of x = 10  

func1()
func2()