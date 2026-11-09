"""
Print distinct numbers) Write a program that reads in
numbers separated by a
space in one line and displays distinct numbers (i.e., if a

number appears mul-
tiple times, it is displayed only once). (Hint: Read all

the numbers and store
them in list1. Create a new list list2. Add a number in
list1 to list2.
If the number is already in the list, ignore it.)
"""

#first list is for user to enter a number
#second list is to add non-duplicate numbers from the first list
list1 = list(map(int, input("Enter a ten numbers:").split()))
list2 = []
#for each element in the first list, if it is not in the second list
#append it to the second list, for non-duplicates
#if there is a duplicate then that number is skipped
for num in list1:
    if num not in list2:
        list2.append(num)
print("The distinct numbers are: ", list2)