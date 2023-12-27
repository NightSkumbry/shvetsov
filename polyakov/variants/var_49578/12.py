
f = lambda x, k: x.find(str(k)) != -1
r = lambda x, k, l: x.replace(str(k), str(l), 1)

for n in range(101, 100000):
    s = '5'*n
    while f(s, 555) or f(s, 11) or f(s, 2):
        if f(s, 555):
            s = r(s, 555, 1)
        if f(s, 11):
            s = r(s, 11, 25)
        if f(s, 2):
            s = r(s, 2, 5)
    if s == '15':
        print(n)
        break





