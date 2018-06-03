# SquareSpiral1.py - Draws a square spiral
import turtle
#使用字母t表示海龟的钢笔
t = turtle.Pen()
for x in range(100):
    #移动距离
    t.forward(x)
    #向左转90°
    t.left(90)