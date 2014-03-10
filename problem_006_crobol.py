#! /usr/bin/env python3.3

# Authors: Crobol
# Complexity: O(1)
# Output: 25164150.0

def sum_squares(x):
    return (2 * (x**3) + 3 * (x**2) + x) / 6

def square_sums(x):
    return ((x + 1) * (x / 2)) ** 2

number = 100
print (square_sums(number) - sum_squares(number))
