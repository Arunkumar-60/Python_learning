# <!-- abstraction :
# data hiding

# abstract classes : 
# considered as blue print of the classes 
# it allowes users to create set of methods
# must be created implemetationn of those methods inside a child classes

# <nikitha> notes -->



# //////////////////////

# abc is module and ABC is class 

from abc import ABC ,  abstractmethod

class data(ABC):

    @abstractmethod
    def area(self,r):
        pass

class data1(data):
    def area (Self,r):
        print("area is ",3.14*r*r)
    
class data2(data):
    def area (Self,r):
        print("area 1 = ",r*r)


d1=data1()
d1.area(3)

d2=data2()
d2.area(4)

