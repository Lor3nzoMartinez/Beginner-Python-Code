def count_odds(list):
    sum_acum = 0
    if list % 2 !=0:
        sum_acum +=1
    return sum_acum

num = [1,2,3,4,5,6,7,8,9]

print(count_odds(num))
