def file_a():
    with open('./files/27_A_10108.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]
    
    ans = -10**10
    for i in range(0, len(a) - 2*k):
        for j in range(i+k, len(a) - k):
            for y in range(j+k, len(a)):
                sm = a[i] + a[j] + a[y]
                if sm > ans:
                    ans = sm
                    # print(i, j, y)
    print(ans)


# file_a()


def file_b():
    with open('./files/27_B_10108.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]
        ar = a[::-1]
    b = a[:k]
    b1 = a[:k]
    mi = k*2-1
    while mi+1 < len(a):
        m = max(a[mi+1:])
        mi = len(a) - 1 - ar.index(m)
        for ind, i in enumerate(a[len(b):mi-k+1], len(b)):
            b.append(i+m)
            b1.append([mi, ind])
    c = []
    br = b[::-1]
    a1 = []
    mi = k-1
    while mi+1 < len(b):
        m = max(b[mi+1:])
        mi = len(b) - 1 - br.index(m)
        for ind, i in enumerate(a[len(c):mi-k+1], len(c)):
            c.append(i+m)
            a1.append(b1[mi]+[ind])
    n = a1[c.index(max(c))]
    print(max(c), n, [a[i] for i in n], sum([a[i] for i in n]))
        
        
            

file_b()