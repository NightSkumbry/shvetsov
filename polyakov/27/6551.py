
def A():
    with open('./files/27-156a.txt') as f:
        a = f.read().strip().split('\n')
        k = int(a[0].split()[1])
        a = list(filter(lambda x: abs(x) <= 10_000, map(int, a[1:])))
    
    from itertools import accumulate
    b = [0] + list(accumulate(a))
    
    ans = 10**100
    for i in range(len(b)):
        for j in range(i+k, len(b)):
            if (b[j]-b[i]) % 131 == 0:
                ans = min(ans, b[j]-b[i])
    print(abs(ans))
    

def B():
    with open('./files/27-156b.txt') as f:
        a = f.read().strip().split('\n')
        k = int(a[0].split()[1])
        a = list(filter(lambda x: abs(x) <= 10_000, map(int, a[1:])))
    
    from itertools import accumulate
    b = [0] + list(accumulate(a))
    
    most = [float('-inf')]*131
    ans = float('inf')
    for i in range(k, len(b)):
        most[b[i-k]%131] = max(most[b[i-k]%131], b[i-k])
        ans = min(ans, b[i]-most[b[i]%131])
    
    print(abs(ans))




from timeit import timeit as t
print(t(A, number=1))
print(t(B, number=1))


