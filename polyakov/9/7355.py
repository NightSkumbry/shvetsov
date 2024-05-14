from collections import Counter as C

with open('./files/9-228.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]
b = list(zip(*a))
c = list(map(C, b))

ans = 0
for i in a:
    l = 0
    for k in range(len(i)):
        if i.count(i[k]) == 1:
            if c[k][i[k]] < 170:
                l += 1
    if 4 >= l >= 1:
        ans += 1

print(ans)


