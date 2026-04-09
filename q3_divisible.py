Question 3: Divisibility Check
Problem:
Check if number is divisible by both 3 and 5.
Code:
Python
num = 15

# Check divisibility
if num % 3 == 0 and num % 5 == 0:
    print("Yes")
else:
    print("No")
Output:

Yes




✅ Question 5: Largest Number
Problem:
Find largest among three numbers.
Code:
Python
a = 10
b = 25
c = 15

# Find largest manually
largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print(largest)
Output:

25
