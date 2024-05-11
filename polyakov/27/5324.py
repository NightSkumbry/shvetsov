from itertools import accumulate
from math import ceil

def F(file):
    with open(f'./files/27-122{file}.txt') as f:
        N, V = map(int, f.readline().split())
        a = sorted([list(map(int, i.split())) for i in f], key=lambda x: x[0])

    d = [0]*(a[-1][0]+10000)
    for i in a:
        d[i[0]-1] = ceil(i[1]/V)

    b = [0] + list(accumulate(d))
    s = 0
    for i in range(1, len(d)):
        s += i*d[i]
    
    ans = 100**1000
    for i in range(1, len(d)):
        if d[i-1]:
            ans = min(ans, s)
        s += b[i]
        s -= b[-1]-b[i]
    
    print(ans)



F('t')
F('a')
F('b')








