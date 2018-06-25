
## Quiz 8

## Number 1


def IsTwinPrime(n):
    List = [True] * n
    if n > 0:
        List[0] = False
        if n > 1:
            List[1] = False
    for number in range(2, int(n ** 0.5) + 1):
        if List[number]:
            for index in range(number * number, n, number):
                List[index] = False
    return [(a, b) for b, a in enumerate(range(0, n - 2), start=2) if List[a] and List[b]]

print(*find_prime_pairs(100), sep='\n')

## Number 2
'''
def endingDigitOf(n):
    if n < 9:
        return n
    else:
        return ((n % 10))
    
for n in range(1000):
    print(endingDigitOf(n))
'''
