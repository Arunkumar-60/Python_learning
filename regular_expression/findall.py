import re
p=re.compile('\d')
print(p.findall("i went to institute at 11 am and retured back at 4 pm on 22 july 2023"))


p=re.compile('\d+')
print(p.findall("i went to institute at 11 am and retured back at 4 pm on 22 july 2023"))

p=re.compile('\w')
print(p.findall("i went to institute at 11 am and retured back at 4 pm on 22 july 2023"))

p=re.compile('\w+')
print(p.findall("i went to institute at 11 am and retured back at 4 pm on 22 july 2023"))

p=re.compile('\W')
print(p.findall("i went to institute @ 11 & retured back at 4pm on 22_july_2023"))

p=re.compile('ab*')
print(p.findall("abababababbabaababa"))