"""This module defines fib(n)"""


def fib(n):
    """fib function returns the nth Fibonacci number"""
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)