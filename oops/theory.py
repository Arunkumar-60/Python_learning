# object oriented programming

# 6 features:
# pobject
# class
# enheritannce
# inheritance
# polymorphism
# abstraction

# <---***************--->

# object :object is a real wotld entity
# collection of attributes
# attubutes are also ncalled as properties

# id:name of object 
# state: data / information
# behaviour: functionality of the object

# object is also called as instance of class

# <---***************--->

# class: logical entity
# class is a collection of different and similar type of objects

# class is  a blueprint of the program 

# without a object a class is nothing
# data inside  a class is called object 

# a class consists of methods
# <----similar to the fuction defined int side a py code---->
# constructer , destructor, medthods , fields are data members of the class 
# class <name>:

# <name> can be captilized , loweercase or uppercase

# for example:
class Hello:
    empname="harish"

    def display(self):
        print("hello world")

obj=Hello()
# and the name is case sensitive
# <---storing thr class hello in a object --->
obj.display()
# <---display is  amethod--->
print("value = ",obj.empname)
# <---***************--->

# types of methods

# static method : 

    # by default the method u define in a class 

class data:
    @staticmethod

    def calculate():
        print ("thsi sis static method")
data.calculate()

class Data:
    @staticmethod
    def nikitha(n):
        print("this is static method for power", n**n)
Data.nikitha(5.6)
# class method
# when class method is defined
# a non-predifined argument is to be passes while defining the class :called decorator

class style:
    @classmethod
    def calcify(cls,n,n1):
        # here cls is a decorator
        print("this is class method", n*n1)

style.calcify(5.6,67)

# instance method : object is the instance of a class
class stylish:
    def clcificationing(self,n,n1):
    # here self is a decorator it can be anything its just a non-predefined argument
        print("this is class method",n*n1)
    
dat1=stylish()
dat1.clcificationing(12,2)
# python prgram to append delete display the elemets of a list using class



# n=int(input("enter number of elements in list"))
# l=[]
# for i in range(n):
#     print("enter the ",i+1,"th value: ")
#     l.append(input())
s="python prgram to append delete display the elemets of a list using class"
print(s.split())
l=[1,223,23,2]

class lists:
    def display():
        print(l)

    def append(ind,val):
        stri=""
        for i in range(ind):
            stri=stri+str(l[i])+" "
        stri=stri+str(val)+" "
        for i in range(ind,len(l)):
            stri=stri+str(l[i])+" "
        
    def remove(ind):
        stri=""
        for i in range(len(l)):
            if l[i] != ind:
                stri=stri+str(l[i])+" "
            else:
                stri=stri+""
        print(stri.split())


lists.display()
lists.append(0,2)
lists.remove(1)

