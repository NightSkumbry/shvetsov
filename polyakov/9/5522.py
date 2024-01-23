from collections import Counter as C

with open('./files/9-170.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if cm[0][1] == 3 and cm[1][1] == 1:
        if (sum(i) - 3*cm[0][0]) * 3 <= cm[0][0]**3:
            ans += 1

print(ans)



