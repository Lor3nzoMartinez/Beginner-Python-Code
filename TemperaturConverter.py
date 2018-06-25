def f2c(fahr):
    C = (fahr-32)*5/9
    return C

def f2k(F):
    K = f2c(F)+ 273.15
    return K
    
print(f2c(32))

print(f2k(32))
