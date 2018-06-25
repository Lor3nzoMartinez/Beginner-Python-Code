'''
Other That Could Work

def num_of_sum_squares(amt):
    sum_acum = 0
    number = 1
    while sum_acum <= amt:
        sum_acum += number**2
        number += 1
    return number - 1
'''

def num_of_sum_squares(amt):
    sum_acum = 0
    number = 0
    while sum_acum <= amt:
        number += 1
        sum_acum += number**2
    return number 

print(num_of_sum_squares(13))

print(num_of_sum_squares(29))

print(num_of_sum_squares(30))
