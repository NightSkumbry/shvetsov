
with open('./polyakov/variants/var_12/26-122.txt') as f:
    K, n = [int(i) for i in f.readline().split()]
    a = [list(map(int, i.split())) for i in f]

a.sort()

d = [[0]*K]
ai = 0
t = 0
while ai < len(a):
    while ai < len(a) and a[ai][0] == t:
        for i in d:
            if not all(i):
                i[i.index(0)] = a[ai][1]
                break
        else:
            d.append([a[ai][1]] + [0]*(K-1))
        ai += 1
        
                
    
    for i in d:
        for k in range(K):
            if i[k] == t:
                i[k] = 0
            
    t += 1
        

print(len(d), sum([sum([i != 0 for i in k]) for k in d]))








