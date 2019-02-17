from turtle import *
color('red', '#ff6666')
begin_fill()
speed(0) 
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()
hideturtle()
done()