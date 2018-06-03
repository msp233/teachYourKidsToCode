import turtle

t = turtle.Pen()
turtle.bgcolor("black")

r1 = int(turtle.textinput('花瓣半径','请输入花瓣半径'))
num = int(turtle.textinput('输入边数','你想画瓣花？'))
r2 = int(turtle.textinput('花蕊半径','请输入花蕊半径'))
for i in range(num):
    print (i)
    t.pencolor("yellow")
    t.circle(r2)
    t.pencolor('red')
    t.circle(r1)
    t.left(360 / num)