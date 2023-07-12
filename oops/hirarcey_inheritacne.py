# grand-> two sons -> two sons each or (1,2)

class A:
    def area(self,r):
        areaa=(22/7)*(r**2)
        print("Area is ",areaa)
    
class B(A):
    def area(self,l,b):
        ar=l*b
        print("area = ",ar)

bb1=B()
bb1.area(23,45)
print("2nd code")

# method in child class is given preferance so single arugment cant be passed(this is called method over riding only when methods have same name)
#  for example when tried to execute this , we get a error .  bb1.area(78)



#super is used to call the method of parent class 
class A:
    def area(self,r):
        areaa=(22/7)*(r**2)
        print("Area is ",areaa)
    
class B(A):
    def area(self,l,b):
        super().area(4.5)
        ar=l*b
        print("area = ",ar)

bb1=B()
bb1.area(23,45)
bb1.area(78,6)
