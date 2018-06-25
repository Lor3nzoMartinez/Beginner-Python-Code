def smlstPwrOf3LrgrThan(t):
    number = 0
    while 3**number <= t:
        number += 1
    return number
'''
for t in range (25,30):
    p = smlstPwrOf3LrgrThan(t)
    print('threshold = ' ,t,', smlstPwrOf3LrgrThan(threshold) = ',p,end = ',')
    print('3**(smallestPwrPf3LT(thereshold) = ',3**p)
'''
print(smlstPwrOf3LrgrThan(991274426))
