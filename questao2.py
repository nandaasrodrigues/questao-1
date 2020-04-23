import turtle

def draw_poly(t, n, sz):
    angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)

# Allows us to use turtles
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
# Creates a playground for turtles
alex = turtle.Turtle()
alex.color("HotPink")
alex.pensize(3)

draw_poly(alex, 8, 50)

wn.mainloop()  
