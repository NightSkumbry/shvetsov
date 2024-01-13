from collections import Counter as C
ans = 0
with open('./files/9-226.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

for r in a:
    c = C(r)
    cm = c.most_common()
    if cm[0][1] == cm[1][1] == 2 and cm[2][1] == 1:
        if c[max(r)] == 1:
            print(sum(r))
            break

