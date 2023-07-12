# decorators :
#     decorators are the kind of functions which changes the behaviour of the function or a class. 

#     it allows us to wrap the another function in order to extend the behaviour of the wraped function.
#     it modifies data without permanently modifying it 

# /////////
#     properties while creating decorators:
#     1)treating functions as object 

def hello(text):
    return text.lower()

print(hello("python"))

v1=hello

print(v1("hello there"))

#   2)passing function as an argumnet
print("\n")

def hello(txt):
     return txt.upper()

def bye(txt):
    return txt.lower()

def welcome(f):
    dt=f("hello World This is ARUN")
    print(dt)

# when hello is a function name it is passed as argumnet when its done f will be hello
welcome(hello)
welcome(bye)

#   3) returning function from an another function
print()

def outer(x):
    def inner(y):
        return x*y
    return inner

dt=outer(10)
print(dt(76))


# next day - 11 july 
print("\n 11-july \n")

def hello(ar):
    def inner():
        print("this is one data")
        ar()
    return inner

@hello
def data():
    print("this is second data")

data()