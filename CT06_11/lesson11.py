# Lesson 11 - AND OR NOT

# Recap 1: Purchase Advisor
# Create a program that asks the user for the price of an item (px) and
# gives a comment based on the price:
# if:
#     px <= 5: "Sounds good!"
#     px <= 50: "Are you sure you need this?"
#     px <= 500: "Where are you getting this money from?!"
#     px > 500: "Don't even think about it!"
# RECAP
# px = float(input("What is the price of the item you want to buy?"))

# if px <= 5:
#     print("Sounds good!") 
# elif px <= 50:
#     print("Are you sure you need this?")
# elif px <= 500:
#     print("Where are you even getting this money from?!")
# else:
#     print("Don't even think about it!")




# Task 1: AND Operator in Simple Conditions (AND)
# You are writing a program for an amusement park that needs to check
# if both riders of a ride are above the height of 120cm. Use the 'and'
# operator to determine if value of both 'rider1' and 'rider2' are
# greater than 120.

# rider1 = 125
# rider2 = 150
# >> True
# rider1 = 125
# rider2 = 150
# print("Rider 1's height is:" + str(rider1))
# print("Rider 2's height is:" + str(rider2))

# if rider1 > 120 and rider2 > 120:
#     print("All clear!")
# else:
#     print("Sorry, no can do!")

# Task 2: Multiples of 3 and 7 (AND)
# Create a program to check if a number is both divisible by 3 and 7

# 1. Ask the user to input a number
# 2. If the number is both a multiple of 3 and a multiple of 7:
#     print "The number is divisible by 3 and 7!"
numberCheck = int(input("Give me a number in numerals."))
if numberCheck % 3 == 0 and numberCheck % 7 == 0:
    print("This number is divisble by 3 and 7!")
else:
    print("This number is not divisible by 3 and 7!")