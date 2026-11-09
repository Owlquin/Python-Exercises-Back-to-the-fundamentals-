"""
(Find the index of the smallest element) Write a function
that returns the index of
the smallest element in a list of integers. If the number
of such elements is greater
than 1, return the smallest index. Use the following
header:
def indexOfSmallestElement(lst):
Write a test program that prompts the user to enter a list
of numbers, invokes this
function to return the index of the smallest element, and
displays the index.
"""
def indexOfSmallestElement(lst):
# Initialize the smallest number to the first element in the list
    smallestnum = lst[0]
# Store the index of the smallest number (initially 0)
    smallestindex = 0
# Initialize a counter to keep track of the current index
    count = 0
# Loop through each number in the list
    for num in lst:
# Check if the current number is smaller than the smallest number found so far
        if num < smallestnum:
# Update the smallest number
            smallestnum = num
# Update the index of the smallest number
            smallestindex = count
# Move to the next index in the list
        count += 1
# Return the index of the smallest number
    return smallestindex

def main():
    lst = list(map(int,input("Enter a list of numbers:").split()))
    print(indexOfSmallestElement(lst))
    
main()
