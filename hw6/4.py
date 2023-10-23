for x in range(37):
    a = [int('m', 36),int('f', 36),x,7,2]
    b = [int('t', 36),x,7,int('y', 36),2]
    r1 = 0
    r2 = 0
    for i, e in enumerate(a[::-1]):
        r1 += e * 37**i
    for i, e in enumerate(b[::-1]):
        r2 += e * 37**i
    if (r1+r2) % 536 == 0:
        print((r1 + r2)//536)