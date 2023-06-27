# file handeling:
#     how to manipulate data 
#     work with the Files

# binamry File    
# text file

# open modes : r : read w : write a :append r+ w+ a+
# read write read() write()
# close close()

# writing inside a file
#also overwrites the data inside the file

f1=open ("harish.py","w")
f1.write("# hello world this is harish")
print("file created")
f1.close()

#reading the text in the file
with open("harish.py","r") as file:
    tr=file.read()
    print(tr)

    file.close()


#wap to copy data from one file to another
#here f2 is object name

f2=open("arun.py","w")
f2.write("""#  just testing i fi can copy data from one file to another
# need multiple lines
# to test the code
# if i can count no of line
""")
f2.close()

with open ("arun.py","r") as file:
    temp=file.read()
    file.close()

f3=open("harish.py","w")
f3.write(temp)
f3.close()

# cound no of blank spaces , lines and characters

with open("harish.py","r") as file:
    string=file.read()
    file.close()

print("no of chars is :",len(string))
#split gives 3 variable if it ahse 2 space by minusing one ur just minusing the only extra char for every line
#if there are multiple line u cant just addd a -1 and assuem u get right count of spaces
print(len(string.split())-1)
nos=0
noc=0
nol=1
for i in string:
    noc+=1
    if i==" ":
        nos=nos+1

    if i=="\n":
        nol+=1
print(noc)
print(nos)
print(nol)


#wap to merge data of twofile
#opening files as readable f1 and f2 and storing in a variable 
f1=open("harish.py","r")
temp1=f1.read()
f2=open("arun.py","r")
temp2=f2.read()
f1.close()
f2.close()
f4=open("merge.py","w")
f4.write(temp1+temp2)

f5=open("merge.py","r")
temp3=f5.read()
#closing thsing thefile reading objects 
f3.close()
f4.close()
f5.close()