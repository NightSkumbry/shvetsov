

def F(file):
    with open(f'./hw/hw17/27-186{file}.txt') as f:
        N, K = map(int, f.readline().split())
        a = [int(i) for i in f]

    ans = -10**100
    v = b = -10**100

    for i in range(len(a)):
        
        if i > K:
            ans = max(ans, a[i] + a[i-K] + b, a[i] + v)
        
        if i >= K:
            v = max(v, a[i]+a[i-K])
            b = max(b, a[i-K])
    
    print(ans)



F('t')
F('a')
F('b')









