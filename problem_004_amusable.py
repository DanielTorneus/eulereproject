#! /usr/bin/env python3.3

# Authors: AmusableLemur
# Complexity: O(n^2)
# Output: 906609

number = 0

# Could possibly avoid checking duplicates here
for i in xrange(100, 999):
	for j in xrange(100, 999):
		n = i * j

		if str(n) == str(n)[::-1] and n > number:
			number = n

print(number)
