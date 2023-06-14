j,k = 0, 0
a = ["{};{}".format(i,j) for j in range(len(x.Paths)) if x.PathExists(i,j)]
# a = selected paths with i line
# swap i,j for different selection
# more genal case
b = ["{};{};{}".format(i,j,k) for j in range(len(x.Paths)) for k in range(len(x.Paths)) if x.PathExists(i,j,k)]