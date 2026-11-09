"""
(Assign grades) Write a program that reads a list of scores
and then assigns grades
based on the following scheme:
The grade is A if score is best - 10.
The grade is B if score is best - 20.
The grade is C if score is best - 30.
The grade is D if score is best - 40.
The grade is F otherwise.
"""
def assign_grades(scores):
# Finds the highest number in the list. You store it in best because every student's grade is
# calculated relative to that number.
    best = max(scores)
# Gives you both the student's index (i) and their score (score) during each iteration of the loop.
    for i, score in enumerate(scores):
        if score >= best - 10:
            grade = 'A'
        elif score >= best - 20:
            grade = 'B'
        elif score >= best - 30:
            grade = 'C'
        elif score >= best - 40:
            grade = 'D'
        else:
            grade = 'F'
#The f before the string lets Python insert variable values wherever you put curly braces, such as {i}, {score},
# and {grade}.
        print(f"Student {i} score is {score} and grade is {grade}")

# Main program to input scores
def main():
    #converts scores into numbers
    scores = list(map(int, input("Enter scores:").split()))
    assign_grades(scores)

main()