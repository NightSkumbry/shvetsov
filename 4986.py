import timeit
def f():
    p = [True] * 10**8
    print(1)
    p *= 5
    print(2)
    p *= 2
    print(len(p))
    p[0] = False
    p[1] = False
    for i in range(2, int(10**4.5)+2):
        if p[i]:
            for k in range(i**2, 10**9+1, i):
                p[k] = False
print(timeit.timeit(f, number=1))