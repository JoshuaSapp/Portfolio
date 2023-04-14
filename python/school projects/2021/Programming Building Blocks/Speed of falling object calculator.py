import math


print("please use sientific units")

m = float(input("What is the mass   "))
g = float(input("What is the gravity   "))
t = float(input("What is the time   "))
p = float(input("what is the dencity of the fluid/air   "))
a = float(input("what is the cross sectional area of the object   "))
C = float(input("What is the drag constant   "))

c = 1/2 * p * a * C

v = math.sqrt(m*g/c) * (1-math.exp((-math.sqrt(m*g*c)/m)*t))

print()
print(f"the inner value of c is: {round(c,2)}")
print(f"the velocity is {round(v,2)}")

#v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))