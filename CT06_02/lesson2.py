print("Hello from lesson 2")

######## Write the pseudocode in comments for task 2 here
# Using comments, translate the code shown on screen into pseudocode.
# 1 Assign the value of the variable "counter" to 0
# 2.Make a repeat loop that stops once the varible counter reaches 50
# 3.Make it move 10 steps and then turn 15 degrees(clockwise). 
# 4.Each time that step 3 is completed, the varible "counter" should be increased by 10 




# ----- example 
# 1. Ask user for 1st number and name it num 1(num1 = input("1st number")
# 2. Ask user for 2nd number and name the varible num2
# 3. Add the value of num1 and num2 together and assign it to "ans"
#  4. Print out the value of Ans
#---------
# example
Num1 = int(input("1st Number?"))
Num2 = int(input("2nd Number?"))
# print(type(Num1))
# print(type(Num2))
# ^^ above prints the type of variables
ans = Num1 + Num2
print(ans)
######## Write the pseudocode in comments for task 3 here
# Using comments, translate the code shown on screen into pseudocode.
# Ask the user for his/her age.
# Save the input of the user to a varible called "answer"
# change the variable type to a integer(variable type that stores numbers)
# If the input(aka. age) of the user(stored in variable"answer") is under 18, it will print out "Acess Denied!"
# Otherwise,(aka. Else,) It will say "Welcome!"
# (bugs - if the user says a text in a integer, it will give an error)

# The robot creates the glass, paper, waste and plastic bin.(list)
# The robot creates a new variable called "items" and counts the number of items on the pad.
# After counting how many items are on the pad, it will put the value of that into the variable "items"
# The user inserts the item into the machine/robot.
# Ask the user what material it is.
# Check the item inserted into the robot.
# If the material of the item is glass, the robot will put it into the glass bin.(a list)
# If the material of the item is plastic, the robot will put it into the plastic bin.(a list)
# If the material of the item is paper, the robot will put it into the paper bin.(a list)
# Else, if the material is not glass, plastic, paper or just unrecognizable, the robot will put it into the incinerator.(a list called Others)
# The robot will repeat the process for the rest of the items.
# Task: Write down the steps on how to solve the problem below
# Design pseudocode for a recycling robot that sorts items
# into bins for glass, plastic, and paper. The robot should
# check each item's material and place it in the correct bin.
#  After each process, it will decrease the variable "item" by 1.
# It will repeat the process until the value of item is 0.
#---------------------------
# Task 3: Using pseudocode, design a program that will check if the
# user has entered the right secret phrase.

# 1. If the user has entered a wrong secret phrase, send them an
# error message.
# 2. If the user has entered the right secret phrase, congratulate
# them.
#  ----------
# 1. Set the secret phrase when the code has been run.
# Ask the user for the secret phrase and link the reply of the input into "ans".
# If the user says the wrong phrase, 
#   Send them an error message and tell them to run the code again to retry.
# Else
#   Congratulate them by printing Acess granted, Congrats!


# Task: Write a pseudocode that calculates the final score of a student
# based on the following weightage:
# _each test is scored upon 100_
# Test 1 = 20%
# Test 2 = 40%
# Test 3 = 40%

# Ask the user for their scores for all 3 scores in order.
# The computer first gathers the scores for each test
# Then, take the score of test 1 and multiply it by 20%(0.2)(assign the value of this to a valuable called T1)
# Then, take the score of test 2 and multiply it by 40%(0.4)(assign the value of this to a valuable called T2)
# Then, take the score of test 3 and multiply it by 40%(0.4)(assign the value of this to a valuable called T3)
# Add the numbers of all the variables(T1, T2, T3) and put it into a variable "ans".
# Then, print the variable "ans".
#  