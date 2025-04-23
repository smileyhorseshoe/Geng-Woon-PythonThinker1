# print("Hello from lesson 14")
import turtle
window = turtle.Screen()
window.setup(width=600, height=400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("orange")
t.seth(0)
t.down()
# SQUARE
# for i in range(4):
#     t.left(90)
#     t.forward(50)
# HEXAGON
for i in range(6):
    t.left(60)
    t.forward(50)






















window.mainloop()
