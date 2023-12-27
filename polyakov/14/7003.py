ans = 1

for x in range(12):
    for y in range(18):
        a = 0
        b = 0
        c = 0
        d = 0
        for i, e in enumerate([3,x,x,7,6]):
            a += e*12**i
        for i, e in enumerate([x,9,x,2]):
            b += e*14**i
        for i, e in enumerate([3,x,x,4,4]):
            c += e*15**i
        for i, e in enumerate([7,y,x,2]):
            d += e*18**i
        r = a + b + c - d
        if r > 0 and r%77 == 0:
            ans *= x*y
print(ans)
        






