#! /usr/bin/env python3.3

# Authors: AmusableLemur
# Complexity: O(nlogn)
# Output: 104743

from math import sqrt

primes = [2]

def is_prime(n):
	# We really only need to check against primes
	for i in primes:
		if n % i == 0:
			return False

	primes.append(n)

	return True

counter = 1
number = 3

while counter < 10001:
	# Skip even numbers
	number += 2

	if is_prime(number):
		counter += 1

print(number)

