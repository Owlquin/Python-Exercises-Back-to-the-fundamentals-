"""
quadratic formula.
Write a program that prompts the user to enter values for a, b, and c and displays
the result based on the discriminant. If the discriminant is positive, display two

roots. If the discriminant is 0, display one root. Otherwise, display The equa-
tion has no real roots
"""
import math
#inpit a,b,c
print("Enter a,b,c: ")
a = eval(input())
b = eval(input())
c = eval(input())
#this is the discriminate
discriminate = pow(b, 2) - 4 * a * c
#have the roots in the if statement so r1 and r2 wont
#calculate before whether the discriminate is positive.
#Python's math.sqrt() cannot calculate the square root of a
#negative number. It raises a ValueError
if discriminate > 0:
    r1 = (-b + math.sqrt(discriminate)) / (2 * a)
    r2 = (-b - math.sqrt(discriminate)) / (2 * a)
    print("The roots are", r1, "and", r2)
# if the discriminate is 0
elif discriminate == 0:
    root = -b / (2 * a)
    print("The root is", root)
# if the discirminate is negative
else:
    print("The equation has no real roots")