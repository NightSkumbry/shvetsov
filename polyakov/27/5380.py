from itertools import accumulate
from math import ceil

def F(file):
    with open(f'./files/27-123{file}.txt') as f:
        N, K, V = map(int, f.readline().split())
        a = [list(map(int, i.split())) for i in f]
    m = (K-1)//2
    isch = (K-1)%2
    d = [0]*K
    for i in a:
        d[i[0]-1] = ceil(i[1]/V)
    d*=3
    
    b = [0] + list(accumulate(d))
    ans = 10**1000
    
    s = 0
    for i in range(-m, m+1):
        s += abs(i)*d[K+i]
    if isch:
        s += abs(m+1)*d[K+m+1]
    
    for i in range(K+1, 2*K+2):
        if d[i-1]:
            ans = min(ans, s)
        s -= b[i+m+isch]-b[i]
        s += b[i]-b[i-m-isch]
        
    print(ans)


F('t')
F('a')
F('b')






