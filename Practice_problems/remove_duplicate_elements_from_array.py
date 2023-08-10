#This page shows you how to use LISTS as ARRAYS, 
#however, to work with arrays in Python you will have to import a library, 
#like the NumPy library.
'''
a=np.array([1,2,3,4,2,3,4,2,1,4,6])
b=np.unique(a)
print(b)
'''

def itr(z):
    for i in z:
        if z.count(i)>1:
            z.remove(i)
    return z




my_array=['arun','pooja','shiva','arun','nikitha']

print(itr(my_array))

print(list(set(my_array)))


