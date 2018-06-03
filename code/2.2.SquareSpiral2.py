# SquareSpiral2.py - Draws a square spiral
# 画正方形
import turtle
t = turtle.Pen()
for x in range(100):
    #移动距离
    t.forward(x)
    #向左转91°
    t.left(91)