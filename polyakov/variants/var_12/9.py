from collections import Counter as C

with open('./polyakov/variants/var_12/9-210.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if c[min(i)] == 1:
        if cm[0][1] > 1:
            if max(i) + min(i) < sum(filter(lambda x: c[x] > 1, i)):
                ans += 1
print(ans)
                







