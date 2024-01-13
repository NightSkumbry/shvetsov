ans = 0
from collections import Counter as C

with open('./files/9-194.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

for r  in a:
    c = C(r).most_common()
    ch = sum(map(lambda x: x%2, r))
    chs = sum(filter(lambda x: x%2 == 0, r))
    if c[0][1] == 1:
        if ch < 3:
            if chs < sum(r)-chs:
                ans += 1
print(ans)