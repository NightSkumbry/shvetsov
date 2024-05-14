from collections import Counter as C

with open('./files/9-228.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if cm[0][1] > 1:
        if c[max(i)] == 1:
            if sum([k for k in i if c[k] > 1]) < max(i):
                ans += 1

print(ans)



