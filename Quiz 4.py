
Z = 0

def find_ints(n):
    Ints = []
    
    for n in range (1100,1301):
        
        if (n % 2 != 0) and (n % 13 == 0):
            Ints.append(n)
            
        elif (n % 2 != 0) and (n % 53 == 0):
            Ints.append(n)
            
    return Ints

        
Ints_L = find_ints(0)

print(Ints_L)




for i in Ints_L:
    Z += i
print(Z)

for i in Ints_L:
    
