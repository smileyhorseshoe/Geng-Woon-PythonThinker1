# Task 1: Positive or Negative Numbers
# Write a program that will let the user know if the number they
# have entered is positive or negative.

# 1. Ask the user to input a number
# 2. Using an 'if' statement, check if the number is greater than 0
#         If it is, print "{number} is positive."
# 3. Use an 'else' statement for when the number is not greater than 0.
#         In this case, print "{number} is negative."
# number = int(input("Give me a number(NO DECIMALS!)"))
# if number > 0:
#     print("Your number is a positive number.")
# else:
#     print("Your number is a negative number.")

# Task 2: Random Number Guesser III
# Create a Random Number Guesser program

# 1. Generate a random integer between 1 to 10
# 2. Ask the user to guess a number
# 3. If the user guesses correctly:
#     print "Congratulations!! You did it!"
# 4. If the user guesses wrongly: 
#     print "Oops, better luck next time!"
# import random
# randomNumber = random.randint(1, 10)
# print(randomNumber)
# # CHECKING
# userAns = int(input("Guess a number from 1-10."))
# if randomNumber == userAns:
#     print("Congratulations!!! You guessed... Correctly!")
# else:
#     print("Oops, better luck next time!")

    # Task 3: Password Checker
# Code a password checker to protect your code!

# 1. Assign a password to a variable
# 2. Ask the user to enter a password
# 3. If the password matches, print "Login Successful"
# 4. If the password does not match, print "Password Incorrect"

pw = "Taco123!"

userInput = input("What is the password?")
if userInput == pw:
    print("Login sucessful!")
else:
    print("Password Incorrect.")