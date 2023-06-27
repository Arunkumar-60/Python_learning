# importing library
import json

# writing raw json data 
student={
    "name":"arun",
    "age":24,
    "qualification":"B.tech"
}

# creating student.json as writable file with <object pl> and dumping the data
with open ("student.json","w") as pl:
    json.dump(student,pl)


#revserse of upper code

#scraping data from json file 
#this can be used for scrapig (extracting) data from the webpages

#opening file as readable in object fl
# loading as json and printing

with open("student.json","r") as fl:
    d=json.load(fl)
    print(d)