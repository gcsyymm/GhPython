j = int(0)
i = int(i)
y = list()
for j in range(len(x.Paths)):
    if x.PathExists(i,j):
        print("{"+"{};{}".format(i,j)+"}")
    else:
        break
