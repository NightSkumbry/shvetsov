for x in range(19):
    a = [9,8,x,7,9,6,4,1]
    b = [3,6,x,1,4]
    c = [7,3,x,4]
    r=0
    for i, e in enumerate(a[::-1]):
        r += e*19**i
    for i, e in enumerate(b[::-1]):
        r += e*19**i
    for i, e in enumerate(c[::-1]):
        r += e*19**i
    if r% 18 == 0:
        print(r//18)