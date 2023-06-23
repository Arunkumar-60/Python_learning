#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:44:08 2023

@author: andy
"""

# swap two number using bitwise operator

x=int(input("x:"))
y=int(input("y:"))

z=x^y
x=z^x
y=z^y

print("x is ",x)
print("y is ",y)


#coverting numb to binary x
# binary=[]
# i=0

# def bintodec (a):
    
#     print(a%2,end="")
#     if a>1:
#         bintodec(a//2)

# bintodec(10)

# print(bintodec(10)[::-1])

#using AND and OR operators


#the covert binary to number
