"""
Count positive and negative numbers and compute the
average of numbers)
Write a program that reads an unspecified number of
integers, determines
how many positive and negative values have been read, and
computes the total
and average of the input values (not counting zeros). Your
program ends with the
input 0. Display the average as a floating-point number.
"""
#entering 0 will stop the program
num = (int(input("Enter an integer, the input reads if it is 0: ")))
positive_count = 0
negative_count = 0
total = 0
num_counter = 0
#continues to loop as long as the user does not enter 0
while num != 0:
    if num > 0:
        positive_count +=1
    else:
        negative_count +=1
    #add the current number to the total
    total += num
    #how many non-zero numbers habe been entered
    num_counter += 1
    num = (int(input("Enter an integer, the input reads if it is 0: ")))
#prevents division by zero when calculating the average
if num_counter == 0:
    print("You did not enter any number")
else:
    avg = total / num_counter
    print("The number of positives is ",positive_count)
    print("The number of negatives is ",negative_count)

    print("The total is", total)
    print("The average is ", avg)