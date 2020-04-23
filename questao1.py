import turtle

def draw_square(t, sz):
#Make turtle t draw a square of sz.
    for i in range(4):
        t.forward(sz)
        t.left(90)


# Allows us to use turtles
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
# Creates a playground for turtles
alex = turtle.Turtle()
alex.color("HotPink")
alex.pensize(3)

for i in range(1,6):
    draw_square(alex,20*i)
    alex.penup()
    alex.setposition(-10*i, -10*i)
    alex.pendown()

wn.mainloop()    