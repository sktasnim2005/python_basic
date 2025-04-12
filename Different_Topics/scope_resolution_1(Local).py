#variable scope   = where a variable is visible and accessible

#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

print("\n-------------- Part 1 -----------------------\n")
def func1():
    a = 1           # variable a is local to function 1
    print(a)

def func2():
    b = 2       # variable b is local to function 2
    print(b)

func1()
func2()


print("\n-------------- Part 2 -----------------------\n")
def func3():
    x = 11           # variable a is local to function 1
    print(x)

def func4():
    x = 22       # variable b is local to function 2
    print(x)

func3()
func4()