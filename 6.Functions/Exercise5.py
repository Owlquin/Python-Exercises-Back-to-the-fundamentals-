"""
# (Display characters) Write a function that prints
characters using the following
#header:
# def printChars(ch1, ch2, numberPerLine):
# This function prints the characters between ch1 and ch2
with the specified
# numbers per line. Write a test program that prints ten
characters per line from 1
# to Z.goes from a ord() char to int -> chr() same int to same
char
"""

def printChars(ch1,ch2,numberPerLine):
    count = 0
# Loop through the ASCII values from ch1 to ch2, takes
#var number one step at a time from the sequence
    for number in range(ord(ch1),ord(ch2)+1):
        print(chr(number), end="") # Print character with a space separator
        count += 1 #counts the number (each char)
# Move to a new line when the line limit is reached
#so count % 10 == 0 make a new line
        if count % numberPerLine == 0:
            print()

print(printChars('1','Z',10))