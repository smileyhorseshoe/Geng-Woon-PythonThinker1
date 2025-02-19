# Lesson 6 - Debugging

## Recap 1: Class Average Calculator

# You have been tasked to create a programme that calculates the
# average marks of a class.

# Your programme will have to ask the
# user for the total number of students, followed by the marks of
# each student one at a time.

# Use only variables, math operators that you have learnt, as
# well as a 'for' loop.
StudentNum = int(input("How many people do you have in your class?"))
Marks = 0
for StudentNum in range(StudentNum):
    Marks = Marks + int(input("What are their marks?"))
Marks = Marks / StudentNum
print("My sum is:" + str(Marks))
print("My average is" + str(Marks / StudentNum))