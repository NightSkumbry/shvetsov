from collections import Counter as C

with open('./files/9-210.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if c[max(i)] == 1:
        if cm[0][1] > 1:
            if max(i) + min(i) > sum(map(lambda x: x[0] * x[1] * (x[1] > 1), cm)):
                ans += 1

print(ans)



