
for x in range(100000):
    a = 64**11 - 4**10 + 96 - x
    r = []
    while a:
        r.append(a%4)
        a //= 4
    if sum(r) == 71:
        print(x)
        break





