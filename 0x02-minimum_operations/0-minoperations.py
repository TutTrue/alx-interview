#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
        @n: number of characters
        Return: minimum operations to copy paste
    """
    if n <= 1:
        return 0
    if n < 6:
        return n
    if n % 5 == 0:
        return 5 + n//5
    if n % 4 == 0:
        return 4 + n//4
    elif n % 3 == 0:
        return 3 + n//3
    elif n % 2 == 0:
        return 2 + n//2
    else:
        return 1 + n
