# *
# **
# ***
# ****
# *****
# executing this pattern
n=int(input("enter number of line sof stars u wanna print : "))
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()