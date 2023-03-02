#!/usr/bin/python3
'''
A module that contain my pascal triangle function
implementation
'''


def _combination(n, r):
    '''Compute the combination of two variables'''
    from functools import reduce

    def n_fac(n):
        '''Find the factorial of an integer'''
        fac = 1
        for x in range(1, n+1):
            fac *= x
        return fac
    return n_fac(n) // (n_fac(n - r) * n_fac(r))


def pascal_triangle(n):
    '''Generates the pascal triangle for a power, excluding (x+y)^power'''
    assert type(n) == int
    if n <= 0:
        return []

    return [[1]] + [
        [_combination(x, y) for y in range(x+1)]
        for x in range(1, n)
    ]
