#!/usr/bin/env python
from turtle import *
from configs import *
edge_count = 5
angle = 72
# size = 8
size = 512
sin36 = math.sin(math.pi/5)
raduis = size / (2*sin36)

print(raduis)

def draw_body():
    penup()
    setpos(-size * (1 + GOLDEN_SECTION)/2,  raduis - size *sin36 )
    pendown()
    color1 = '#999999'
    color2 ='#666666'
    color(color1)
    begin_fill()

    forward(size*(1+GOLDEN_SECTION))
    right(108)
    for n in range(edge_count-2):
        forward(size)
        right(angle)
    end_fill()
    begin_fill()
    color(color2)
    for n in range(2):
        forward(size)
        right(angle)
    end_fill()
    


def draw_eyes():
    x = GOLDEN_SECTION * size/2
    y = raduis - size *( sin36 / 2 + 0.03)
    draw_eye(x, y)
    draw_eye(-x,y)
def draw_eye(x,y):
    eye_size = size*GOLDEN_SECTION
    eye_color1 = '#ddeeff'
    eye_color2 = '#000000'
    penup()
    setpos(x, y)
    dot(eye_size, eye_color1)
    pendown()

    penup()
    setpos(x, y*0.8)
    dot(eye_size*GOLDEN_SECTION/2, eye_color2)
    pendown()


def draw_head():
    penup()
    setpos(-size * (1 + GOLDEN_SECTION)/2, raduis  )
    setheading(0)
    pendown()

    color('#333333', '#333333')
    begin_fill()
    forward(size*(1+GOLDEN_SECTION))
    right(144)      
    forward(size)
    right(angle)
    forward(size)
    right(angle)
    end_fill()


def draw_center():
    penup()
    setpos(0,0)
    pendown()
    dot(5,'#ff0000')
    color('#ff3333')
    setheading(90)
    forward(raduis)


def main():
    setup (width=WINDOW_SIZE,height=WINDOW_SIZE)
    speed(0)
    draw_body()
    draw_eyes()
    draw_head()
    # draw_center()
    hideturtle()
    done()


if __name__ == "__main__":
    main()
