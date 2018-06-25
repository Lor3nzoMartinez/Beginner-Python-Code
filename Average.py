
def average ():
    prod_acum=1
    for i in [ 2,5,8,12]:
        prod_acum *=i
    prod_acum *=4
    return prod_acum
        
print(average())


