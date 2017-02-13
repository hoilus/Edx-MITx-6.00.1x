# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:42:00 2016

"""

def general_poly(L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def inner(x):
        res = 0
        n = len(L)-1
        for e in range(len(L)):
            res += L[e]*x**n
            n -= 1
        return res
    return inner
