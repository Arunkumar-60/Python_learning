# getter() accessor method
# setter() muttator method
# an example of encapsualted class 

class student:
    # setter method , name can be abythinf setid or hello doesnt matter
    def setID(self,id):
        self.__id=id

    # this method , reads and write data
    def getId(self):
        return self.__id
    
s1=student()
# calling class as obj 
s1.setID(20345986)
# passing argument to set values for id 

#printing using the getter method name getID (getID is user defined it can be anything)
print("id = ",s1.getId())

