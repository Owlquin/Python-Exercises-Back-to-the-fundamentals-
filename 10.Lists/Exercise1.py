"""
(Reverse the numbers entered) Write a program that reads a
list of integers and
displays them in the reverse order in which they were read.

"""
#creates a list of integers
numbers = list(map(int, input("Enter numbers: ").split()))
#reverse method reverses the inputted list
numbers.reverse()
print(numbers)