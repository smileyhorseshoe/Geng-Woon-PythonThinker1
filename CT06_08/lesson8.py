# name = input("What is your name?")
# # Asking the user what their name i via 'input'.
# print("Nice to meet you, " + name +"!")
# # Printing a welcome script with their name given in the input.
# 
start = int(input("What is your starting number?"))
# Asking the user for the first number via an input(variable named "start")
end = int(input("What is your ending number?"))
#  Asking the user for the 2nd number via an input(variable named "end")
increment = int(input("What is your third number(increment)?"))
# Asking the user for the 3rd number via an input(increment)

#  Additional note: All numbers asked for has been converted to integers instead of strings.

for i in range(start , end , increment):
    print(i)
    i = start + increment
# Creating a repeat loop that adds the current number by the increment(e.g. 5 + 2 = 7 , 7 + 2 = 9) and stopping once the next multiple is the end number.


