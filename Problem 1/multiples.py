# Current solution: O(k) ?
import math

number = 1000-1
x = math.trunc(number/3)
y = math.trunc(number/5)
z = math.trunc(number/15)

X = (x*(x-1)/2 + x)*3
Y = (y*(y-1)/2 + y)*5
Z = (z*(z-1)/2 + z)*15

total = X + Y - Z

print total
