#####------- Question 5: Largest Number
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
