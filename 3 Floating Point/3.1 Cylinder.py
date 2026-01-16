import math

def circle_area(r):
    return math.pow(r,2)*math.pi

def circle_circumference(r):
    return 2*math.pi*r

def cylinder_area(r,h):
    return 2*circle_area(r) + circle_circumference(r)*h