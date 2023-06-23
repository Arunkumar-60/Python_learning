#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:06:05 2023

@author: andy
"""

# covert 2 digit integer to binarynumber(10-99)
# using list,append and while loops


# a=int(input())
# binary=[]
# #27
# while(a!=0):
#     binary.append(a%2)
#     a=a//2

# k=len(binary)
# while k>0:
#     print(binary[k-1],end="")
#     k=k-1


#using strings , data types and slicing
# stingy but works

a=int(input())
s1=''

s1=s1+str(a%2)
a=a//2
s1=s1+str(a%2)
a=a//2
s1=s1+str(a%2)
a=a//2
s1=s1+str(a%2)
a=a//2
s1=s1+str(a%2)
a=a//2
s1=s1+str(a%2)
a=a//2
s1=s1+str(a%2)
a=a//2


print(int(s1[::-1]))