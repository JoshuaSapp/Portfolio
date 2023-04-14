"""
Write Python code to satisfy the following conditions. Then test your code on the values of the variables given.

Given an int n, return the absolute diffrence between n and 10, except return triple the absolute dfference if n is over 10. 
It should return 1 when n=9. It should return 33 when n=21. What will the code return when n=7 or n=35?

We have a loud talking robot. The "hour" parameter is the current hour time in the range 0 to 23.
We are in trouble if the robot is talking and the hour is before 6 or after 21. Return True if we are in trouble. 
It should return True when the robot is talking and the hour is 8. It should return False when the robot is not talking and the hour is 8. 
What does it return if the robot is talking and the hour is 9?
"""

def p1(n):

    an = abs(n)
    ad = abs(10 - an)

    if n > 10:
        return(ad*3)
    return(ad)

print(p1(9))
print(p1(21))
print(p1(7))
print(p1(35))

def p2(hour,talking):
    if hour > 6 and hour < 21 and talking:
        return(True)
    else:
        return(False)

print(p2(5,False))
print(p2(8,False))
print(p2(8,True))



"""Write a function that takes, as input, two lists of integers, a and b, both of length 3, and returns, as output, a new list of length 2 containing the
last elements of a and b. For example, if a = [1, 2, 3] and b = [10, 20, 30], then the function should return the list [3, 30]."""

def p3(a,b):
    return[a[2],b[2]]


a = [1, 2, 3]
b = [10, 20, 30]
print(p3(a,b))

