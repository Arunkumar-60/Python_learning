def div(f): #step 3 function runs
    def inner(a,b): #step 4 this runs and takes arguments from line 13
        if b<=0 or b>a: #step 5 checks for conditions
            print("unable to divide")
            return 1 #if setp 5 is true this reurns nothing
        return f(a,b) #or the inner fuction returns function f with two arguments a,b
    return inner #step 7 this reurns the whole function 

@div #2-> then this decorator
def divide(x,y): #takes and passes the a,b values as x,y and prints x/y from line 11
    print(x/y)

divide(34,12)
# 1->code starts here, gives argumnets


#similarly factorial using decoratos
#solve it 
def fact(f):
    def inner(n):
        if n<=0:
            print("cant find factorial")
            return 1
        return f(n)
    return inner()

@fact
def factorial(x):
    print(n)

factorial(3)