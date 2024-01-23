from turtle import *
def t():
    i = 7


    left(90)
    fd(30)
    for x in range(i, 0, -1):
        for _ in range(2):
            fd(x*10)
            right(90)
        fd(x*10)
        left(90)
        fd(10)
        left(90)
    back(30)
    hideturtle()
    up()
    goto(-1000, 0)
    down()
    goto(1000, 0)
    input()

# t()
d_in_squares = 0
for x in range(1, 20000):
    d_in_squares += (x-1)**2
    d_total = d_in_squares + (x + (x+1)/2*x - 1)*3 - 2*x + 1
    if d_total >= 3300000:
        print(x-1)
        break


