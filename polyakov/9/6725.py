from collections import Counter as C

with open('./files/9-225.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if cm[0][1] == 2 and cm[1][1] == 1:
        if (max(i) + min(i))**2 < sum([k**2 for k in i]) - min(i)**2 - max(i)**2:
            ans += 1

print(ans)



