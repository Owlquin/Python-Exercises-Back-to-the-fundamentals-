"""
(Palindrome integer) Write the functions with the following
headers:
Return the reversal of an integer, e.g. reverse(456)
returns
654
def reverse(number):
Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A
number is a palin-
drome if its reversal is the same as itself. Write a test
program that prompts the
user to enter an integer and reports whether the integer is
a palindrome.takes a number and returns the number reversed, taking
negative numbers into account as well
"""
def reverse(number):
    negative_num = number < 0
    number = abs(number)
    reverse = 0
    while number != 0:
        digit = number % 10
        number = number // 10

        reverse = reverse * 10 + digit
    if negative_num:
        reverse = -reverse
    return reverse

#determines whether or not the number is a palindrome
def isPalindrome(number):
    original_num = number
    if reverse(number) == original_num:
        return True
    else:
        return False
#main function
def main():
    number = int(input("Enter a number:"))
    print("This is the number but reversed:", reverse(number))
    print("is your number a palindrome:", isPalindrome(number))

main()
