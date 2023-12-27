
with open('./some_files/var/26-42.txt') as f:
    a = []
    z = []
    k = int(f.readline().split()[1])
    
    for i in f.readlines():
        i = i.split()
        if i[0] == 'A':
            a.append([int(i[1]), int(i[2])])
        else:
            z.append([int(i[1]), int(i[2])])
        a.sort()
        z.sort()


for i in a:
    if k - i[0]*i[1] > 0:
        k -= i[0]*i[1]
    else:
        h = i[0]
        while k>0:
            k-=h
        if k < 0:
            k += h

ans = 0
for i in z:
    if k - i[0]*i[1] > 0:
        k -= i[0]*i[1]
        ans += i[1]
    else:
        h = i[0]
        while k>0:
            k-=h
            ans += 1
        if k < 0:
            k += h
            ans -= 1

print(ans, k)







