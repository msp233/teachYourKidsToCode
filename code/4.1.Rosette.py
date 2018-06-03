import turtle

t = turtle.Pen()
turtle.bgcolor("black")

width = int(turtle.textinput('Enter circle width','Please enter circle width'))
for i in range(0,4):
    print (i)
    t.pencolor("orange")
    t.circle(width)
    t.left(90)