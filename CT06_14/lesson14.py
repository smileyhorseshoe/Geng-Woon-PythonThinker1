# print("Hello from lesson 14")
import turtle
window = turtle.Screen()
window.setup(width=600, height=400)
t = turtle.Turtle()
t.fillcolor("orange")
t.shape("turtle")
# Pentagon
# for i in range(5):
#     t.forward(50)
#     t.left(72)
# Square
# for i in range(3):
#     t.forward(50)
#     t.left(90)
# Hexagon
# for i in range(6):
#     t.forward(50)
#     t.left(60)
# Circles
# for i in range(360):
#     t.forward(1)
# #     t.left(1)
# CROSSHAIR[ALPHA]
# t.penup()
# t.goto(-300 , 0)
# t.pendown()
# t.setx(300)
# t.penup()
# t.goto(0, -200)
# t.pendown()
# t.sety(200)
import random
for i in range(10):
    t.penup()
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    y = y - 40
    t.goto(x , y)
    for i in range(4):
        t.pendown()
        t.forward(5)
        t.left(90)
    text = x , y # (-10, 50)
    t.write(text , align="center")
t.penup()
t.goto(-300 , -200)







































































window.mainloop()
