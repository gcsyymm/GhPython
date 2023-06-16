j = k = int(0)
i = int(i)
for j in range(x.BranchCount):
    for k in range(x.BranchCount):
        if x.PathExists(i,j,k):
            print('{'+'{};{};{}'.format(i,j,k)+'}')
        else:
            break