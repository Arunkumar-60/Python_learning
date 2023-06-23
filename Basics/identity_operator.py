#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 18:31:49 2023

@author: andy
"""

# identity operator is  is not

x1=90

y1=80

x2=90

print(x1 is x2)
print(x1 is y1)
print(x2 is not y1)
print(x2 is y1)

x2=90.45
y2=29.35

print(x2 is not y2)

x3=[1,2,3,4]
y3=[1,2,3,4]

print (x3 is y3)

x4=(1,2,3,4)
y4=(1,2,3,4)
print(x4 is y4)

# true cuz the tuple is immutable , cant be changes and both x4 and y4 are pointed to same memory location as python is oop language 