"""
(Sort three integers) Write a program that prompts the user
to enter three integers
and displays them in increasing order
"""

# Enter a number
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
#first case is if num1 is the smallest or equal to show as
#num 1 first and if num2 is less than num3 then print 1,2,3
#else 1,3,2
if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
#second case if num 2 is the smallest or equal to show num
#2 first and if num 1 is less than num 3 then print 2,1,3
#else 2,3,1
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:

        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
#at this point the python already knows num3 is the
#smallest or tied for the smallest which is why it is the
#else statement
#and the nested if shows the next smallest if 1 < 2 and the
#nested else shows 2 < 1
else:
    if num1 <= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)