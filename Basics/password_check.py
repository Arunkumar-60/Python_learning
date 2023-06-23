#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:39:25 2023

@author: andy
"""

# #wap in python to read string as password
#  password must ne 8 characters long
#  atleast on 1 number
#  first character must be uppercase
#  if all above conditions are satisfied then print msg:
#      "password is valid"
#  else:
#      print("password id not valid")
     
password_len=0

a=str(input("password :"))

for x in a:
    password_len=(password_len+1)
    

cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number_str="0123456789"
num=0

if (password_len>=8):
    for j in range(0,1):
        if (a[0] in cap):
            for i in range(0,password_len):
                if (a[i] in number_str):
                    num=1
            if (num==1):
                print("valid password")
            elif (num==0):
                print("password must contain number")
        else:
            print("password must start with capital letter")
else:
    print("paswword lemngth should be atleast 8 characters long")