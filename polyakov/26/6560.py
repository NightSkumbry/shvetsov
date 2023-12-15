
with open('./files/26-123.txt') as f:
    a = f.read().strip().split('\n')
    m = int(a[0].split()[0])
    a = list(map(lambda x: list(map(int, x.split())), a[1:]))
    a.sort(key=lambda x: x[0])
    

ans = 0
mans = 0


ms = [0 for _ in range(m+1)]
s = 0

arenda = []

ai = 0
for i in range(a[-1][0]+a[-1][1]+2000):
    while ai < len(a) and a[ai][0] == i:
        l = a[ai]
        if ms[l[2]] == 0:
            ans += 1
        else:
            ms[l[2]] -= 1
        arenda.append([l[1]+1, l[3]])
        mans = max(len(list(filter(lambda x: x[0] > 1, arenda))), mans)
        ai += 1
    
    todel = []
    for ind, r in enumerate(arenda):
        r[0] -= 1
        if r[0] == 0:
            todel.append(ind)
            ms[r[1]] += 1
    
    for i in todel[::-1]:
        arenda.pop(i)


print(ans, mans)




