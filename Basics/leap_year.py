#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 18:45:35 2023

@author: andy
"""
x=int(input())

if (x%400==0 or (x%4==0 and x%100!=0)):
    print("leap year")


else:
    print("not leap year")