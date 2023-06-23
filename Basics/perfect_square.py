#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:36:54 2023

@author: andy
"""

a=int(input())
i=a
if (a==1):
    print("it's a perfect square")
elif(a==0):
    print(" its a perfect square")


while(a>0 and i>0):
    if(a/i==i):
        print("its perfect square")
        break
    elif(i==1):
        print("not a perfect square")
    i-=1

# wap to find a given number is perfect square or not
#wap to find if given number is a sunny number of not(FYI: numbe, 8 is sunny number)