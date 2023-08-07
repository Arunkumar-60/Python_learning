class A:
    # parent class A 
    def methodA(self):
        print("class A method")
    
class B:
    # parent class B 
    def methodB(self):
        print("class B method")

class C(A,B):
    def methodC(self):
        print("class C method")

obj=C()
# we can call any call as the class c has inheritated the properties of A and B (multi inheritance)
obj.methodA()
obj.methodB()
obj.methodC()

# for ecample 
# MRO-method resolving order -> first parent class is called or given preferance (first caomes first server)

# here

class A:
    # parent class A 
    def methodA(self):
        print("class A method")
    
class B:
    # parent class B 
    def methodA(self):
        print("class B method")

class C(A,B):
    def methodC(self):
        print("class C method")

obj=C()
# we can call any call as the class c has inheritated the properties
print(2)
obj.methodA()
print(1)
# here upon callinf ther class only first parent with that specified method is called
obj.methodC()
obj.methodA()
