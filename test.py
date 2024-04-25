import turtle
import random
turtle.shape("turtle")
shape=int(input("정수입력: (3:삼각형,4:사각형)"))
if shape==3:
    turtle.pencolor(random.random(),random.random(),random.random())
    turtle.pensize(3)
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.done()
elif shape==4:
    len=int(input("가로 길이입력:"))
    h=int(input("세로길이 입력:"))
    turtle.pencolor(random.random(),random.random(),random.random())
    turtle.pensize(7)
    for i in range(2):
        turtle.forward(len)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)
    turtle.done()