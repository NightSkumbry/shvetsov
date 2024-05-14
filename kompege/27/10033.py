from sys import setrecursionlimit
setrecursionlimit(10001)

def F(file):
    with open(f'./files/27{file}_10033.txt') as f:
        N, W, K = map(int, f.readline().split())
        a = [list(map(int, i.split())) for i in f]

    s = []
    g = []
    for i in a:
        if i[1] == 0:
            s.append(i[0])
        else:
            g.append(i[0])

    s = sorted(s)
    g = sorted(g)
    
    cgs = [0]*(W+1)
    
    def cg(v, i=0, su=0, b=False):
        if b: cgs[su] += 1
        if i >= len(g):
            return
        if su + g[i] > W:
            return
        if g[i] not in v:
            cg(v + [g[i]], i+1, su+g[i], True)
        cg(v, i+1, su, False)
    
    cg([])
    
    ans = [0]
    def cs(v, i=0, su=0, b=True):
        if b: ans[0] += cgs[W-su]
        if i >= len(s):
            return
        if su + s[i] > K:
            return
        if s[i] not in v:
            cs(v + [s[i]], i+1, su+s[i], True)
        cs(v, i+1, su, False)

    cs([])
    
    print(ans)




F('T')






