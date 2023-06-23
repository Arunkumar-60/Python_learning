#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:42:22 2023

@author: andy
"""

#wap to read mobile number as word of string and covert that into numeraic number
#i/o -> string = "nine eight six four" o/p -> string="9864"


word_len=0

a=str(input("Number In Words:"))

words=a.split()

for x in (a.split()):
    word_len=(word_len+1)


b="one onE oNe oNE One OnE ONe ONE"
c="two twO tWo tWO Two TwO TWo TWO"
d="three threE thrEe thrEE thRee thReE thREe thREE tHree tHreE tHrEe tHrEE tHRee tHReE tHREe tHREE Three ThreE ThrEe ThrEE ThRee ThReE ThREe ThREE THree THreE THrEe THrEE THRee THReE THREe THREE"
e="four fouR foUr foUR fOur fOuR fOUr fOUR Four FouR FoUr FoUR FOur FOuR FOUr FOUR"
f="five fivE fiVe fiVE fIve fIvE fIVe fIVE Five FivE FiVe FiVE FIve FIvE FIVe FIVE"
g="six siX sIx sIX Six SiX SIx SIX"
h="seven seveN sevEn sevEN seVen seVeN seVEn seVEN sEven sEveN sEvEn sEvEN sEVen sEVeN sEVEn sEVEN Seven SeveN SevEn SevEN SeVen SeVeN SeVEn SeVEN SEven SEveN SEvEn SEvEN SEVen SEVeN SEVEn SEVEN"
i="eight eighT eigHt eigHT eiGht eiGhT eiGHt eiGHT eIght eIghT eIgHt eIgHT eIGht eIGhT eIGHt eIGHT Eight EighT EigHt EigHT EiGht EiGhT EiGHt EiGHT EIght EIghT EIgHt EIgHT EIGht EIGhT EIGHt EIGHT"
j="nine ninE niNe niNE nIne nInE nINe nINE Nine NinE NiNe NiNE NIne NInE NINe NINE"
k="zero zerO zeRo zeRO zEro zErO zERo zERO Zero ZerO ZeRo ZeRO ZEro ZErO ZERo ZERO"

one_word=b.split()
two_word=c.split()
three_word=d.split()
four_word=e.split()
five_word=f.split()
six_word=g.split()
seven_word=h.split()
eight_word=i.split()
nine_word=j.split()
zero_word=k.split()
num_str=""

for i in range(word_len):
    if words[i] in one_word:
        num_str=num_str+str(1)
        
    elif words[i] in two_word:
        num_str=num_str+str(2)
        
    elif words[i] in two_word:
        num_str=num_str+str(2)
        
    elif words[i] in three_word:
        num_str=num_str+str(3)
    
    elif words[i] in four_word:
        num_str=num_str+str(4)
    
    elif words[i] in five_word:
        num_str=num_str+str(5)
    
    elif words[i] in six_word:
        num_str=num_str+str(6)
        
    elif words[i] in seven_word:
        num_str=num_str+str(7)
    
    elif words[i] in eight_word:
        num_str=num_str+str(8)
    
    elif words[i] in nine_word:
        num_str=num_str+str(9)
    
    elif words[i] in zero_word:
        num_str=num_str+str(0)

print(str(num_str))