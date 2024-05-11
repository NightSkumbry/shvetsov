

def F(file):
    with open(f'./files/27{file}_6931.txt') as f:
        N = int(f.readline())
        a = [int(i) for i in f]
    a*=2
    b = list(map(lambda x: x%2, a))
    a = list(map(lambda x: x//2, a))
    K = b.index(1-b[0])
    c = [0]
    for i in range(K, N+K):
        d = b[i]
        c.append(c[-1]+a[i])
        if b[i+1]!=d:
            c.append(0)
 
            
    print(max(c))












F('T')
F('A')
F('B')


