from itertools import accumulate as C

def A():
    with open('./files/27-178a.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    
    a *= 3
    b = [0] + list(C(a))
    im = 0
    m = 0
    ans = 0
    for i in range(len(b)):
        if b[i] <= m:
            im = i
            m = b[i]
        if i-im >= len(a)//3:
            print('panic')
            m = min(b[im+1:i])
            im += b[im+1:i].index(m)+1
        ans = max(ans, b[i]-b[im])
    print(ans)


def B():
    with open('./files/27-178b.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    
    a *= 3
    b = [0] + list(C(a))
    im = 0
    m = 0
    ans = 0
    for i in range(len(b)):
        if b[i] <= m:
            im = i
            m = b[i]
        if i-im >= len(a)//3:
            print('panic')
            m = min(b[im+1:i])
            im += b[im+1:i].index(m)+1
        ans = max(ans, b[i]-b[im])
    print(ans)



from timeit import timeit as t
print(t(A, number=1))
print(t(B, number=1))



