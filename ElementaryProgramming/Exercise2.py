"""
(multiply the digits in an integer) Write a program that reads an integer between
0 and 1000 and multiplies all the digits in the integer. For example, if an integer
is 932, the multiplication of all its digits is 54.
Hint: Use the % operator to extract digits, and use the / operator to remove the
extracted digit. For instance, 932 % 10 = 2 and 932 / 10 = 93.
"""

number = int(input("Enter a number: "))
#ones 2
digit1 = number % 10
#tens 3
digit2 = number // 10 % 10
#hundreths 9
digit3 = number // 100

product = digit1 * digit2 * digit3

print("The multiplication of all digits in ",number,
"is" ,product)