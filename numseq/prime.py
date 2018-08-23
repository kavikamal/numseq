"""This module defines primes, and is_prime functions"""

from math import sqrt


def primes(n):
    """primes function returns a list of all primes less than n"""
    return [i for i in range(1, n+1) if i % 2 != 0]


def is_prime(m):
    """is_prime function returns a boolean indicating whether m is a prime number"""
    if m == 2:
        return True
    if m % 2 == 0 or m <= 1:
        return False
    sqr = int(sqrt(m)) + 1
    for divisor in range(3, sqr, 2):
        if m % divisor == 0:
            return False
    return True
