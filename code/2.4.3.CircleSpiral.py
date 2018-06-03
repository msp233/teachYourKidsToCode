# CircleSpiral2.py - Draws a square spiral
# 画圆
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green"]
for x in range(100):
    t.pencolor(colors[x%4])
    #使用x作为半径
    t.circle(x)
    #向左转91°
    t.left(91)