#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:06:32 2023

@author: andy
"""

# wap to find the area of triagles when sides are given

a=int(input("enter a side length"))
b=int(input("enter a side length"))
c=int(input("enter a side length"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print("area of the triangle is : ",area)