import math

def main():
    square()
    circle()
    rectangle()
    circle()
    print("done!")

def square():
    #input
    print('square')
    side_legnth = float(input("what is the side legnth?"))
    #output
    print(f"the area is: {side_legnth*side_legnth} cm or {(side_legnth*side_legnth)/1000} Meters")

def circle():
    #input
    print('circle')
    radius = float(input("what is the radious of the circle?  "))
    #output
    print(f"the area of the circle is {(radius**2)*math.pi} cm or {((radius**2)*math.pi)/1000}")


def rectangle():
    #input
    print("rectange")
    side_legnth1 = float(input("what is the side 1 legnth?"))
    side_legnth2 = float(input("what is the side 2 legnth?"))
    #output
    print(f"the area of the rectangle is {side_legnth1*side_legnth2}")



main()