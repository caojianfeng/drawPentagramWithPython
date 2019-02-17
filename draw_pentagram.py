from time import sleep
import turtle
import math

edge_count = 5
angle=144

def draw_pentagram(t,size):
    for n in range(edge_count):
        t.forward(size)
        t.right(angle)

def main():
    t = turtle.Pen()
    t.setpos(-100,0)
    draw_pentagram(t,200)
    sleep(40)

if __name__ == "__main__":
    main()