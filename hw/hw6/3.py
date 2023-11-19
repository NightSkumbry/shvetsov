p = 7
while True:
    for x in range(p):
        for y in range(p):
            a = [5,x,1,6]
            b = [x,x,x,5]
            c = [1,1,5,y,y]
            r1 = 0
            r2 = 0
            r3 = 0
            for i, e in enumerate(a[::-1]):
                r1 += e * p**i
            for i, e in enumerate(b[::-1]):
                r2 += e * p**i
            for i, e in enumerate(c[::-1]):
                r3 += e * p**i
            if r1 + r2 == r3:
                l = [y, x, y]
                ans = 0
                for i, e in enumerate(a[::-1]):
                    ans += e * p**i
                print(ans)
                import sys
                sys.exit()
    p+=1