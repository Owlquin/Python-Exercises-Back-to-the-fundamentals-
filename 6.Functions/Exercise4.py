"""
Display an integer reversed) Write the following function
to display an integer in
reverse order:
def reverse(number):
For example, reverse(3456) displays 6543. Write a test
program that prompts
the user to enter an integer and displays its reversal.
takes a number and reverses it
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
#main function that asks for a number and calls
#reverse(number) to output number reversed
def main():
    number = int(input("please enter a number:"))
    print("Your number reversed is: ", reverse(number))

main()