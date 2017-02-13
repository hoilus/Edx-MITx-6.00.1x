# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:43:26 2016

@author: hoilus
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    num = int(us_num)
    for key in trans:
        if key == us_num:
            return print(trans[key])
    if num >= 11 and num <= 19:
        for key in trans:
            if key == us_num[1]:
                print(trans['10']+' '+trans[key])
    if num >= 20 and num <= 99:
        for key in trans:
            if key == us_num[0]:
                ch1 = trans[key]
            if key == us_num[1]:
                ch2 = trans[key]
        if num % 10 != 0:
            return print(ch1+' '+trans['10']+' '+ch2)
        else:
            return print(ch1+' '+trans['10'])
