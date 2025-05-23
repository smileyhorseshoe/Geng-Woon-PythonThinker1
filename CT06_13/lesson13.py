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
# HOW TO GET THE SIZE OF LIST
# length = len(list name)
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
# basket = [ ]
# catalog = [ ]
# item = " "
# while True:
#     item = input("Input an item you want to add to your store[Type End to complete.].")
#     if item == "End":
#         break
#     print("Success! You have added: " + str(item) )
#     catalog.append(item)
# print("Customer comes in.")

# while True:
#     customerneed = input("What are you looking for?[Type End to terminate.]")
#     if customerneed == "End":
#         break
#     if customerneed in catalog:
#         print("Yes, we sell that.")
#         basket.append(customerneed)
#     else:
#         print("Sorry, we dont have that.")
# print("You have bought: " + str(basket))
# HOW TO CHECK IF SOMETHING IS IN THE LIST
# if [something] in [list name]:

# Task 5: Lucky draw number generator
# Create a lucky draw number generator that generates 10 numbers
# between 1 to 9999.

# 1. Import the 'random' library
# 2. Using the 'random.randint()' function and a 'for' loop, add 10
#    random numbers into a list
# 3. Using another loop, announce the winners in the following format:
#     a. Winner #1: 5426
#     b. Winner #2: 3241
#     c. Etc...

# import random
# winners = ["" , ]
# for i in range(10):
#     i = random.randint(1 , 9999)
#     winners.append(i)
# num = 1
# while num < 11:
#     print("Winner #" , int(num) , winners[num])
#     num = num + 1


# Task 6: Pizza Topping
# Create a program that asks the user what pizza topping they want

# 1. Create a list of pizza toppings
# 2. Print out the list of pizza toppings with an index number next
#    to each of them in this format:
#     "1. Mushrooms"
#     "2. Pepperoni"
#     "3. Pineapple"
#     ...
# 3. In a 'while' loop, ask the user which pizza topping they want
#    (By index)
# 4. Exit the 'while' loop only when the user enters "end"
# 5. Print the toppings that the user has selected
# pizzaToppings = ["Mushrooms" , "Pineapple" , "Pepperoni" , "Sausage" ,"Onions", "Bacon" , "BBQ Chicken"]
# print(pizzaToppings)
# while True:
    # pizzatopping = input("Do you want any pizza toppings[Can choose more than one, type End to Terminate, No spaces.]")
    # if pizzatopping == "End":
        # break
    # if pizzatopping in pizzaToppings:
        # print("Added to your pizza.")
        # pizzaToppings.append(pizzatopping)
    # else:
        # print("Sorry, we dont have that. Try another one?")
# print("Extra Ingredients you've ordered:" , pizzaToppings)


# 13.6 Teacher solution
# Step 1: Create a list of pizza toppings
# pizza_toppings = ["Mushrooms", "Pepperoni", "Pineapple", "Onions", "Sausage", "Bacon", "Extra cheese", "Black olives", "Green peppers", "Fresh garlic"]
# user_toppings = []

# # Step 2: Use a 'for' loop to print the list of pizza toppings without using len() or enumerate()
# print("Available pizza toppings:")
# i = 1  # Manually track the index
# for topping in pizza_toppings:
#     print(str(i) + ". " + topping)
#     i += 1  # Increment the index manually

# # Step 3: Ask the user which pizza topping they want (By index)

# while True:
#     user_choice = input("Please choose your pizza topping by number: ")
#     if user_choice == "end":
#         break
#     else:
#         user_toppings.append(pizza_toppings[int(user_choice) - 1])

# for i in user_toppings:
#     print(i)

