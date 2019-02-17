from PIL import ImageColor
def hsl2rgb(h,s,l):
    degreeH = 360*h
    print('degreeH',degreeH)
    (r,g,b)=ImageColor.getrgb("hsl(%f,%f%%,%f%%)"%(degreeH,s*100,l*100))
    return (r/255,g/255,b/255)