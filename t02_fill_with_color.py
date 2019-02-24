from turtle import *
setup (width=500,height=500)
speed(0)
hideturtle()
color('red', '#ff6666')
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()

done()
