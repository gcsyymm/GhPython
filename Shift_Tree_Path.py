s = 1
w = True
p = list(x.Paths)
s = int(s % len(p))
y = p[s:] + p[:s] if w else p[s:]
for _ in range(len(y)):
    print y[_]