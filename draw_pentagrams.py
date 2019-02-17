import math
from turtle import *
from draw_pentagram import draw_pentagram

BLOCK_ANGLE = 288
INIT_SIZE = 200
MIN_SIZE = 10
LIMIT_COUNT = 80

# scale styles
STYLE_DIAMOND_SCALE = 1
STYLE_STORM1_SCALE = (4 - math.sqrt(5))/2
STYLE_STORM2_SCALE = math.pow((math.sqrt(5)-1)/2, 1/5)
STYLE_SNAIL_SCALE = (math.sqrt(5)-1)/2
CURRENT_SCALE = STYLE_STORM1_SCALE


def draw_pentagrams(left_count, size):
    new_size = CURRENT_SCALE*size
    new_left_count = left_count - 1
    right(BLOCK_ANGLE)
    if new_size > MIN_SIZE:
        draw_pentagram(size)
        if new_left_count > 0:
            draw_pentagrams(new_left_count, new_size)


if __name__ == "__main__":
    speed(0)
    setpos(0, 0)
    hideturtle()
    draw_pentagrams(LIMIT_COUNT, INIT_SIZE)
    done()
