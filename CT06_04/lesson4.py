# print("Hello from lesson 4")

# Lesson 4 - Strings

## Recap 1: Sushi Checkout

# You just had a lunch at a sushi restaurant and have to
# calculate the total amount you have spent. Different coloured
# plates costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates, and 4
# green plates.

# Calculate and print the total amount you have spent: -->

#  Calculating red plates
#  1 red plate = $3
#  1 x $3 = $3
# redPlates = 3
# #  Calculating blue plates
# #  5 x $2 = $10
# bluePlates = 10
# # Calculating Green plates
# #  4 x $3 = $12
# greenPlates = 12
# Calculating total
# ans = greenPlates + bluePlates + redPlates

# Printing amount
# print("Your total is", ans, "dollars.")
# myName = input("What is your name?")
# print("Hello", myName, "welcome to coding!")

## Task 1: Storing and printing Strings

# **Task 1a**:
# Use the input() function to ask the user for their name and
# store it in a variable. Then print that variable.

# **Task 1b**:
# Ask the user for their favorite colour using input() and
# store the response in a variable. Print the variable.

# **Task 1c**:
# Ask the user for their age using input() and store the answer
# in a variable. Print the variable.

#  TASK 1a
# myName = input("What is your name?")
# print("Hello", myName)

# # TASK 1b
# favColour = input("What is your favorite colour?")
# print(favColour)

# # TASK 1c
# age = input("What is your age?")
# print(age)

# print("Hello,",myName,"your favourite colour is",favColour,"and you are",age,"this year.")
# print("A" + "B")


## Task 2: Input & string concatenation

# **Task 2a**:
# Ask the user for their name using input() and store it in a
# variable. 
# Concatenate the name with "Hi, [name]!" and print the
# complete message.

# **Task 2b**:
# Use input() to ask the user for their favorite hobby. Store this
# in a variable.
# Print a message saying "I enjoy [hobby]" using string
# concatenation.

# **Task 2c**:
# Ask the user for their dream vacation destination using input()
# and store it in a variable.
# Concatenate this variable with a phrase like "I would love to
# visit" and print the full sentence.

# Task 2A
# myName = input("What is your name?")
# print("Hello," + myName)

# #  TASK 2B
# myHobby = input("What is your favourite hobby?")
# print("Your favourite hobby is" + myHobby)

# #  TASK 2C
# dreamVacation = input("What is your dream vacation destination?")
# print("I would like to vist" + dreamVacation)

# # EXTRA
# print("Hello," + myName + " your hobby is" + myHobby + " Your dream vacation holiday place is" + dreamVacation)

# # --------------------------------------------------------------------------------
# **Task 3a**:
# 1. Ask the user for their current age using input(). Convert this
# to an integer.
# 2. Add 1 to their age and convert it back to a string.
# 3. Then print a message saying "Next year, you will be [age+1]
# years old."

# **Task 3b**:
# 1. Use input() to ask the user for a number. Convert this number
# from a string to an integer.
# 2. Double the number and convert it back to a string.
# 3. Print "Double your number is [double the number]".

# **Task 3c**:
# 1. Use input() to ask the user for the year they were born and
# convert it to an integer.
# 2. Subtract the birth year from the current year (assume the
# current year as an integer) to find their age.
# 3. Convert the age back to a string and print "You are [age]
# years old".]
age = int(input("What is your age?"))
age + 1
print("Next year, you will be" + str(age))