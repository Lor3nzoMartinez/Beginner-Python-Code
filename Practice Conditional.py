def is_d7_d13 (num):
    Bool= (num % 2 != 0) and (num % 7 == 0) and (num % 13 == 0)
    if Bool:
        print ( num, 'is a canidate')
    else:
        return num

for num in range (1,501):
    is_d7_d13(num);
