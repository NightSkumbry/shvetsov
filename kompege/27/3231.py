from itertools import accumulate

def v(n, g, a):
    ans = 0
    for i in range(g+1):
        ans += i * a[(i+n)%len(a)]
        ans += i * a[(-i+n)%len(a)]
    ans -= g * a[(g+n)%len(a)] * (len(a)%2 == 0)
    return ans


def get_sum(pr, s, e):
    if e > s:
        return pr[e]-pr[s]
    return pr[-1]-pr[s] + pr[e]


def A():
    with open('./files/27-A_3231.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    g = len(a)//2
    a1 = [v(i, g, a) for i in range(len(a))]
    

    print(a1.index(min(a1))+1)


def B1():
    with open('./files/27-B_3231.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    g = len(a)//2
    a3 = [2*a[i]-a[(i+g)%len(a)]-a[(i-g)%len(a)] for i in range(len(a))]
    a1 = [v(0, g, a), v(1, g, a)]
    a2 = [a1[1]-a1[0]]
    for i in a3[1:]:
        a2.append(a2[-1]+i)
    for i in a2[1:-1]:
        a1.append(a1[-1]+i)

    print(a1.index(min(a1))+1)


def B2():
    with open('./files/27-B_3231.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    g = len(a)//2
    ans = 0
    p = h = v(0, g, a)
    pr = [0] + list(accumulate(a))
    for i in range(1, len(a)):
        h += get_sum(pr, (i-g)%len(a), i) - get_sum(pr, i, (i+g)%len(a))
        if h < p:
            p = h
            ans = i
    print(ans+1)


import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B1, number=1))
print(timeit.timeit(B2, number=1))

