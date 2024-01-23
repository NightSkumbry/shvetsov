from collections import Counter as C

with open('./files/9-190.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if (cm[0][1] > 1) ^ (len(list(filter(lambda x: x%2, i))) == 3):
        ans += 1

print(ans)



