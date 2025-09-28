import math as m


def func(x):
    return (m.e**(-x)*m.log(x))

def getc(x1, x2):
    c = x1 + (x2-x1)/2
    return c

def intervals(c, x1, x2, root):
    if func(c) == 0 or abs(func(c)) < 0.05:
        root = True
        print("Root is", c)
    elif func(c)*func(x1) < 0:
        x2 = c
    elif func(c)*func(x2) < 0:
        x1 = c

    return root, x1, x2

#############################

root = False
x1 = float(input("Enter lower bound of interval: "))
x2 = float(input("Enter upper bound of interval: "))

while not(root):
    c = getc(x1, x2)
    root, x1, x2 = intervals(c, x1, x2, root)




