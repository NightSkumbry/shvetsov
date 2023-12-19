
def A():
    with open('./files/27-107a.txt') as f:
        a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[1:]))
    a.sort(key=lambda x: x[0])
    i = 0
    end = 0
    ans = 0
    b = sorted(a, key=lambda x: x[1])
    ie = 0
    while i < len(a):
        if a[i][0] <= end:
            i += 1
        else:
            while ie < len(b) and b[ie][0] <= end:
                ie += 1
            end = b[ie][1]
            i += 1
            ans += 1
    print(ans)


def B():
    with open('./files/27-107b.txt') as f:
        a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[1:]))
    a.sort(key=lambda x: x[0])
    i = 0
    end = 0
    ans = 0
    b = sorted(a, key=lambda x: x[1])
    ie = 0
    while i < len(a):
        if a[i][0] <= end:
            i += 1
        else:
            while ie < len(b) and b[ie][0] <= end:
                ie += 1
            end = b[ie][1]
            i += 1
            ans += 1
    print(ans)

import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))



