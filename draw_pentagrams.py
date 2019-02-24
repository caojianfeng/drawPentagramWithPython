#!/usr/bin/env python
import math
from turtle import *
from draw_pentagram import draw_pentagram
from configs import *

# scale styles
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
