"""
(Reverse number) Write a program that prompts the user to enter a four-digit inte-
ger and displays the number in reverse order.
"""


s = int(input("Enter a four-digit integer: "))

# Taking the 4-digit number and extracting the rightmost digit
digit = s % 10

# Removing the rightmost digit from number s
s = s // 10

# Setting the first extracted digit as the reverse number
reverse = digit

# Taking the 3-digit number and extracting the rightmost digit
digit = s % 10

# Removing the rightmost digit from number s
s = s // 10

# Building the reverse number
reverse = reverse * 10 + digit

# Taking the 2-digit number and extracting the rightmost digit
digit = s % 10

# Removing the rightmost digit from number s
s = s // 10

# Building the reverse number
reverse = reverse * 10 + digit

# Taking the 1-digit number and extracting the rightmost digit
digit = s % 10

# Building the reverse number
reverse = reverse * 10 + digit

print("The reverse number is", reverse)
