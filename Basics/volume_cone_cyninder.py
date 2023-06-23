#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:06:27 2023

@author: andy
"""

# wap to calculate volume of cone and cylinder

h=int(input("enter height of cone: "))
r=int(input("enter the radius :"))

hc=int(input("enter height of cone: "))
rc=int(input("enter the radius :"))

#vloume of cone

v=(1/3)*(22/7)*(r)*(r)*(h)

print("volume of the cone: ",v)
#volume of cylinder

vc=(22/7)*(rc)*(rc)*(hc)
print("volume of the cylinder",vc)