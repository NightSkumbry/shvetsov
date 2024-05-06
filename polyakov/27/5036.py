from itertools import accumulate


def F(file):
    with open(f'./files/27-99{file}.txt') as f:
        N = int(f.readline())
        n = N//2-1
        a = [int(i) for i in f]

    a *= 3
    b = [0] + list(accumulate(a))
    

    # s = b[N]-b[N-n] + b[N+n+1]-b[N+1] + a[N-n-1]
    s = 0
    for i in range(-n-1, n+1):
        s += a[N+i]*abs(i)
    
    ans = 10**1000
    o = 6
    for i in range(N+1, 2*N):
        if s <= ans:
            o = i-N
            ans = min(ans, s)
        s += b[i]-b[i-n-1]
        s -= b[i+n+1]-b[i]
    if s <= ans:
            o = i-N
            ans = min(ans, s)

    print(s, o)

F('t')
F('a')
F('b')













