#wap to find the largest word in a string and print it

x=str(input("enter the sentence :"))


def find_largest_word(a):
    maximum_word=""
    b=a.split()
    max_length=0
    for i in b:
        length=0
        for j in i:
            length=length+1
        if length>=max_length:
            max_length=length
            maximum_word=str(i)
    print(maximum_word)


find_largest_word(x)