for x in range(67):
    a = [3, x, 2, 1]
    b = [1, 7, x, 4]
    r = 0
    for i, e in enumerate(a[::-1]):
        r += e * 81**i
    for i, e in enumerate(b[::-1]):
        r += e * 67**i
    if r % 35 == 0:
        print(r//35)