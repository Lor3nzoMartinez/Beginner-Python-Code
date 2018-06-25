def isFactor(f,n):
   return n % f == 0    

def listOfFactors(n):
    factors=[]
    for i in range(2,n):
        if isFactor(i,n):
            factors.append(i)
    return factors

def isPrime(n):
    if n == 1:
        return False
    return len(listOfFactors(n)) == 0

print(listOfFactors(9))
