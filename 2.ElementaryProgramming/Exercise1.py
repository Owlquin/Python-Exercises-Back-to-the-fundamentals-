"""
(Convert square meter into ping) Write a program that converts square meter into ping.
The program prompts the user to enter a number in square meter, converts it to ping,
and displays the result. One square meter is 0.3025 ping.

"""

square_meters = float(input("Enter a number in square meters: "))
ping = square_meters * 0.3025
print(square_meters, "square meters is ", ping, " pings")
