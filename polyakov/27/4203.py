nost = [3,5,10,15,17,24,25,31,35,38,52,55,59,65,66]
inf = float('inf')

def A():
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
    
        
            






import timeit
print(timeit.timeit(A, number=1))
