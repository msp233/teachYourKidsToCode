import turtle

t = turtle.Pen()
turtle.bgcolor("black")

r = int(turtle.textinput('Enter circle width','Please enter circle width'))
num = int(turtle.textinput('输入边数','你想画几个圆？'))
for i in range(num):
    print (i)
    t.pencolor("orange")
    t.circle(r)
    t.left(360 / num)