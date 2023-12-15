

def A():
    t = [[0, 100000000]]
    with open('./files/27-179a.txt') as f:
        a = list(map(lambda x: list(map(int, x.split())), ((f.read().strip().split('\n')[1:]))))
    for i in a:
        for ind, k in enumerate(t):
            if k[0] <= i[0]:
                if k[1] >= i[1]:
                    u = k.copy()
                    t[ind] = [u[0], i[0]]
                    t.insert(ind+1, [i[1], u[1]])
                    break
    
    print(len(t)-1)


def B():
    t = [[0, 100000000]]
    with open('./files/27-179b.txt') as f:
        a = list(map(lambda x: list(map(int, x.split())), ((f.read().strip().split('\n')[1:]))))
    for i in a:
        for ind, k in enumerate(t):
            if k[0] <= i[0]:
                if k[1] >= i[1]:
                    u = k.copy()
                    t[ind] = [u[0], i[0]]
                    t.insert(ind+1, [i[1], u[1]])
                    break
    
    print(len(t)-1)



import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))




