## Task 1: Self-introduction
# You are at a party, and you expect to see your friend Ethan and 3 of
# his friends you have never met before. They are Ben, Gracie, and
# Javior.

# Write a program (with or without functions) that will ask the user
# for their name and print 1 of 3 ways to greet the person:
# 1. If the person is Ethan, greet him by saying:
#         "Hi Ethan. How are you?"
# 2. If the person is either Ben, Gracie, or Javior, greet them by
#    saying:
#         "Hi there!"
#         "My name is Freddo"
#         "I like to swim and eat chicken wings!"
#         "Nice to meet you!"
# 3. If the person is none of the above, say:
#         "I don't think you belong here..."
# def greetings():
#     name = input("What is your name?")
# def Ethan():
#     print("Hi Eathen. How are you?")
# def Friends(): 
#     print("Hi there!")
#     print("My name is Freddo")
#     print("I like to eat chicken wings!)")
#     print("Nice to meet you!")
# def unknown():
#     print("I don't think you belong here... GET OUT!")
# if name == "Ethan":
#     Ethan()
# elif name == "Ben":

## Task 3: Increment Counter
# Create a function that will increase the 'counter' variable by 1 each
# time it is called.

# 1. Create a 'counter' variable and assign it '0'
# 2. Define a function 'increment_counter()':
#         a. Declare 'counter' as 'global'
#         b. Add 1 to 'counter'
# 3. Test your program out by calling the 'increment_counter()' function
# 4. 3 times before printing out the value of the 'counter' variable.

# Your output should be "3"

# counter = 0
# def increment():
#     global counter
#     counter += 1
# for i in range(3):
#     increment()
# print(counter)

## Task 5: Double the Number
# Create a function that takes in a number and doubles it

# 1. Create a function named 'doubleNumber()'
# 2. The function should return the doubled number
# 3. Using the 'doubleNumber()' function, print the doubles of the
#    following numbers:
#     4
#     9
#     1530
#     284
# def doubleNumber(number):
#     number = number * 2 
#     print(number)

# uinum = int(input("What is the number that you want to double?"))
# doubleNumber(uinum)


## Task 6: Greetings III
# Create a function that takes in a name and returns a greeting

# 1. Create a function named 'greet()'
# 2. The function should return a greeting
#     Example: "Hello there <name>!"
# 3. Ask the user for their name
# 4. Using the 'greet()' function, print the greeting

# def greet(name):
#     print("Hello there," + name + "!")


# greet(input("What is your name?"))


## Task 7: Even or Odd? III
# Create a function that takes in a number and returns whether it is
# even

# 1. Create a function named isEven()
# 2. If the number is even, the function should return True
# 3. If the number is odd, the function should return False
# 4. Using the 'isEven()' function, loop through a list of numbers and
#    print them out in this format:
#     "3 is an odd number"
#     "9 is an odd number"
#     "2 is an even number"
num = [ ]
def isEven(number):
    print(number % 2 == 0)
import random
for i in range(10):
    random.randint(1, 100000000)
    num.append(i)
for i in num:
    isEven(i)
    