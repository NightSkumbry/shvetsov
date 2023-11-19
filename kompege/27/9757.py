
def A():
    with open('./files/27A_9757.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]
    m = 0

    for x in range(0, len(a)-k-k):
        for y in range(x+k, len(a)-k):
            for z in range(y+k, len(a)):
                h = a[x]*a[y]*a[z]
                if h > m and h%2023 == 0:
                    m = h
    print(m)

g = [(1, 1, 2023), (1, 7, 289), (1, 17, 119), (1, 2023, 1), (7, 1, 289), (7, 17, 17), (17, 1, 119), (17, 7, 17), (17, 17, 7), (2023, 1, 1)]
def B():
    with open('./files/27B_9757.txt') as f:
        ak = list(map(int, f.read().strip().split('\n')))
        k = ak[0]
        ak = ak[2:]
    maxi = 0
    for q,w,e in g:
        print('wait')
        a1 = list(map(lambda x: x*(x%q==0), ak))
        a2 = list(map(lambda x: x*(x%w==0), ak))
        a3 = list(map(lambda x: x*(x%e==0), ak))
        b = [0 for i in range(k)]
        while a3[len(b)+k:]:
            m = max(a3[len(b)+k:])
            mi = len(a3)-a3[::-1].index(m)-1
            for i in a2[len(b):mi-k+1]:
                b.append(m*i)
        c = []
        while b[len(c)+k:]:
            m = max(b[len(c)+k:])
            mi = len(b)-b[::-1].index(m)-1
            for i in a1[len(c):mi-k+1]:
                if (m*i)%2023 == 0:
                    h = m*i
                else:
                    h = 0
                c.append(h)
        maxi = max(max(c), maxi)
    print(maxi)
    
            
        






A()
import timeit
print(timeit.timeit(B, number=1))
