import math
from turtle import *
from draw_pentagram import draw_pentagram_edge, draw_pentagram
from hsl2rgb import *
from configs import *


HDEGREE = 30

CURRENT_SCALE = STYLE_STORM2_SCALE
LIMIT_COUNT = 5 if CURRENT_SCALE == STYLE_DIAMOND_SCALE else 30
DRAW_EDGE_ONLY = False if CURRENT_SCALE == STYLE_DIAMOND_SCALE else True


def draw_pentagrams(left_count, size, hsl_border, hsl_fill):
    if size <= MIN_SIZE:
        return
    if left_count == 0:
        return

    right(BLOCK_ANGLE)
    (bh, bs, bl) = hsl_border
    (fh, fs, fl) = hsl_fill

    colormode(255)
    color(hsl2rgb(bh, bs, bl), hsl2rgb(fh, fs, fl))
    # color((255,0,0), (255,187,187))
    begin_fill()
    if DRAW_EDGE_ONLY:
        draw_pentagram_edge(size)
    else:
        draw_pentagram(size)
    end_fill()

    new_size = size * CURRENT_SCALE
    new_left_count = left_count - 1
    new_hsl_border = (bh + HDEGREE, bs, bl)
    new_hsl_fill = (fh + HDEGREE, fs, fl)

    draw_pentagrams(new_left_count, new_size, new_hsl_border, new_hsl_fill)


if __name__ == "__main__":
    setup (width=WINDOW_SIZE,height=WINDOW_SIZE)
    speed(0)
    setpos(0, 0)
    hideturtle()
    draw_pentagrams(LIMIT_COUNT, INIT_SIZE, (36, 1.0, 0.5), (0, 1.0, 0.7))
    print(screensize())
    done()
