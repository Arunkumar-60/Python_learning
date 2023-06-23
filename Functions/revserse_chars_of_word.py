# reverse char of a word in the sentance and replace the o's with a's
a=str(input())
# u have to check for every char in the input string if it is "o"
b=a.split()

def replace_o(y):
    for i in y:
        if i=="o":
            print("a",end="")
        else:
            print(i,end="")

def reverse(x):
    replace_o(x[::-1])
    print(end=" ")

for j in b:
    reverse(j)