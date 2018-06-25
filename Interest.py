# Write a Python that assign the principal amount of $10000
# to variable P, assign to n the the value 12 and assign to r the
# the intrest rate of 8%. Then have the program prompt the user for 
# the number of years t that the money will be compounded for. Calculate
# and print the final amount after t years.

P = 10000
n = 12
r = 0.08

t = float(input("How many years? "))


t = P*(1+r/n)**n*t

print (t)


## Youtube Video:(Part 1 https://www.youtube.com/watch?v=E51y7lvphew)
## Youtube Video:(Part 2 https://www.youtube.com/watch?v=hhYUaozfMHI)
