#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:02:19 2023

@author: andy
"""

# a or A is Ada
# b or B is basic
# c or C is cobol
# D or d is fortran
# p or P is Pascal
# V or v is visual C++

x=input("enter the language of install :")

if (x == "A" or x == "a"):
    print("Ada")

elif (x == "B" or x == "b"):
    print("Basic")
    
elif (x == "C" or x == "c"):
    print("Cobol")

elif (x == "D" or x == "d"):
    print("Fortran")

elif (x == "p" or x == "P"):
    print("Pascal")

elif (x == "P" or x == "P"):
    print("Visual C++")
else:
    print("wrong input")