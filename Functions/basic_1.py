def data(n):
    while n!=0:
        print(n)
        n=n-1

data(10)
data(5)
# data(5.5) u can give decimal value but that will be a infinite loop as the n value changes from 
# 5.5 -> 4.5 -> 3.5 -> 2.5 -> 1.5 -> 0.5 -> -0.5 -> -1.5 -> and so...on
# i will print negitive infitely

