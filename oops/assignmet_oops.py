# WAP (create a class and get all possible distinct subsets from the set)

# Python Program to Print
# all subsets of given size of a set
 
import itertools
# def findsubsets(s, n):
def findsubsets(s, n):
    return [set(i) for i in itertools.combinations(s, n)]
     
# Driver Code
s = {1, 2, 3, 4}

l=[]
for z in range(len(s)):
    l.append((findsubsets(s, z)))

for i in range(len(l)):
    print(l[i],end="")

# //set of numbers given is in the list j 


    
# wap to create a class to extract numbers from the text file:

class DIS():
    def disply(self,z):
        print(z,end=" ")



class NUM(DIS):
    
    def numb(self,cr):
        if (cr.isnumeric()):
            super().disply(cr)

class Word(NUM):
    def word(self,word):
        for i in word:
            super().numb(i)

class numberextract(Word):

    def splitting(self,doctor):
        for j in doctor.split():
            super().word(str(j))
        

obj=numberextract()

f1=open ("harish_1.py","w")
f1.write("# h0el2lo world2 this i3s har1ish")
f1.close()

with open("harish_1.py","r") as file:
    data_of_file=file.read()



obj.splitting(data_of_file)

    