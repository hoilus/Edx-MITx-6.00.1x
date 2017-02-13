# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:46:12 2016

"""

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new
