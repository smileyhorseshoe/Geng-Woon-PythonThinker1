
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
# visitor = 1
# while visitor < 51:
#     print("Visitor Count:" + str(visitor))
#     visitor += 1
# print("The venue has reached its max capacity! Do not accept anymore visitors!")
# 1b.
# maxVisitor = 30
# visitorPresence = 18
# while visitorPresence < maxVisitor:
#     visitorPresence =+ 1
#     print("Visitor Count:" + str(visitorPresence))
# print("The venue has reached its max capacity! Do not accept anymore visitors!")
# 1c
maxVisitor = 25
visitorPresence = 4
while visitorPresence < maxVisitor:
    visitorPresence =+ 1
    print("Visitor Count:" + str(visitorPresence))
print("The venue has reached its max capacity! Do not accept anymore visitors!")