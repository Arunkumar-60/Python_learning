# importing a library
import pickle

# creating a variable
str="hello data binding , object oriented programing with python"

# creating a object named f1
# creating a file nikki.bin in writeable binary format

f1=open("nikki.bin","wb")

# steralizing the data
pickle.dump(str,f1)


f1.close()

# now desterlizing the data 
# reading as binary 
f1=open("nikki.bin","rb")

# using pickle to de sterlize the binary data to normal data 
lst=pickle.load(f1)

# reading the data as list of string
print(list(lst))

f1.close()