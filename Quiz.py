Sum_Acum = 0

def divis (num):
    D17 = (num % 17 == 0)
    D37 = (num % 37 == 0)
    D47 = (num % 47 == 0)

    cond = D17 or D37 or D47

    if cond:
        print (num, 'happens')
    else:
        return num

for num in range (201,1001):
    divis(num)
    Sum_Acum += num
print(Sum_Acum)
