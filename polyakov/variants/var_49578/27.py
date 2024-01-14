def A():
    with open('./polyakov/variants/var_49578/27-110a.txt') as f:
        a = [list(map(int, i.split())) for i in f.readlines()]
        k = a[0][1]
        a = a[1:]

    from functools import cache

    @cache
    def f(i, n, j):
        if i >= len(a):
            return n
        g = max(f(i+1, n+a[i][1], 0), f(i+1, n, j))
        if j < k:
            g = max(g, f(i+1, n+a[i][0], j+1))
        return g
    print(f(0, 0, 0))



def B():
    with open('./polyakov/variants/var_49578/27-110b.txt') as f:
        a = [list(map(int, i.split())) for i in f.readlines()]
        k = a[0][1]
        a = a[1:]
        
        b = [[0, k]]
        for i in a:
            br = []
            for r in b:
                br.append([r[0] + i[1], k])
                br.append([r[0], r[1]])
                if r[1]:
                    br.append([r[0] + i[0], r[1]-1])
            br.sort()
            br = br[::-1]
            b = [br[0]]
            for r in br[1:]:
                if r[1] > b[-1][1]:
                    b.append(r)
        
    print(b[0][0])
                
                

import timeit as t
print(t.timeit(A, number=1))
print(t.timeit(B, number=1))

