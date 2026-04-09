###-----Problem:
Check if a year is leap year.
Code:
Python
year = 2024

# Leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
Output:

Leap Year
