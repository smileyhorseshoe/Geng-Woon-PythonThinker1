# Lesson 7 - For Loop (Part 2)

## Recap 1: Debugging Average Score Program

# ## There is a total of 3 bugs in the following program.
# ## Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three
# #  Changes made: "score_two + score+Three".
# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))
# Changes made: Changed variable average_score to string from integer.

# # Task 9: Accumulative Sum in Loop

# 1. Create a variable 'num' and assign the integer "0" to it
# 2. Create a 'for' loop that repeats 10 times
# 3. Add the sum of 'num' and the loop's parameter and print out
#    the value.
# 4. Observe what happens.

# Example:
# 1st iteration
#     num = num + i
#     print(num)

# 2nd iteration
#     num = num + i
#     print(num)

# ...

# 10th iteration
#     num = num + i
#     print(num)

# Output:
#     0
#     1
#     3
#     6
#     10
#     15
#     21
#     28
#     36
#     45

# num = 0
# for i in range(0, 10, 1):
#     num = num + i
#     print(num)


# ## Task 1: For Loop: 1 to 10 using range(start, stop)

# Use a 'for' loop to print numbers from 1 to 10.

# ---------------------------------------------------------------

# ## Task 2: Even Numbers 2-20 Loop using
# ##         range(start, stop, step)

# Print all even numbers between 2 and 20 using a 'for' loop and
# range().

# ---------------------------------------------------------------

# ## Task 3: Countdown From 10 For Loop

# Use a 'for' loop and range() to count down from 10 to 1.

#  TASK 1
# for i in range (1 , 11):
#     print(i)
# print("Task 1 done")
#  TASK 2
# for i in range(2, 21, 2):
#     print(i)
# Task 2 Done
# TASK 3
# for i in range(10 , 0 , -1):
#     print(i)                            
# Task 3 Done 

## Task 4: Word Repetition Input Loop

# Ask the user for a word and a number n. Print the word repeated
# n times (on separate lines).

# Example:
# What word would you like to repeat? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# burger
# burger
# burger
# Task 4
# word = input("Choose and enter one word.")
# for _ in range(3):
#     print(word)

## Task 5: Personalized Greeting Loop

# Ask for a user's name and an integer n, then print a
# personalized greeting n times.

# Example:
# What is your name? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# Nice to meet you, burger
# Nice to meet you, burger
# Nice to meet you, burger

# Task 5
# userName = input("What is your name?")
# repeatingTimes = int(input("How many times would you like to repeat the greeting(in numerals)?"))
# for _ in range(repeatingTimes):
#     print("Nice to meet you, "+ userName)


## Task 6: Sum of Five User Inputs

# Ask the user to input 5 numbers, one at a time, and print the
# sum of these numbers.

# Example:
# What is number #1? <<5>>
# What is number #2? <<2>>
# What is number #3? <<4>>
# What is number #4? <<1>>
# What is number #5? <<7>>

# output:
# Sum of the 5 numbers is 19 
# Task 6
# sum = 0
# for i in range(1 , 6):
#     sum = sum + int(input("What is number # "+str(i) + "?"))

# print("The sum of the 5 numbers you have chosen is " + str(sum))

## Task 7: Multiplication Table Generator

# Ask the user for a number, then print the multiplication table
# for that number from 1 to 12.

# Example:
# What number for the timestable? > << 5 >>
# output:
# 5 x 1 = 5
# 5 x 2 = 10
# ....
# ..
# 5 x 12 = 60

# numberTimes = int(input("What number for the timestable in numeral(will be printed 12 times.)"))
# for i in range(1 , 13):
#     print( str(numberTimes) + " x" , str(i) , "=" , str(numberTimes * i))

## Task 8: Number Pyramid Pattern

# 1. Ask the user for a number
# 2. Using the 'for' loop, print out the number like the
#    following:

# 1
# 22
# 333
# 4444
# 55555

# Hint: You can use a code like this >>> print("a" * 5) => aaaaa
number = int(input("choose a number and enter it in numerals"))
for i in range(1 , number + 1):
    print(str(number) * i)