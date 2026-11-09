"""
(Palindrome number) Write a program that prompts the user
to enter a three-digit
integer and determines whether it is a palindrome number.
A number is a palindrome
if it reads the same from right to left and from left to
right.
"""


num = int(input("Enter a three digit integer: "))

original_num = num
#extracts and removes the first digit (from the right)
digit = num % 10
num = num // 10
#building the number starting with extracted digit
reverse = digit

digit = num % 10

num = num // 10
#add the extracted digit to the reversed number
reverse = reverse * 10 + digit

digit = num % 10
num = num // 10
#adds the finals digit to complete the reversed number
reverse = reverse * 10 + digit
#checks if reversed number matches the original number
if reverse == original_num:
    print(original_num, " is a palindrome")
else:
    print(original_num, "is not a palindrome")
