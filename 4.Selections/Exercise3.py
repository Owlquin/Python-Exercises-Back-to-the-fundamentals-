"""
(Find future dates) Write a program that prompts the user
to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and
Saturday is 6). Also
prompt the user to enter the number of days after today for

a future day and dis-
play the future day of the week.

"""
print("Enter today's day: ")
day = int(input())

print("Enter the number of days elapsed since today: ")
elapsed_day = int(input())

#for the future days up to 31, uses modulus going past
#6 ... ex 6(day) + 9(elapsed) = 15 ... 15 % 7 = 2 which
#would be monday and if the future day is less than 7
future_date = (day + elapsed_day) % 7
#shows the current day
if day == 0:
    day_name = "Sunday"
elif day == 1:
    day_name = "Monday"
elif day == 2:
    day_name = "Tuesday"
elif day == 3:
    day_name = "Wednesday"
elif day == 4:
    day_name = "Thursday"
elif day == 5:
    day_name = "Friday"
elif day == 6:
    day_name = "Saturday"
else:
    day_name = "Invalid day"
#shows the future day
if future_date == 0:
    future_day_name = "Sunday"

elif future_date == 1:
    future_day_name = "Monday"
elif future_date == 2:
    future_day_name = "Tuesday"
elif future_date == 3:
    future_day_name = "Wednesday"
elif future_date == 4:
    future_day_name = "Thursday"
elif future_date == 5:
    future_day_name = "Friday"
elif future_date == 6:
    future_day_name = "Saturday"
else:
    future_day_name = "Unknown"

print("Today is", day_name, "and the future day is",
future_day_name )