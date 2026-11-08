"""
#Write a program that prompts the user to enter the side of  a pentagon and displays 
the area 
"""

import math 
#entering the number of sides and length 
n = eval(input("Enter the number of sides: ")) 
s = eval(input("Enter the side: ")) 
# computing the area of a polygon 
area = ((n * pow(s,2)) / ( 4* math.tan(math.pi / n))) 
print("The area of the polygon is ", area)
