from tqdm import tqdm

def F(file):
    with open(f'./files/27-186{file}.txt') as f:
        N, K, *a = map(int, f.read().strip().split())

    a1 = -10**23
    a2 = -10**23
    b = -10**23
    ans = -10**23
    
    for i in tqdm(range(K+1,N)):
        a1 = max(a1, a[i-K-1])
        a2 = a1+a[i-K]
        ans = max(ans, a2+a[i])
        b = max(b, a[i-K-1]+a[i-1])
        ans = max(ans, b+a[i])
    print(ans)
            



F('t')
F('a')
F('b')









