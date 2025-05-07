# 1. Write code below to print the 3rd item 
#    in this list using index e.g. earth
#  planets = mercury, venus, earth, muskworld, jupiter, saturn, neptune

# 2. Write code to append neptune to this list.


# 3. Elon Musk has conquered Mars. 
#    Rename Mars in the list to be "muskworld"


# 4. Remove uranus from this list.


# 5. Using a for loop, print all the planets 
#    from this list one by one.

# Defining the list
planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
# Q1:
print(planets[2])
# Q2:
planets.append("neptune")
# Q3:
planets[3] = "muskworld"
# Q4:
planets.pop(6)
# Q5:
for i in planets:
    print(i)