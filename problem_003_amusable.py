#! /usr/bin/env python3.3

# Authors: AmusableLemur
# Complexity: O(logn)
# Output: 6857

from math import sqrt

number = 600851475143
i = 2

while i < number:
	while number % i == 0:
		number = number / i

	i += 1

print(number)
