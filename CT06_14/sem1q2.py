planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
# 1. Write code below to print the 3rd item 
#    in this list using index e.g. earth
#  planets = mercury, venus, earth, muskworld, jupiter, saturn, neptune

# 2. Write code to append neptune to this list.


# 3. Elon Musk has conquered Mars. 
#    Rename Mars in the list to be "muskworld"


# 4. Remove uranus from this list.


# 5. Using a for loop, print all the planets 
#    from this list one by one.

print(planets[2])
planets.append("neptune")
planets[3] = "muskworld"
planets.pop(6)
print("List of Planets")
for i in planets:
    print(i)