"""
(Sum the major diagonal in a matrix) Write a function that
sums all the numbers
of the major diagonal in an matrix of integers using the
following header:
def sumMajorDiagonal(m):
The major diagonal is the diagonal that runs from the top
left corner to the bottom
right corner in the square matrix. Write a test program
that reads a 4x4 matrix and
displays the sum of all its elements on the major diagonal.
"""
def sumMajorDiagonal(m):
    total = 0 # Initialize a variable to store the diagonal sum
    for i in range(len(m)): # Loop through each row in the matrix
        total += m[i][i] # Add the major diagonal element to total
    return total # # Return the final sum


def main():
    m = [] # Create an empty list to store the matrix
    rows = 4 # Set the number of rows to 4
    columns = 4 # Set the number of columns to 4
    for row in range(rows): # Loop through each row
        m.append([]) # Create an empty list for the current row
        for column in range(columns): # Loop through each column
            num = float(input("Enter an element for the row:"))
            m[row].append(num) # Add the entered number to the current row
    diagonalSum = sumMajorDiagonal(m) # Call the function and store its returned sum
    print("The total of the major diagonal added is",diagonalSum) # display the result

main()