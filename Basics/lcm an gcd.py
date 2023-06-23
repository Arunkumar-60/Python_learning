#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 03:20:13 2023

@author: andy
"""

def lcm(x,y):
    for j in range((max(x,y)),((x*y)+1)):
        if(j%x==0 and j%y==0):
            return j
            break
            

a,b=map(int, input().split())
print(((a*b)//lcm(a,b)),lcm(a,b))