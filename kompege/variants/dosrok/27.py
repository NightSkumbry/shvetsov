from math import ceil
from itertools import accumulate

def F(file):
    with open(f'./kompege/variants/dosrok/27{file}.txt') as f:
        N, K = map(int, f.readline().split())
        a = [list(map(int, i.split())) for i in f]
    k = [0]*K
    for i in a:
        k[i[0]-1] = ceil(i[1]/11)
    k*=3
    b = [0] + list(accumulate(k))
    p = K
    l1 = (K-1)//2
    l2 = K-1-l1
    s = ans = sum([k[p-i]*i for i in range(1, l1+1)]) + sum([k[p+i]*i for i in range(1, l2+1)])
    while p < 2*K:
        p += 1
        s += (b[p]-b[p-l1]) - (b[p+l2]-b[p]) + (k[p+l2]*(K%2==0))
        if k[p]:
            ans = min(ans, s)
    print(ans)
    
    
F('A')
F('B')















