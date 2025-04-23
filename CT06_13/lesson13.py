# Task 1: List of groceries
# **Task 1a**:
# Create a list of 8 groceries you need to buy:
# 1. Apples
# 2. Bread
# 3. Carrots
# 4. Dates
# 5. Eggs
# 6. Flour
# 7. Grapes
# 8. Honey

# groceries_list = ["Apples" , "Bread" , "Carrots" , "Dates" , "Eggs" , "Flour" , "Grapes" , "Honey"]
# groceries_list[7] = "Herbs"
# groceries_list.append("Ice")
# groceries_list.insert(1 , "Banana")
# del(groceries_list[2])
# print(groceries_list)



# TO ADD:
# USE EITHER:
# list.insert[index you want to insert]
# OR
# list.append("")
# HOW TO DELETE
# EITHER:
# 1. del(list[3])
# 2. list[NAME OF LIST].pop(index)

# Task 2: List of groceries (part 2)
# 1. Use a 'for' loop and print out all the groceries on your list
# 2. If grocery == "Apples", print "<grocery name>: I need 5 of these"
# 3. If grocery == "Carrots", print "<grocery name>: I need 3 of
#    these"
# 4. If name == "Grapes", print "<grocery name>: Get the FarmFresh
#    brand"

# groceries_list = ["Apples" , "Bread" , "Carrots" , "Dates" , "Eggs" , "Flour" , "Grapes" , "Honey"]
# groceries_list[7] = "Herbs"
# groceries_list.append("Ice")
# groceries_list.insert(1 , "Banana")
# del(groceries_list[2])
# for char in groceries_list:
#     print(char)
#     if char == "Apples":
#         del(groceries_list[1])
#         print(char + ": I need 5 of these.")
#     elif char == "Carrots":
#         print(char + ": I need 3 of these.")
#     elif char == "Grapes":
#         del(groceries_list[7])
        # print(char + ": Get the FarmFresh brand.")

# for grocery in groceries:
#     if grocery == "Apples":
#         print(grocery + ": I need 5 of these")
#     elif grocery == "Carrots":
#         print(grocery + ": I need 3 of these")
#     elif grocery == "Grapes":
#         print(grocery + ": Get the FarmFresh brand")
#     else:
# #         print(grocery)
# whattoadd = " "
# basket = [ ]
# while True:
    # whattoadd = input("What do you want to add to your basket?[Type end to exit.]")
    # if whattoadd == "end":
    #     break
    # basket.append(whattoadd)
    # print("You have added into your basket: " + whattoadd)
# for item in basket:
#     print("You have bought:" + item)

# Task 4: Online Catalogue
# **Task 4a**:
# Write a program to create an online catalogue for a grocery store.

# 1. Using a 'while' loop, ask the user (grocery store manager) to
#    input the items their online catalogue should have.
# 3. Add each item into the catalogue list
# 4. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the grocery store manager, do the
# following:

# 1. Imagine a customer browsing the website of the grocery store.
#    Ask the customer: "What are you looking for?"
# 2. If the item is in the list, say "Yes we sell that."
# 3. Else, say "Sorry, we don't have that."

catalog = [ ]
item = " "
while True:
    item = input("Input an item you want to add to your store.")
    if item == "end":
        break
    print("Success! You have added: " + str(item) )
    catalog.append(item)
print("Customer comes in.")

while True:
    customerneed = input("What are you looking for?[Type End to terminate.]")
    if customerneed == "End":
        break
    if customerneed in catalog:
        print("Yes, we sell that.")
    else:
        print("Sorry, we dont have that.")