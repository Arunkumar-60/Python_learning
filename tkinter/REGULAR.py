import re

p=re.compile('[a-e]')

print(p.findall("this is a test statement of for the findall predef function"))

from re import split

print(split('\W+','Words, words, Words'))

import re

print(re.split('\d+','ON 12th jan 2016'))

print(re.split('[a-f,1-3]+','ON 12th jan 2016'))

# read documentaion of regular expression on W#SCHOOLS


print(re.split('[a-f,1-3]+','ON 12th jan 2016',flags=re.IGNORECASE))

#sub function sunstitutes

print(re.sub("ub","~","subject has Uber booked already"))

print(re.sub("ub","~","subject has Uber booked already",flags=re.IGNORECASE))

print(re.sub("ub","~","subject has Uber booked already",flags=re.IGNORECASE, count=1))

#subn

print(re.subn("ub","~","subject has Uber booked already",flags=re.IGNORECASE))

t=re.subn("ub","~","subject has Uber booked already",flags=re.IGNORECASE)

print(t)

print(len(t))