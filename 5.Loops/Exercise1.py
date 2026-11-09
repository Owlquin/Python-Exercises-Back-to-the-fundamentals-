"""
#(Conversion from kilograms to pounds) Write a program that
displays the following table
(note that 1 kilogram is 2.2 pounds)
"""

print(f"{'Kilograms':<15}{'Pounds':<10}")
print("-------------------")

for kilograms in range(1,200,2):
    pounds = kilograms * 2.2
    print(f"{kilograms:<15}{pounds:<10.1f}")