import math
from turtle import *
from draw_pentagram import draw_pentagram

edge_count = 5
angle = 144
block_angle = 288
init_size = 200
# scale = (4- math.sqrt(5))/2
# scale = (math.sqrt(5)-1)/2
scale = math.pow((math.sqrt(5)-1)/2, 1/5)

speed(0)
setpos(0, 0)
hideturtle()


def draw_next_pentagram(size):
    new_size = scale*size
    right(block_angle)
    if new_size > 10:
        draw_pentagram(size)
        draw_next_pentagram(new_size)


if __name__ == "__main__":
    draw_next_pentagram(init_size)
    done()
