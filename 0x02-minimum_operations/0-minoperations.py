#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
        @n: number of characters
        Return: minimum operations to copy paste
    """
    if n <= 1:
        return 0
    m = float("inf")
    for i in range(1, n//2+1):
        if n % i == 0:
            m = min(m, i + n//i)
    return m
