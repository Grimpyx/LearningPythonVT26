import math

def extrapolate(x1,y1,x2,y2,x):
    k = (y2-y1)/(x2-x1)
    m = (y1*x2-y2*x1)/(x2-x1)
    return k*x + m