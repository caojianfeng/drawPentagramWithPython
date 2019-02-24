# draw pentagram with python

## Tutorials:

### tutorial 01:

The simplest code to draw a pentagram

![screen shot of tutorial 01](screen_capture/t01.png)

### tutorial 02:

Fill the pentagram with color

![screen shot of tutorial 02](screen_capture/t02.png)

### tutorial 03:

We need a edge only pentagram.
So we can fill the whole pentagram with color.

![screen shot of tutorial 03](screen_capture/t03.png)

### tutorial 04:

Move the pentagram to center of the window. final center at (0,0).
It is easy to kown , how to move the pentagram to the center of horizontal.
Move the start point from (0, 0) to (-100, 0) is what we want.

But how about the vertical center?
You need some math knowledge to resolve this.

This is how I get the Y_OFF.

`$GOLDEN\_SECTION ={\frac {{\sqrt {5}-1}}{2}}$`

`$CENTER\_YOFF ={\frac {{2GOLDEN\_SECTION-1}}{2}} * tan(54*\pi/180) * size$`

![screen shot of tutorial 04](screen_capture/t04.png)

### tutorial 05:

Draw a lot of pentagram at once

style == diamond
![screen shot of tutorial 05 style is  diamond](screen_capture/t05_DIAMOND.png)

style == snail
![screen shot of tutorial 05 style is  snail](screen_capture/t05_SNAIL.png)

style == storm1
![screen shot of tutorial 05 style is  storm1](screen_capture/t05_STORM1.png)

style == storm2
![screen shot of tutorial 05 style is  storm2](screen_capture/t05_STORM2.png)


### tutorial 06:
Draw a lot of pentagram with different colors

style == diamond
![screen shot of tutorial 06 style is  diamond](screen_capture/t06_DIAMOND.png)

style == snail
![screen shot of tutorial 06 style is  snail](screen_capture/t06_SNAIL.png)

style == storm1
![screen shot of tutorial 06 style is  storm1](screen_capture/t06_STORM1.png)

style == storm2
![screen shot of tutorial 06 style is  storm2](screen_capture/t06_STORM2.png)

## Truble shutting:

If you get a error "No module named 'PIL'"
you need to install Pillow

```bash
pip install Pillow
```
