def A():
    with open('./some_files/var_49578/27-110a.txt') as f:
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
    with open('./some_files/var_49578/27-110a.txt') as f:
        a = [list(map(int, i.split())) for i in f.readlines()]
        k = a[0][1]
        a = a[1:]


import timeit as t
print(t.timeit(A, number=1))
