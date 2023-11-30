def A():
    with open('./files/27_A_9755.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]
    
    ms = 10**10
    for i in range(0, len(a)-2*k):
        for j in range(i+k, len(a)-k):
            for y in range(j+k, len(a)):
                ms = min(ms, a[i]+a[j]+a[y])
    print(ms)




def B1():
    with open('./files/27_B_9755.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]

    b = [0]*k
    while a[len(b)+k:]:
        m = min(a[len(b)+k:])
        mi = len(a)-a[::-1].index(m)-1
        for i in a[len(b):mi-k+1]:
            b.append(m+i)
    
    c = []
    while b[len(c)+k:]:
        m = min(b[len(c)+k:])
        mi = len(b)-b[::-1].index(m)-1
        for i in a[len(c):mi-k+1]:
            c.append(m+i)
    
    print(min(c))
    

def B2():
    with open('./files/27_B_9755.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]
    
    ind1 = [0]*k
    b = [0]*k
    while a[len(b)+k:]:
        m = min(a[len(b)+k:])
        mi = len(a)-a[::-1].index(m)-1
        for ind, i in enumerate(a[len(b):mi-k+1], len(b)):
            b.append(m+i)
            ind1.append([ind, mi])
    
    ind2 = []
    c = []
    while b[len(c)+k:]:
        m = min(b[len(c)+k:])
        mi = len(b)-b[::-1].index(m)-1
        for ind, i in enumerate(a[len(c):mi-k+1], len(c)):
            c.append(m+i)
            ind2.append([ind] + ind1[mi])
    
    print(min(c))
    print(f'Индексы: {ind2[c.index(min(c))]}')
    print(f'Значения: {list(map(lambda x: a[x], ind2[c.index(min(c))]))}')


import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B1, number=1))
print(timeit.timeit(B2, number=1))
