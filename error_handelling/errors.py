dt=[12,2,22,3,4,12,3,44,'p']
try:
    sum=0
    for i in dt:
        sum=+1
    print(sum)
    print(dt[19])
except TypeError:
    print("can sum the character, its not possible")
except IndexError:
    print("out of bound index error")
finally:
    print("this is finally block")
    