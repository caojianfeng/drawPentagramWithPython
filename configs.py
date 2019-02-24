#!/usr/bin/env python
import math

STYLE_DIAMOND_SCALE = 1
STYLE_STORM1_SCALE = (4 - math.sqrt(5))/float(2)
STYLE_STORM2_SCALE = math.pow((math.sqrt(5)-1)/float(2),1/float(5))
STYLE_SNAIL_SCALE = (math.sqrt(5)-float(1))/float(2)
GOLDEN_SECTION = (math.sqrt(5)-1)/2
YOFF = 2 * GOLDEN_SECTION - 1

WINDOW_SIZE = 500
BLOCK_ANGLE = 288
INIT_SIZE = 200
MIN_SIZE = 3
LIMIT_COUNT = 80

if __name__ == "__main__":
    print(GOLDEN_SECTION);
    print(STYLE_STORM1_SCALE);
    print(STYLE_STORM2_SCALE);
    print(STYLE_SNAIL_SCALE);
# 0.61803398875
# 0.88196601125
# 0.908243862856
# 0.61803398875
