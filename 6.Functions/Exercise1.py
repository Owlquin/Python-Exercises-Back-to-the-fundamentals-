"""
#Math: pentagonal numbers) A pentagonal number is defined
as forand so on. So, the first few numbers are 1, 5, 12,
22, .... Write a
function with the following header that returns a
pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display
the first 100 pentagonal
numbers with 10 numbers on each line.
"""
#calculates the pentagonal number
def getPentagonalNumber(n):
    result = n *(3*n-1)//2
    return result

#loop to calculate the first 1-- pentagonal numbers
for n in range(1,101):
    print(getPentagonalNumber(n), end = " ")
    if n % 10 == 0:
        print()