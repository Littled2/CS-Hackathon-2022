import turtle
from turtle import *

 
groupname="YourGroupName"
speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255


t = turtle.Turtle()

t.speed(0)

 

# Used to center

t.width(50)

t.up()

t.left(90)

t.forward(100)
t.color("aquamarine")
t.speed(400)

t.right(90)

t.down()

def polygon(n, side_length):

    for _ in range(n):

        t.right(360/n)

        t.forward(side_length)

   
def outher_line(ratio):
    forward(ratio*3)
    right(90)
    forward(ratio*4)
    circle(-ratio*4, 60)
    forward(ratio*1.2)

    penup()
    home()
    pendown()

    right(180)
    forward(ratio*3)
    right(-90)
    forward(ratio*4)
    circle(ratio*4, 60)
    forward(ratio*1.2)

def inner_line():
    penup()
    home()
    right(90)
    forward(30)
    pendown()
    left(90)

    outher_line(10)

 

polygon(500,2)


color("teal")
pensize(1)



outher_line(25)
inner_line()
mainloop()