# mapping_numbers
x,y,z=[int(i) for i in input().split()]

print(x,y,z)

# more examples

value = [lambda a=x:a*10 for x in range(1,5)]
print(type(value))

for i in value:
    print(i())