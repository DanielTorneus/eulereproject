#! /usr/bin/env python3.3

# Authors: AmusableLemur
# Complexity: O(logn)
# Output: 4613732

# Fibonacci sequence
a = 1
b = 2
c = 3

sum = 0

while c < 4000000:
    # Calculate next number
    c = a + b

    # Update sequence
    a = b
    b = c

    if a % 2 == 0:
        sum += a

print(sum)
