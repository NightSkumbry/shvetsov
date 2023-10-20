def A():
    with open('./files/2691_b.txt') as f:
        a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[1:]))
        # print(a)
    b = []
    r = 0
    for ind, i in enumerate(a):
        h = list(sorted(i))
        b.append([h[2]-h[1], 0, ind])
        r += h[0] + h[1]
    b.sort(key=lambda x: x[0])
    while r % 9 == 0:
        r += b[0][0]
        b[0][1] += 1
        if b[0][1] == 1:
            h = list(sorted(a[b[0][2]]))
            b[0][0] = h[1]-h[0]
        elif b[0][1] >= 2:
            b.pop(0)
        if not b:
            print('aaaaaaaaa')
            break
        b.sort(key=lambda x: x[0])
    print(r)
    
A()