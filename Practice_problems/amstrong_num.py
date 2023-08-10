def amstrong(n,k):
    if n!=0:
        return ((n%10)**k)+amstrong(n//10,k)
    else:
        return 0

a=int(input())
k=len(str(a))
if a==amstrong(a,k):print(a,"is an amstrong number")
else: print(a,"is not an amstrong number")