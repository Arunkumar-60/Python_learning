def dup(sentance):
    l=[]
    k=sentance.split()
    for i in range(len(k)):
        for j in range(len(k)):
            if k[i]==k[j] and i!=j:
                l.append(k[i])
    return list(set(l))


print(dup(input()))

