"""
(Display patterns) Write a function to display a pattern as
follows:
1
2 1
3 2 1
...
n n-1 ... 3 2 1
The function header is
def displayPattern(n):
Write a test program that prompts the user to enter a
number n and invokes
displayPattern(n) to display the pattern.
"""

def displayPattern(n):
    for row in range(1,n+1):
        for x in range(row,0,-1):
            print(x,end = "")
        print()


def main():
    n = int(input("Enter a number: "))
    displayPattern(n)

main()