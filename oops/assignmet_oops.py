# WAP (create a class and get all possible distinct subsets from the set)

l=[]
u=int(input("enter number of numbers"))

for i in range(u):
    l.append(int(input("enter a number  :")))

k=set(int(i) for i in l)

j=[]

for x in k:
    j.append(int(x))
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

    