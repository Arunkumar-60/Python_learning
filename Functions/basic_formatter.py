# basic_formatter, potional required argument
def student(id,name):
    print("id = {} and name = {}".format(id,name))

i=101
n="arun"
student(i,n)


#default argument
def student_new(id,name,college="nit_ap"):
    print("id = {} and name = {} and college = {}".\
        # here \ is the just line braeak for code
          format(id,name,college))

i=101
n="arun"
student_new(i,n)
student_new(i,n,"New Jersey")
student_new(201,"jay","other")

#key word argument

def student_key(id,name):
    print("id = {} and name = {}".format(id,name))

i=101
n="arun"
student_key(name="arun",id=120)
# order doesnt matter when u name the attribules while calling the function

#function with variable argumnet length
def student_var(*n):
    print(n)

student_var(1,2,3,4,5)
student_var()
student_var(1,2)

#function with variable argument with keywords

def student_keyvar(**n):
    print(n)

student_keyvar(id="101",name="Arun",college="nit")
