# SquareSpiral3.py - Draws a square spiral
# 画四种颜色列表彩色正方形
import turtle
t = turtle.Pen();
#设置背景颜色
turtle.bgcolor("black")
colors = ["red","yellow","blue","green"]
# 下标 0-3
for x in range(100):
    # % 取模操作符，就是取余，得数是余数
    t.pencolor(colors[x%4])
    #移动距离
    t.forward(x)
    #向左转91°
    t.left(91)