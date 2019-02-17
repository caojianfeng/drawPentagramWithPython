import math
from turtle import *
from draw_pentagram import draw_pentagram
from hsl2rgb import *
BLOCK_ANGLE = 288
INIT_SIZE = 200
MIN_SIZE = 10
LIMIT_COUNT = 80

# scale styles
STYLE_DIAMOND_SCALE = 1
STYLE_STORM1_SCALE = (4 - math.sqrt(5)) / 2
STYLE_STORM2_SCALE = math.pow((math.sqrt(5) - 1) / 2, 1 / 5)
STYLE_SNAIL_SCALE = (math.sqrt(5) - 1) / 2
CURRENT_SCALE = STYLE_SNAIL_SCALE
HDEGREE = 30


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
    draw_pentagram(size)
    end_fill()

    new_size = size * CURRENT_SCALE
    new_left_count = left_count - 1
    new_hsl_border = (bh + HDEGREE, bs, bl)
    new_hsl_fill = (fh + HDEGREE, fs, fl)

    draw_pentagrams(new_left_count, new_size, new_hsl_border, new_hsl_fill)


if __name__ == "__main__":
    speed(0)
    setpos(0, 0)
    hideturtle()
    draw_pentagrams(LIMIT_COUNT, INIT_SIZE, (180, 1.0, 0.5), (0, 1.0, 0.5))
    done()
