# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1



for i in range(1,6):
    for j in range(1,6):
        print(min(i,j,6-i,6-j),end=" ")
    print()

