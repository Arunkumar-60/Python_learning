class data:
    def __init__(self,v):
        self.v=v
    
    def display(self):
        print("value is ",self.v)
    
ad=data(12)
ad.display()
print(id(ad))

# ///////////

class info:
    # constructor starus with __init__ 
    def __init__(self,id,name):
        self.id=id
        self.name=name
    # destructor starts witjh __del__ 
    def __del__(self):
        print("this is a destructor")

    def display(self):
        print(self.id,self.name)

ad.display()

ad=info(101,"hello")
ad.display()
print(id(ad))
del ad
