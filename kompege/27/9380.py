from itertools import accumulate
import math


def get_sum(pr, s, e):
    if e > s:
        return pr[e]-pr[s]
    else:
        return pr[-1]-pr[s] + pr[e]


def A():
    with open('./files/27A_9380.txt') as f:
        a = f.read().strip().split('\n')
        k = int(a[0].split()[1])
        a = list(map(lambda x: math.ceil(int(x)/k), a[1:]))
    ans = 0
    for i in range(len(a)):
        i1 = 0
        i2 = 0
        k1 = 0
        k2 = 0
        for j in range(len(a)-1):
            if k1 > k2:
                i2 += 1
                k2 += i2*a[(i-i2)%len(a)]
            else:
                i1 += 1
                k1 += i1*a[(i+i1)%len(a)]
        if k1 == k2:
            ans = i
    print(ans)




def B():
    with open('./files/27B_9380.txt') as f:
        a = f.read().strip().split('\n')
        k = int(a[0].split()[1])
        a = list(map(lambda x: math.ceil(int(x)/k), a[1:]))
    i2 = 0
    i1 = 0
    k1 = 0
    k2 = 0
    ans = 0
    for j in range(len(a)-1):
        if k1 > k2:
            i2 += 1
            k2 += i2*a[(-i2)%len(a)]
        else:
            i1 += 1
            k1 += i1*a[(i1)%len(a)]
    pr = [0] + list(accumulate(a))
    for i in range(1, len(a)):
        k1 -= get_sum(pr, i, (i+i1)%len(a))
        k2 += get_sum(pr, (i-i2-1)%len(a), i)
        i1 -= 1
        i2 += 1
        while k2 > k1:
            k2 -= i2*a[(i-i2)%len(a)]
            i2 -= 1
            i1 += 1
            k1 += i1*a[(i+i1)%len(a)]
        if k1 == k2:
            ans = i
    print(ans)

    
    


import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))

