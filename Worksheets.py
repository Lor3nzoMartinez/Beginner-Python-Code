import sys

def isFactor(f,n):
    if f % n == 0 and n>= 2:
        return True
    else:
        return False

def listOfFactorsOf(n):
    f = n
    for n in range(1,61):
        if isFactor(f,n) == True:
            print(n,'is a factor of 20')


def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   

def tableOfPrimes(From,To,num_per_line):
    for n in range (From,To):
        if is_prime(n) == True:
            print(n)
        
tableOfPrimes(2,1000,1)

