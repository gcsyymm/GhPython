j = int(0)
i = int(i)
y = list()
for j in range(len(x.Paths)):
    if x.PathExists(i,j):
        y.append("{"+"{};{}".format(i,j)+"}")
    else:
        break
for _ in range(len(y)):
    print(y[_])