"""This module defines square, triangle, and cube functions"""


def square(n):
    """ square function returns the square of a number """
    return n**2


def triangle(m):
    """ triangle function returns a triangles of a number """
    result = 0
    for i in range(1, m+1):
        result += i
    return result


def cube(n):
    """ cube function returns the cube value of a number """
    return n ** 3
