sho = min(x.BranchCount,y.BranchCount)
if x.BranchCount > y.BranchCount:
    for i in list(x.Paths)[sho:]:
        x.RemovePath(i)
elif x.BranchCount < y.BranchCount:
    for i in list(y.Paths)[sho:]:
        y.RemovePath(i)
