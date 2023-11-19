for x in range(150):
    a = [5, 1, x, 2, 9]
    b = [x, 0, 2, 3]
    r = 0
    for i, e in enumerate(a[::-1]):
        r += e * 150**i
    for i, e in enumerate(b[::-1]):
        r += e * 150**i
    if r % 149 == 0:
        print(r//149)
    