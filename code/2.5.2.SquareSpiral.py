# SquareSpiral3.py - Draws a square spiral
# 画彩色，2-6边形 ，边数由用户指定
# 橡皮筋球体
import turtle
t = turtle.Pen();
#设置背景颜色
turtle.bgcolor("black")
#You can choose between 2 and 6 sides for some cool shapes!
sides = eval(input('Enter a number of sides between 2 and 6:'))
colors = ["red","yellow","blue","orange","green","purple"]
# 下标 0-3
for x in range(360):
    # % 取模操作符，就是取余，得数是余数
    t.pencolor(colors[x%sides])
    #移动距离
    t.forward(x*3/sides +x)
    #向左转(360/sides+1)°
    t.left(360/sides+1)
    t.width(x*sides/200)
    t.left(90)