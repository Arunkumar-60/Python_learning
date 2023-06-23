#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:24:26 2023

@author: andy
"""

# (A+B)^n

# const is co-efficient of the polynomial 
# coeffiecent(Ncr) A**n-r B*r
# ncr=n!/(n-r)! r!
# n(n-1)(n-2)(n-3)/4*3*2*1=> nc4 //does this make sense?
# nc0 a^n b^0+ nc1 a^(n-1) b^1+
# concatination??
n=int(input())

coeff=1
# ncr=n(n-1)(n-2)/3*2*1



for i in range(0,n+1):
    coeff=1
    if (i==0 or i==n):
        coeff=1
    elif(i!=0 or i!=n):
        for i in range(1,i+1):
            coeff=(coeff*((n+1)-i)/i)
    print(str(int(coeff))+" * "+"(A^",n-i,")"+"*(B^",i,")"+"+",end="")
    
    
        