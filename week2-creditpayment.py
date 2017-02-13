# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:21:05 2016

"""

import math

annualInterestRate = 0.2
balance = 320000

MIR = annualInterestRate/12.0
MinPay = balance/12.0
MaxPay = (balance*math.pow(1+MIR, 12))/12
OneYBall = balance
cent = 0.1

while OneYBall > 0 or OneYBall < -0.1:
    OneYBall = balance
    MidPay = (MinPay + MaxPay)/2.0
    i = 0
    while i < 12:
        MUB = OneYBall - MidPay
        OneYBall = MUB + MIR*MUB
        i += 1
    if OneYBall > 0:
        MinPay = MidPay
    else:
        MaxPay = MidPay    

print("Lowest Payment:", MinPay)
