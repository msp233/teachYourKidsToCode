# CircleSpiral2.py - Draws a square spiral
# 画圆
import turtle
t = turtle.Pen()
for x in range(100):
    #使用x作为半径
    t.circle(x)
    #向左转91°
    t.left(91)