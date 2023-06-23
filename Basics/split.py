#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:16:52 2023

@author: andy
"""

x=90
y=98
sum=x+y
print("sum of",x ,"and",y,"is",sum)

# can also write is like below

print("sum of {} and {} is {}".format(x,y,sum))

# percentile %d is for integer %f for float %s for string 

print("sum of %d and %d is %d" %(x,y,sum))


# split function

s="one two three four five six seven"
#sllits acordingly with spaces and has been stored
s1=s.split()
print(s1)

s2=s.split("t")

print(s2)
# splits using characters t not by space

# split functioon can be used for mapping data into variables

# x1,x2,x3,x4= input("enter value").split(",")
# type inpu tseperated by comma like 12,23,34,45
# print(x1,x2,x3,x4)

s="@"
print(s.join("inspanner"))

#write a program indivials from 100 to 999

num=int(input("number between 100-999"))

print("sum = ",num//100+((num//10)%10)+num%10)

#reverse the number

print((num//100)+(((num//10)%10)*10)+((num%10)*100))
