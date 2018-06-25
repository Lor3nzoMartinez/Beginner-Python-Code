import math

def answer (a,b,c):
    D = b**2 - 4 * a * c
    if D > 0:
        root_1 = (-b - math.sqrt(D))/(2*a)
        root_2 =(b - math.sqrt(D))/(2*a)
        return [root_1, root_2]
    elif D==0:
        root = -b/(2*a)
        return[root]
    elif D < 0:
        return []


print(answer(1,-1,-2))
print(answer(1,10,25))
print(answer(1,-2.5,-6.25))
print(answer(6,1,-12))
