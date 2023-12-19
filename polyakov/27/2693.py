
def A():
    with open('./files/27-33a.txt') as f:
        a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[1:]))
    
    d = [0] * 4
    
    for k in a:
        s1 = k[0] + k[1]
        s2 = k[0] + k[2]
        s3 = k[1] + k[2]
        s = [s1, s2, s3]
        for i in d:
            s += [s1 + i, s2 + i, s3 + i]
        for i in range(len(d)):
            m = max(map(lambda x: x*(x%4 == i), s))
            d[i] = m
    
    print(d[0])


def B():
    with open('./files/27-33b.txt') as f:
        a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[1:]))
    
    d = [0] * 4
    
    for k in a:
        s1 = k[0] + k[1]
        s2 = k[0] + k[2]
        s3 = k[1] + k[2]
        s = [s1, s2, s3]
        for i in range(len(d)):
            s += [s1 + d[i], s2 + d[i], s3 + d[i]]
        for i in range(len(d)):
            m = max(map(lambda x: x*(x%4 == i), s))
            d[i] = m
    
    print(d[0])



import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))


