"""
(Algebra: solve linear equations) You can use Cramer’s rule
to solve the
following system of linear equation

Write a program that prompts the user to enter a, b, c, d,
e, and f and display the
result. If ad - bc is 0, report that The equation has no
solution.
"""
print("Enter a, b, c, d, e, f: ")
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = eval(input())
f = eval(input())

if (a * d - b * c) != 0:

    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", x, "and", "y is", y)
elif (a * d - b * c) == 0:
    print("The equation has no solution")