import math

def circle_area(r):
    A = math.pi*r**2
    return round((A),3)

for i in [1,3,7,10]:
    print(circle_area(i))
