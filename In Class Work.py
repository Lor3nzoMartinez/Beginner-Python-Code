def sumSqrs_diffSqrs(x,y):
    X = x**2 + y**2
    Y = x**2 - y**2
    return X, Y

A,B = sumSqrs_diffSqrs(4,2)

print(A,B)

