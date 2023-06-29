if type(x) != list:
    raise Exception('wrong type for x')
def gcd(x,y):
    l = max(x,y)
    s = min(x,y)
    r = l % s
    while r != 0:
        l = s
        s = r
        r = l % s
    return s
def gcds(x):
    ans = gcd(x[0],x[1])
    for i in xrange(2,len(x)):
        ans = gcd(ans,x[i])
    return ans
print(gcds(x))