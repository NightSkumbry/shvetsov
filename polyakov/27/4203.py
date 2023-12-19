nost = [3,5,10,15,17,24,25,31,35,38,52,55,59,65,66]
inf = float('inf')

def A_BAD():
    with open('./files/27-69b.txt') as f:
        a = list(map(lambda x: sorted(list(map(int, x.split()))), f.read().strip().split('\n')[1:]))
    
    s = 0
    ost = [inf for _ in range(70)]
    can_be = [{} for _ in range(70)]
    for i in nost:
        ost[i] = 0
    b = []
    for i in a:
        s += i[2] + i[1]
        b.append(i[1]-i[0])
        b.append(i[2]-i[0])
        
    for i in range(70):
        for k in b:
            ost[i] = min(k + ost[(i-k)%70], ost[i])
            if k%70:
                if i in can_be[(i-k)%70].keys():
                    can_be[(i-k)%70][i] = min(can_be[(i-k)%70][i], k)
                else:
                    can_be[(i-k)%70][i] = k
    for _ in range(70):
        for i in range(70):
            for k, x in can_be[i].items():
                ost[k] = min(ost[k], x + ost[i])
    
    print(s - ost[s%70])
    

def A():
    with open('./files/27-69a.txt') as f:
        a = list(map(lambda x: sorted(list(map(int, x.split()))), f.read().strip().split('\n')[1:]))
    
    d = [0]*70
    
    for k in a:
        s1 = k[0] + k[1]
        s2 = k[0] + k[2]
        s3 = k[2] + k[1]
        s = [s1, s2, s3]
        for i in d:
            s += [s1+i, s2+i, s3+i]
        for i in range(len(d)):
            m = max(map(lambda x: x*(x%70 == i), s))
            d[i] = m
    print(max([d[i] for i in nost]))
    

def B():
    with open('./files/27-69b.txt') as f:
        a = list(map(lambda x: sorted(list(map(int, x.split()))), f.read().strip().split('\n')[1:]))
    
    d = [0]*70
    
    for k in a:
        s1 = k[0] + k[1]
        s2 = k[0] + k[2]
        s3 = k[2] + k[1]
        # s = [s1, s2, s3]
        s = [0]*70
        s[s1%70] = max(s[s1%70], s1)
        s[s2%70] = max(s[s2%70], s2)
        s[s3%70] = max(s[s3%70], s3)
        
        for i in d:
            # s += [s1+i, s2+i, s3+i]
            s[(s1+i)%70] = max(s[(s1+i)%70], s1+i)
            s[(s2+i)%70] = max(s[(s2+i)%70], s2+i)
            s[(s3+i)%70] = max(s[(s3+i)%70], s3+i)
        for i in range(len(d)):
            # m = max(map(lambda x: x*(x%70 == i), s))
            d[i] = s[i]
    print(max([d[i] for i in nost]))






import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))
