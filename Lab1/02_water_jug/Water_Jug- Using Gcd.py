import math
x=int(input("Enter Capacity of Jug 1: "))
y=int(input("Enter Capacity of Jug 2: "))
target=int(input("Enter Target: "))
g=math.gcd(x, y)
if target>x+y:
    print("False")
else:
    if target % g == 0:
        print("True")
    else:
        print("False")