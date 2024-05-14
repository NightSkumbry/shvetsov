from collections import Counter as C

with open('./files/9-220.csv') as f:
    a = [sorted(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    if (i[0] + i[-1]) %3 == 0:
        if any([i[3]-i[2] == i[1]-i[0], i[3]-i[1] == i[2]-i[0]]):
            ans += 1

print(ans)

