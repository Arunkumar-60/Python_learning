# manupulation of data (public variables) from one class to another 
class A:
    def insert (self,id,salary):
        self.id=id
        self.salary=salary
    
    def display(self):
        print(self.id,self.salary)
    
class B:

    def data(Self,obj):
        obj.salary+=10000
        obj.display()

obj=A()
# claiing class in a obj 
obj1=B()
# calling class b in diff obj 
obj.insert(101,45000)
# passing arguments for class to assigning values 
obj.display()
# to print intial values       


obj1.data(obj)