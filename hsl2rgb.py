from PIL import ImageColor

# h 0-360
# s 0-1.0
# l 0-1.0
# return (0-1.0,0-1.0,0-1.0)


def hsl2rgb(h, s, l):
    (r, g, b) = ImageColor.getrgb("hsl(%f,%f%%,%f%%)" %
                                  (h, s * 100, l * 100))
    return (r, g, b)

if __name__ == "__main__":
    print(hsl2rgb(0, 1, 0.5))
    # print(rgb2hsl(255, 1, 0.5))
