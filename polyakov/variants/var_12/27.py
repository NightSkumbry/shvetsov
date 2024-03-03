
from tqdm import tqdm
def A(F):
    with open(f'./polyakov/variants/var_12/27-163{F}.txt') as f:
        N, K = [int(i) for i in f.readline().split()]
        a = [list(map(int, i.split())) for i in f]

    
    ans = 0

    for i in tqdm(range(len(a))):
        for j in range(i+K, len(a)):
            if a[i][0] == a[j][0]:
                ans = max(ans, abs(a[i][1]-a[j][1]))
    print(ans)

A('a')
# A('b')

def B():
    with open('./polyakov/variants/var_12/27-163b.txt') as f:
        N, K = [int(i) for i in f.readline().split()]
        a = [list(map(int, i.split())) for i in f]
    
    A = [-1] * 10000
    B = [100000000000] * 10000
    ans = 0
    for i in range(K, len(a)):
        n = a[i-K][0]
        if A[n] == -1:
            A[n] = a[i-K][1]
            B[n] = a[i-K][1]
        else:
            A[n] = max(A[n], a[i-K][1])
            B[n] = min(B[n], a[i-K][1])
        
        if A[a[i][0]] != -1:
            ans = max(ans, abs(a[i][1] - A[a[i][0]]), abs(a[i][1] - B[a[i][0]]))

    print(ans)

B()
