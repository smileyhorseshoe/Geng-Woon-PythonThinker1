# Recap 1: Dice Roll Simulator
# Generate and print 3 random numbers between 1 and 6, followed
# by an output of 'True' if all 3 numbers are either even or odd.

# Example:
# 1st number: 6
# 2nd number: 4
# 3rd number: 6
# All numbers are even/odd: True

# 1. Import the 'random' library: DONE
# 2. Create 3 variables to hold a random number that is between
#    1 and 6, generated using 'random.randint()': DONE
# 3. Using string concatenation, print the generated number for
#    each of the 3 numbers: ??
# 4. Using the '%' and '==' operator, check if each number is
#    divisible by 2 (remainder = 0)
# 5. Using multiple '==' operators, a new variable 'all_even_odd'
#    should be assigned 'True' if all 3 numbers are either all
#    even or all odd numbers.
# 6. Print if "All numbers are even/odd" is 'True' or 'False'
# import random

# num1 = random.randint(1 , 6)
# num2 = random.randint(1 , 6)
# num3 = random.randint(1 , 6)
# print("Number 1:" + str(num1))
# print("Number 2:" + str(num2))
# print("Number 3:" + str(num3))
# num1 % 2
# num2 % 2
# num3 % 2
# print(num1 and num2 and num3 == 0 or num1 and num2 and num3 == 1)
# NOT WORKING

# Teacher solution
# import random
# num1, num2, num3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)
# print("1st number: " + str(num1))
# print("2nd number: " + str(num2))
# print("3rd number: " + str(num3))
# all_even_odd = (num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0) or (num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1)
# print("All numbers are even/odd is " + str(all_even_odd))
