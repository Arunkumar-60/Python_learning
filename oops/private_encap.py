class A:
    def __hello(self):
        print("this is private data")
    
    def show(self):
        self.__hello()
        print("thi is a public method")
    
obj=A()
obj._A__hello()
print()
obj.show()

# protected class 
class A:
    def __hello(self):
        print("this is potected data")
    
    def show(self):
        self.__hello()
        print("thi is a public method")
    
obj=A()
obj._A__hello()
print()
obj.show()