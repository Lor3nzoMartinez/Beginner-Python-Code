import math

def distance (x1, y1, x2, y2):
    del_x = x2 - x1
    del_y = y2 - y1
    dist_sqrd = del_x **2 + del_y **2
    return math.sqrt(dist_sqrd)

def trngl_perim (x1, y1, x2, y2, x3, y3):
    a = distance (x1, y1, x2, y2)
    b = distance (x3, y3, x2, y2)
    c = distance (x1, y1, x3, y3)
    return a + b + c

print(trngl_perim(0,0,3,3,5,5))
