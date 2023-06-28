n=int(input("enter the value"))
try:
    if n<20:
        raise ValueError("lessthan 20 not allowes")
    else:
        print(n)
except IndexError:
    print("error")

# nex code with diff error handelling 
n=int(input("enter the value"))
try:
    if n<20:
        raise ValueError("lessthan 20 not allowes")
    else:
        print(n)
except ValueError:
    print("error")
