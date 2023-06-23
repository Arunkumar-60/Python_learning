# returning_values

def data(n):
    sum=0
    while n!=0:
        sum=sum+n
        n=n-1
    return sum

print(data(10))

# data (10) will be executed and functions returns thw value to the python named or unnamed variables 

def mul_data(n,n1):
    a=n+n1
    b=n-n1
    return a,b


print(type(mul_data(1,3)))

x,y=mul_data(1,3)

print(type(x))

print("x is ",x)

print("y is",y)

def rec_call(n):
    if n>=0:
        print(n,end=" ")
        return rec_call(n-1)
    
print(rec_call(5))
rec_call(5)


