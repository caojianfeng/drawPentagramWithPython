
from turtle import *
from configs import *
from draw_pentagram import draw_pentagram
import math

CENTER_YOFF = float(2 * GOLDEN_SECTION - 1)/float(2) * \
    tan(54*math.pi/180) * INIT_SIZE
COLOR_OLD = '#ff6666'
COLOR_H_CENTER = '#6666ff'
COLOR_V_CENTER = '#66ff66'
if __name__ == "__main__":
    setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
    print(CENTER_YOFF)

    # the orgin pos
    color(COLOR_OLD)
    draw_pentagram(200)

    # move to the horizontal center
    color(COLOR_OLD)
    penup()
    setpos(100, -CENTER_YOFF)
    pendown()
    setpos(0, -CENTER_YOFF)
    forward(CENTER_YOFF)

    penup()
    setpos(-100, 0)
    pendown()
    color(COLOR_H_CENTER)
    draw_pentagram(200)

    penup()
    setpos(-100, CENTER_YOFF)
    pendown()
    color(COLOR_V_CENTER)
    draw_pentagram(200)

    # move to the horizontal center
    color(COLOR_H_CENTER)
    penup()
    setpos(0, -CENTER_YOFF)
    pendown()
    setpos(0, 0)
    left(90)

    done()
