#Task 1
# Print numbers from 10 to 200 using the while loop
# Your numbers must be in multiples of 10.
# 10 must be first number printed, and 200 the last number.

# Example: 10, 20, 30 ..... 180, 190, 200.
# Note that the numbers do not need to be printed in one line.
# Write your code here

num1 = 0
while num1 < 200:
    if num1 % 10 == 0:
        num1 = num1 + 10
        print(num1)

