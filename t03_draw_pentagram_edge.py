from turtle import *

from configs import *
edge_count = 5
angle = 144
angle_out = -72
def draw_pentagram_edge(size):
    for n in range(edge_count*2):
        forward(size*(1-GOLDEN_SECTION))
        right(angle_out if n % 2 == 0 else angle)

if __name__ == "__main__":
    setup (width=WINDOW_SIZE,height=WINDOW_SIZE)
    speed(0)
    hideturtle()
    color('red', '#ff6666')
    begin_fill()
    draw_pentagram_edge(200)
    end_fill()
    done()
