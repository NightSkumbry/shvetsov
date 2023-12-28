

def A():
    with open('./files/27-176a.txt') as f:
        n, k, *a = map(int, (f.read().strip().split()))
        # print(n,k,a[:3])
    b = [0 for i in range(10_001)]
    for i in a:
        b[i] += i
    m = []
    for i in b[k:]:
        if len(m)-k+1 >= 0:
            m.append(max(m[:len(m)-k+1]+[0])+i)
        else:
            m.append(i)
    print(max(m))


def B():
    with open('./files/27-176b.txt') as f:
        n, k, *a = map(int, (f.read().strip().split()))
        # print(n,k,a[:3])
    b = [0 for i in range(10_001)]
    for i in a:
        b[i] += i
    m = []
    for i in b[k:]:
        if len(m)-k+1 >= 0:
            m.append(max(m[:len(m)-k+1]+[0])+i)
        else:
            m.append(i)
    print(max(m))


from timeit import timeit as t
print(t(A, number=1))
print(t(B, number=1))



