from PIL import ImageColor

def RGB_to_HSL(r, g, b):
    ''' Converts RGB colorspace to HSL (Hue/Saturation/Value) colorspace.
        Formula from http://www.easyrgb.com/math.php?MATH=M18#text18

        Input:
            (r,g,b) (integers 0...255) : RGB values

        Ouput:
            (h,s,l) (floats 0...1): corresponding HSL values

        Example:
            >>> print RGB_to_HSL(110,82,224)
            (0.69953051643192476, 0.69607843137254899, 0.59999999999999998)
            >>> h,s,l = RGB_to_HSL(110,82,224)
            >>> print s
            0.696078431373
    '''
    # if not (0 <= r <= 255):
    #     raise ValueError, "r (red) parameter must be between 0 and 255."
    # if not (0 <= g <= 255):
    #     raise ValueError, "g (green) parameter must be between 0 and 255."
    # if not (0 <= b <= 255):
    #     raise ValueError, "b (blue) parameter must be between 0 and 255."

    var_R = r / 255.0
    var_G = g / 255.0
    var_B = b / 255.0

    var_Min = min(var_R, var_G, var_B)    # Min. value of RGB
    var_Max = max(var_R, var_G, var_B)    # Max. value of RGB
    del_Max = var_Max - var_Min             # Delta RGB value

    l = (var_Max + var_Min) / 2.0
    h = 0.0
    s = 0.0
    if del_Max != 0.0:
        if l < 0.5:
            s = del_Max / (var_Max + var_Min)
        else:
            s = del_Max / (2.0 - var_Max - var_Min)
        del_R = (((var_Max - var_R) / 6.0) + (del_Max / 2.0)) / del_Max
        del_G = (((var_Max - var_G) / 6.0) + (del_Max / 2.0)) / del_Max
        del_B = (((var_Max - var_B) / 6.0) + (del_Max / 2.0)) / del_Max
        if var_R == var_Max:
            h = del_B - del_G
        elif var_G == var_Max:
            h = (1.0 / 3.0) + del_R - del_B
        elif var_B == var_Max:
            h = (2.0 / 3.0) + del_G - del_R
        while h < 0.0:
            h += 1.0
        while h > 1.0:
            h -= 1.0

    return (h, s, l)


# h 0-360
# s 0-1.0
# l 0-1.0
# return (0-1.0,0-1.0,0-1.0)


def hsl2rgb(h, s, l):
    (r, g, b) = ImageColor.getrgb("hsl(%f,%f%%,%f%%)" %
                                  (h, s * 100, l * 100))
    return (r, g, b)


def rgb2hsl(r, g, b):
    return RGB_to_HSL(r,g,b)


if __name__ == "__main__":
    # print(hsl2rgb(0, 1, 0.5))
    print('{}')
    print(rgb2hsl(255, 102, 102))
    print('}')
