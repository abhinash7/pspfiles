def bar_graph(abhi,value):
    abhi.begin_fill()
    abhi.left(90)
    abhi.forward(value)
    abhi.write(" "+str(value))
    abhi.right(90)
    abhi.forward(40)
    abhi.right(90)
    abhi.forward(value)
    abhi.left(90)
    abhi.end_fill()
    abhi.forward(10)

import turtle
t = turtle.Turtle()
a = turtle.Screen()
a.bgcolor("lightblue")
t.color("black" , "pink")
t.pensize(3)
measureheight=[20,45,60,85,100]
for i in measureheight:
    bar_graph(t,i)

