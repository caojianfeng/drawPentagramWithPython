from turtle import *

edge_count = 5
angle = 144


def draw_pentagram(size):
    for n in range(edge_count):
        forward(size)
        right(angle)


def main():
    setpos(-100, 0)
    draw_pentagram(200)
    done()


if __name__ == "__main__":
    main()
