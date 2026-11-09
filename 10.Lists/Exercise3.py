"""
(Analyze scores) Write a program that reads an unspecified
number of scores and
determines how many scores are above or equal to the
average and how many
scores are below the average. Assume the input numbers are
separated by one
space in one line.
"""

import statistics

#creates a list of integers
score = list(map(float, input("Enter score(s): ").split()))
#creating a variable for average
average = statistics.mean(score)
#counters for above and below
above = 0
below = 0

#looks at each number in the list and takes it and decides whether
# a num is above or below the average
for num in score:
    if num >= average:

        above+=1
    else:
        below+=1

print("average is: ", average)
print("Scores above or equal to average:", above)
print("Scores below average:", below)