def five_fact():
    '''Return 5!'''
    prod_acum = 1
    for i in range (1,11):
        prod_acum *=i
    return (prod_acum)

#print(five_fact())


    
def fact_n(n):
    '''Return n!, int n > 0.'''
    prod_acum = 1
    for i in range (1,n+1):
        prod_acum*=i

    return(prod_acum)

#print(fact_n(1))


def number_table(n):
    print("n          n!")
    print("-------------")
    for n in range (1,11):
        print(n,'        ', fact_n(n))

number_table(10)
