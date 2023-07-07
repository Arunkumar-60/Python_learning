# inheritance 

# aquiring properties from one class to another is called inheritance.
# IS-A relationship (parent-child)

#base class - parent class 
#sub class - child class

class A:
    def methodA(self):
        print("a method")
    
class B(A):
    def methodB(Self):
        print("method B")
    
ad=B()
ad.methodA()
ad.methodB()

ob=A()
ob.methodA()
