from tqdm import tqdm


def F(file):
    with open(f'./polyakov/variants/var_87049/27{file}.txt') as f:
        N, K = map(int, f.readline().split())
        a = [list(map(int, i.split())) for i in f]
    P = max(map(lambda x: x[0], a))
    
    prebs = [{} for _ in range(10_000_000)]
    for i in a:
        prebs[i[1]-1][i[0]-1] = i[2]
    
    ans = 0
    
    mi = [-1]*P
    ma = [-1]*P
    
    
    for i in tqdm(range(K, 10_000_000)):
        for p, z in prebs[i-K].items():
            if mi[p] == -1:
                mi[p] = z
                ma[p] = z
            else:
                mi[p] = min(mi[p], z)
                ma[p] = max(ma[p], z)
        for p, z in prebs[i].items():
            if mi[p] != -1:
                ans = max(ans, abs(z-mi[p]), abs(z-ma[p]))
    print(ans)


F('t')
F('a')
F('b')



