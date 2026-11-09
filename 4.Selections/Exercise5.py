"""
heads to tails guessing game
"""
import random

guess = int(input("Enter a guess for 0 = heads or 1 = tail: "))
#assigns the number 0 or 1 to heads/tails
coin = random.randint(0,1)
#if guess is correct or not
if coin == guess:
    print("Correct guess")
else:
    print("Incorrect guess")