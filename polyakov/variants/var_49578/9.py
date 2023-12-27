
from collections import Counter as C
ans = 0
with open('./some_files/var_49578/9-225.csv') as f:
    a = [list(map(int, i.split(','))) for i in f.readlines()]

for r in a:
    c = C(r).most_common()
    # print(c)
    # break
    if c[0][1] == 2 and c[1][1] == 1:
        if (max(r) + min(r))**2 < sum(map(lambda x: x**2, r)) - max(r)**2 - min(r)**2:
            ans += 1


print(ans)


