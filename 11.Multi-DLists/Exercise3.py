"""
(Row sorting) Implement the following function to sort the

rows in a two-
dimensional list. A new list is returned and the original

list is intact.
def sortRows(m):
Write a test program that prompts the user to enter a
matrix of numbers and
displays a new row-sorted matrix.
"""
def sortRows(m):
    newMatrix = [] # Creates an empty list to store the newly sorted rows
    for row in m: # Loops through each individual row in the original matrix
        sortedRow = sorted(row) # Sorts the current row sorted() creates a new list without modifying the original row
        newMatrix.append(sortedRow) # Adds the newly sorted row to the new matrix
    return newMatrix

def main():
    print("Enter a 3-by-3 matrix row by row:")

    matrix = [] # creates the empty matrix
    for row in range(3): # in the 3x3 rows
        rowsNum = list(map(float, input().split())) #creates a new row(list)
        matrix.append(rowsNum) #adding the row to the empty matrix
    print(matrix)
    rowsSorted = sortRows(matrix) #passes matrix into sortRows function
    print("The rows-sorted list is", rowsSorted) # displays the matrix with each row sorted
main()