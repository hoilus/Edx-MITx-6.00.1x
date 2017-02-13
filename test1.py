# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("I like 6.00.1x!")

s = 'zyxwvutsrqponmlkjihgfedcba'

count = 0

test = s[0]
best = ''

for i in range(1,len(s)):
    if len(test) > len(best):
        best = test
    if s[i] >= s[i-1]:
        test = test + s[i]
    else:
        test = s[i]
    if len(test) > len(best):
        best = test
        
print("Longest substring in alphabetical order is: " + best)
            