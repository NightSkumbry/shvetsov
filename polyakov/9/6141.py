from collections import Counter as C

with open('./files/9-194.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if cm[0][1] == 1:
        if sum([k%2 == 0 for k in i]) <= 2:
            if sum([k*(k%2 == 0) for k in i]) > sum([k*(k%2 == 1) for k in i]):
                ans += 1


print(ans)

