
with open('./files/26-112.txt') as f:
    a = f.read().strip().split('\n')
    n = int(a[0].split()[0])
    a = list(map(lambda x: list(map(int, x.split())), a[1:]))
    for i, e in enumerate(a):
        a[i] = [e[0], i, e[1]] # Время прихода, порядковый номер, время обслуживания
    a.sort(key=lambda x: x[0])

from queue import Queue as Q

q = Q()
b = [0 for i in range(n)]
bc = [0 for i in range(n)]
ai = 0

ans = 0

for i in range(24*60+1):
    for k in range(n):
        if b[k]:
            b[k] -= 1
    while ai < len(a) and a[ai][0] == i:
        q.put(a[ai])
        ai += 1
    if q.qsize():
        for k in range(n):
            if b[k] == 0 and q.qsize():
                j = q.get()
                b[k] = j[2]
                ans = i
                bc[k] += 1

print(max(bc), ans)
                
    




