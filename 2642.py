with open('./files/26-k5.txt') as f:
    a = list(map(int, f.read().strip().split()[3:]))
    a.sort()
    k = 30
    m = 10
am = a[-m:]

print(am[0], int(sum(a[:k])/k))


