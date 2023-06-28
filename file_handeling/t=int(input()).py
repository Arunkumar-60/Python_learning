t=int(input())
for _ in range(t):
    c=0
    k=int(input())
    l=[]
    for i in input().split():
        l.append(int(i))
    
    for j in range(len(l)):
        if 60>=l[j]>=10:
            c=c+1
    print(c)