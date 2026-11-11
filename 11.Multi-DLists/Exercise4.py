"""
(Column sorting) Implement the following function to sort

the columns in a two-
dimensional list. A new list is returned and the original

list is intact.
def sortColumns(m):
Programming Exercises 391
Write a test program that prompts the user to enter a
matrix of numbers and
displays a new column-sorted matrix.
"""

def sortColumns(m):
    newMatrix = []  # Creates an empty list to store the new 3x3 matrix

    for row in range(3):  # Creates rows, each containing placeholders
        newMatrix.append([0, 0, 0])

    # Loops through each column in the original matrix
    for column in range(3):
        currentColumn = []  # An empty list to store the numbers from the current column

        # Loops through each row to collect the numbers in the current column
        for row in range(3):
            num = m[row][column]  # Retrieves the number at the current row and column
            currentColumn.append(num)  # Adds that number to the temporary column list

        # Sorts the numbers in the current column from smallest to largest
        sortedColumn = sorted(currentColumn)

        # Loops through each row to put the sorted numbers into the new matrix
        for row in range(3):
            newMatrix[row][column] = sortedColumn[row]

    return newMatrix


def main():
    print("Enter a 3-by-3 matrix row by row:")

    matrix = []

    for row in range(3):
        currentRow = list(map(float, input().split()))
        matrix.append(currentRow)

    print(matrix)

    columnSorted = sortColumns(matrix)

    print("The column-sorted list is ", columnSorted)


main()
