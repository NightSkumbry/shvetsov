from itertools import accumulate
from math import ceil


def F(file):
    with open(f'./files/27{file}_4713.txt') as f:
        N = int(f.readline())
        a = [list(map(int, i.split())) for i in f]
    m = max(map(lambda x: x[0], a))
    
    d = [0]*(m+100)
    for i in a:
        if file == 'T':
            d[i[0]-1] = ceil(i[1]/96)
        else:
            d[i[0]-1] = ceil(i[1]/36)
    
    b = [0] + list(accumulate(d))
    
    ans = 10**1000
    
    s = 0
    for i in range(1, len(d)):
        s += d[i]*i
    
    for i in range(1, len(d)):
        if d[i-1]:
            ans = min(ans, s)
        s -= b[-1]-b[i]
        s += b[i]

    print(ans)





F('T')
F('A')
F('B')




