#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 14:10:03 2023

@author: andy
"""

a=int(input())
i=a
if (a==0):
    print("it's a sunny number")
elif(a==-1):
    print(" its a sunny number")
while(a>-2 and i>1):
    if(((a+1)/i)==i):
        print("its a sunny number")
        break
    elif(i==2):
        print("not a sunny number")
    i=i-1
    
    
    # or method 2
    

# a=(int(input()))+1
# i=a
# if (a==0):
#     print("it's a sunny number")
# elif(a==-1):
#     print(" its a sunny number")


# while(a>0 and i>0):
#     if(a/i==i):
#         print("its sunny number")
#         break
#     elif(i==1):
#         print("not a sunny number")
#     i-=1
