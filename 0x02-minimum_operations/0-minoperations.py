#!/usr/bin/python3
"""
:returns: the minimum number of operations
 to reach n characters starting with 1
"""


def minOperations(n: int) -> int:
    """
    Returns the minimum number of operations
     to reach n characters starting with 1
    """
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
