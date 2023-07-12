# c is the child of B
# B is the child of A and parent of c
# A is the parent of B

class A:
    # parent of class B
    def methodA(self):
        print("class A method")
    
class B(A):
    # 
    def methodB(self,r):

        print("class B method",r)

class C(B):
    def methodC(self):

        print("class C method")
        

obj=C()

# using class c we can use data of class B and Class A

# using class B we can use data of class A but not Class C

obj.methodA()
obj.methodB()
obj.methodC()