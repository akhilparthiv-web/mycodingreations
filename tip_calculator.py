from math import *
x = input("how much was the dinner?: ")
total_sub = float(x)
y = input("how much do you want to tip?(don't  enter the percent sign): ")
tip = float(y)
z = input('how much is the tax: ')
totwtax = total_sub * (1 + (float(z)/100))
tot = totwtax * (1 + (tip/100))
print(round(tot, 2))