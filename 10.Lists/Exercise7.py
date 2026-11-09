"""
(Eliminate duplicates) Write a function that returns a new
list by eliminating the
duplicate values in the list. Use the following function
header:
def eliminateDuplicates(lst):
Write a test program that reads in a list of integers,

invokes the function, and dis-
plays the result.
"""

def eliminateDuplicates(lst):
    newlst = []
    for num in lst:
        if num not in newlst:
            newlst.append(num)
    return newlst