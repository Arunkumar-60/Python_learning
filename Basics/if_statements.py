#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 18:18:24 2023

@author: andy
"""
"""
simple if: executes bloack of tatement associated with if block
when if blocjk condition is true if block staement
will execute else if block will be executed

if (condition):
    block of statement
    
outer block statement
here : is a indentation mark

"""

n=int(input("enter the number"))

if n>100:
    print("this is if block")
    n=n+1
    print("value = ",n)

else:
    print("this is else block of statement")
    n-=1
    print("value =",n)
print("this is the outer if block statement")


if n>0:
    print("+ve number")
elif n<0:
    print("-ve number")
else:
    print("zero")

print("this is outer if block")
