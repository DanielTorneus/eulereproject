#! /usr/bin/env python3.3

# Author: Crobol
# Complexity: ?
# Output: 906609

def is_palindrome(n):
    return str(n) == str(n)[::-1]

answer = max(
            filter(
                is_palindrome, 
                (x * y for x in range(100, 999) for y in range(100, 999))
            )
        )

print(answer)
