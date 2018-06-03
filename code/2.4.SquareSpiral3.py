# SquareSpiral3.py - Draws a square spiral
# 画彩色正方形
import turtle
t = turtle.Pen()
t.pencolor("red")
for x in range(100):
    #移动距离
    t.forward(x)
    #向左转91°
    t.left(91)