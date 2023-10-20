for x in range(111):
    r = 0
    a = [x, 3, 2, 1]
    b = [1, 7, x, 4]
    for i, e in enumerate(a[::-1]):
        r += e*111**i
    for i, e in enumerate(b[::-1]):
        r += e*211**i
    if r % 111 == 0:
        print(r//111)