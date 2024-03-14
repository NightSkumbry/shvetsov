# a78bf7c8-e640-46fd-9e7c-c504952c4905
    
from functools import cache
import sys
sys.setrecursionlimit(2000)

def A(f):
    with open(f'./yandex_edu/variants/a78bf7c8-e640-46fd-9e7c-c504952c4905/27_{f}.txt') as f:
        m = int(f.readline())
        g = int(f.readline())
        a = [list(map(int, i.split())) for i in f]
    
    
    @cache
    def rec(m,i):
        if i >= g:
            return 0, []
        
        if m >= a[i][0]:
            k1,b1 = rec(m, i+1)
            k2,b2 = rec(m-a[i][0], i+1)
            k2 += a[i][1]
            b1, b2 = b1.copy(), b2.copy()
            b2.append(i)
            if k2 >= k1:
                k = k2
                b = b2
            else:
                k = k1
                b = b1

        else:
            k, b = rec(m, i+1)
            b = b.copy()
        
        return k, b
    
    k, h = rec(m, 0)
    print(k, h, sum([a[i][1] for i in h]))

A('A')
A('B')






