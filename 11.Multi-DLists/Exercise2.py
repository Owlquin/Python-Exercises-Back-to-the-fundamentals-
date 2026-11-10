"""
(Locate the largest element) Write the following function
that returns the location
of the largest element in a two-dimensional list:
def locateLargest(a):
The return value is a one-dimensional list that contains
two elements. These
two elements indicate the row and column indexes of the
largest element in the
two-dimensional list. Write a test program that prompts the

user to enter a two-
dimensional list and displays the location of the largest

element in the list.
"""
def locateLargest(a):
    largestNum = a[0][0] # first element is the largest number
    largestRow = 0 #initialize the row and column indexes of the largest number.
    largestColumn = 0 # first element is located at [0][0]
    for row in range(len(a)): #go through every row in the 2D list
        for column in range(len(a[row])): # go through every column in the current row

            if largestNum < a[row][column]:# Check if the current element is larger than the largest number found so far
                largestNum = a[row][column]
                largestRow = row
                largestColumn = column
    return [largestRow,largestColumn]

def main():
    rows = int(input("Enter the number of rows in the list:"))
    matrix = []
    for row in range(rows):
        numbers = input("Enter a row: ").split()
        # Convert each number from a string to a float
        # Append the completed row to the matrix
        matrix.append([float(num) for num in numbers])

    largeNum = locateLargest(matrix)

    print("The location of the largest element is at ",(largeNum[0], largeNum[1]))

main()