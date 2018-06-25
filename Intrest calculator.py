def final_amt(p,r,n,t):
    a = p*(1+r/n)**(n*t)
    return a
print('Year         $amt')

for t in range(20):
    print(t , '          ' , round(final_amt(1050,0.05,1,t),2))
