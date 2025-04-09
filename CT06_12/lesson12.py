
# Task 1: Introduction to while loop
# **Task 1a**:
# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count

# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30

# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25
# 1a.
# print("1a")
# visitor = 1
# while visitor < 51:
#     print("Visitor Count:" + str(visitor))
#     visitor += 1
# print("The venue has reached its max capacity! Do not accept anymore visitors!")
# # 1b.
# print("1b")
# maxVisitor = 30
# visitorPresence = 18
# while visitorPresence < maxVisitor:
#     visitorPresence =+ 1
#     print("Visitor Count:" + str(visitorPresence))
# print("The venue has reached its max capacity! Do not accept anymore visitors!")
# # 1c
# print("1c")
# maxVisitor = 25
# visitorPresence = 4
# while visitorPresence < maxVisitor:
#     visitorPresence =+ 1
#     print("Visitor Count:" + str(visitorPresence))
# print("The venue has reached its max capacity! Do not accept anymore visitors!")


# Task 2: while... break
# A restaurant used to have a max capacity of 50. However, due to
# the worsening of the pandemic, the government has restricted the
# max capacity of the restaurant to 30.

# Using an 'if' condition and 'break' within the 'while' loop,
# modify your answer for Task 1a to terminate the 'while' loop when
# number of visitors is 30.
# visitorsMax = 50
# presentVisitors = 1
# print("NEW LIMIT: 30.")
# while presentVisitors <= 50:
#     presentVisitors += 1
#     print("Visitor count = " + str(presentVisitors))
#     if presentVisitors == 30:
#          break
# print("Visitors in the venue:" + str(presentVisitors) + "No more visitors as the venue has reached its full capcity!")

# # Task 3: Order taking using while loop
# Using what you have learnt so far, code a program to take a
# customer's order.

# Declare a variable called 'order' and assign an empty string
# variable "" to it.

# Using a 'while' loop:
# 1. Ask the user to enter their order
# 2. For each order entered, concatenate to the 'order' variable.
# 3. Exit the 'while' loop if the user enters "end"
# 4. On program end, print out the customer's order.

# **Bonus**
# 1. Modify your code to remove the comma (",") that appears
#    either at the start or end of your sentence-*
order = ""
while True:
    item = input("What would you like to order today?(If nothing else say end)")
    if item == "end":
        break
    else:
        order = order + item
print(order)