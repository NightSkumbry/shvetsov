from collections import Counter as C

with open('./files/9-228.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]
c = list(map(C, zip(*a)))

ans = 0
for i in a:
    p = 0
    for k in range(len(i)):
        if i.count(i[k]) == 1:
            if c[k][i[k]] < 170:
                p += 1
    if p > 4:
        ans +=1

print(ans)

