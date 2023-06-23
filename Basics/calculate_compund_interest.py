#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:06:38 2023

@author: andy
"""

# wap to czlculate CI

principle=int(input("enter principle amount : "))

rate=int(input("enter rate of interest :"))

n=int(input("enter number of times interest is compunded per year :"))
# number of times intereet compunded per year

t=int(input("enter time in years : "))
# time in years


ci=((principle*((1+(rate/n))**(n*t)))-principle)

print("compund interest is :",ci)
