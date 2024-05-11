# from itertools import accumulate
from math import ceil

def F(file):
    with open(f'./files/27-124{file}.txt') as f:
        N, K, V, M = map(int, f.readline().split())
        a = [list(map(int, i.split())) for i in f]

    d = [0]*K
    for i in a:
        d[i[0]-1] = ceil(i[1]/V)
    d *= 3
    # b = [0] + list(accumulate(d))
    s = sum(d[K-M:K+M+1])
    
    ans = 0
    
    for i in range(K+1, 2*K+2):
        if d[i-1]:
            ans = max(ans, s)
        s -= d[i-M-1]
        s += d[i+M]
    
    print(ans)


F('')
F('a')
F('b')











