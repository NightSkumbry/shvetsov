from collections import Counter as C

with open('./files/9-176.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if cm[0][1] > 1:
        if sum(filter(lambda x: c[x] == 1, i)) % 2 == 1:
            ans += 1

print(ans)



