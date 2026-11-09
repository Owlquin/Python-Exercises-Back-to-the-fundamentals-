"""
(Random number chooser) You can shuffle a list using
random.shuffle(lst).
Write your own function without using random.shuffle(lst)
to shuffle a list
and return the list. Use the following function header:
def shuffle(lst):
Write a test program that prompts the user to enter a list
of numbers, invokes the
function to shuffle the numbers, and displays the numbers.
"""

import random

def shuffle(lst):
# Repeat the shuffling process once for each element
    for num in range(0,len(lst)):
    # Generate two random indexes
        i = random.randint(0,len(lst) - 1)
        j = random.randint(0, len(lst) - 1)
        # Swap the elements at the two random indexes
        lst[i], lst[j] = lst[j], lst[i]
    return lst

def main():
    lst = list(map(int,input("Enter numbers: ").split()))
    print(shuffle(lst))
main()