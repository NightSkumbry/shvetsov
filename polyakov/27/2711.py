from math import gcd

def A(f):
    with open(f'./files/27-36{f}.txt') as f:
        n = int(f.readline())
        a = [list(map(int, i.split())) for i in f]
    
    g = [0]*10
    
    j = gcd(a[0][0], a[0][1])
    g[j%10] = max(g[j%10], j)
    j = gcd(a[0][2], a[0][1])
    g[j%10] = max(g[j%10], j)
    j = gcd(a[0][0], a[0][2])
    g[j%10] = max(g[j%10], j)
    
    for i in a[1:]:
        h = g.copy()
        g = [0]*10
        p = [0]*10
        j = gcd(i[0], i[1])
        p[j%10] = max(p[j%10], j)
        j = gcd(i[2], i[1])
        p[j%10] = max(p[j%10], j)
        j = gcd(i[0], i[2])
        p[j%10] = max(p[j%10], j)
        for k in range(10):
            for u in range(10):
                if p[k] and h[u]:
                    g[(k+u)%10] = max(g[(k+u)%10], h[u] + p[k])
        
    print(g[0])


A('a')
A('b')









