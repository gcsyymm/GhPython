a = list(x.Paths) 
#a = path index
s = int(s % len(a)) 
#s = shift
b = a[s:] + a[:s] if w else a[s:] 
#b = shifted path, w = wrap boolean