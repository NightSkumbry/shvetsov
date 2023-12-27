
for x in range(1, 100000):
    a = 64**12 - 8**14 + x
    r = []
    while a:
        r.append(a%8)
        a //= 8
    if r.count(7) == 12 and r.count(1) == 1:
        print(x)
        break
