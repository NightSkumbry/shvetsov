from collections import Counter as C
ans = 0 

with open('./files/9-194.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]


for r in a:
    c = C(r).most_common()
    if c[0][1] == 2 and c[1][1] == 1:
        if c[0][0]*2 < sum(r) - c[0][0]*2:
            ans += 1

print(ans)