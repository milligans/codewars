import math
def tankvol(h, d, vt):
    length= vt/(math.pi * ((d/2)**2))
    area_of_circle = math.pi*((d/2 **2))
    print (area_of_circle)
    volrem = h/d * vt
    print(volrem)

    return length, volrem