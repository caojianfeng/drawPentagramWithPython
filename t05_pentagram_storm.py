import math
from turtle import *
from draw_pentagram import draw_pentagram_edge
from draw_pentagram import draw_pentagram
from configs import *

CURRENT_SCALE = STYLE_DIAMOND_SCALE
LIMIT_COUNT = 8 if CURRENT_SCALE == STYLE_DIAMOND_SCALE else 30
DRAW_EDGE_ONLY = False if CURRENT_SCALE == STYLE_DIAMOND_SCALE else True

def draw_pentagrams(left_count, size):
    if size <= MIN_SIZE:
        return
    if left_count == 0:
        return

    right(BLOCK_ANGLE)
    color('red', '#ff6666')
    begin_fill()
    if DRAW_EDGE_ONLY:
        draw_pentagram_edge(size)
    else:
        draw_pentagram(size)
    end_fill()
    new_size = CURRENT_SCALE * size
    new_left_count = left_count - 1
    draw_pentagrams(new_left_count, new_size)


if __name__ == "__main__":
    setup (width=WINDOW_SIZE,height=WINDOW_SIZE)
    speed(0)
    setpos(0, 0)
    hideturtle()
    draw_pentagrams(LIMIT_COUNT, INIT_SIZE)
    done()
