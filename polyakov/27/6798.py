
def A():
    with open('./files/27-168a.txt') as f:
        n, k = map(int, f.readline().split())
        a = [int(i) for i in f]
    
    ans = 0
    for i in range(n):
        for j in range(i+k, n):
            for l in range(j+k, n):
                ans = max(ans, a[i]*a[j]*a[l])
    print(ans%(10**6+1))

A()
def B():
    with open('./files/27-168a.txt') as f:
        n, k = map(int, f.readline().split())
        a = [int(i) for i in f]
    h1 = 0
    h2 = 0
    h3 = 0
    for i in range(2*k, n):
        h1 = max(h1, a[i-2*k])
        h2 = max(h2, a[i-k]*h1)
        h3 = max(h3, a[i]*h2)
    print(h3%(10**6+1))


B()









