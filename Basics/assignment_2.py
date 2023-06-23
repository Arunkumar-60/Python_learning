#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:14:16 2023

@author: andy
"""
n=int(input())
if(n>=0):
    if (n%2==1):
        print("wierd")
    elif(n%2==0 and 2<=n<=5):
        print("not wierd")
    elif(n%2==0 and 6<=n<=20):
        print("wierd")
    else:
        print("not wierd")