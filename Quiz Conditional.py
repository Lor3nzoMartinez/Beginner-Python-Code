def tell_if_d3_and_not_d5 (num):
    d3 = num %3 == 0
    notd5=num %5 != 0
    cond = d3 and notd5
    if cond:
        print(num, 'is divisible by 3 but not divisible by 5')
    elif not cond:
        print(num, "is divisble  not by 3 and not divisible by 5")
     #else:

for num in range (2,21):
    tell_if_d3_and_not_d5(num)
