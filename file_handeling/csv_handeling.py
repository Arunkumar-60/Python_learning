# importing the csv library 
import csv

# creating file as writable
f1=open("data1.csv","w")

#writing a list for the hearing attribute names
fn=["name","branch","city","marks"]


#def a varioable to hold the feildname from the variable 
# dictwrite is a prefefined function 
wr=csv.DictWriter(f1,fieldnames=fn)

# writes the fild anems as key 

wr.writeheader()
# writeing rows using the key attributes so that we can assign values to the respective attribute
wr.writerow({"name":"arun","branch":"cse","city":"hyd","marks":"900"})
wr.writerow({"name":"nikki","branch":"cse","city":"hyd","marks":"1000"})

f1.close()

# !@#$%^&*() next program

# printing the csv as file  
with open("data1.csv") as file:
    dt=csv.reader(file,delimiter=",")

    for i in dt:
        print(i)
