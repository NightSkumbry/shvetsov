from collections import Counter as C
ans = 0
with open('./files/9-210.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

for r in a:
    c = C(r)
    cm = c.most_common()
    if c[min(r)] == 1:
        if cm[0][1] != 1:
            if min(r) + max(r) < (sum(r) - min(r) - max(r))/2:
                ans += 1

print(ans)


