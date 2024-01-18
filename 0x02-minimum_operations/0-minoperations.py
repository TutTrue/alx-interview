#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
        @n: number of characters
        Return: minimum operations to copy paste
    """
    if n <= 1:
        return 0

    num, div, res = n, 2, 0

    while num > 1:
        if num % div == 0:
            num /= div
            res += div
        else:
            div += 1
    return res
