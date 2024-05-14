from collections import Counter as C

with open('./files/9-228.csv') as f:
    a = [sorted(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    cm = c.most_common()
    if cm[0][1] == 2 and cm[1][1] == 1:
        if (i[0] + i[5])*2 > i[1]+i[2]+i[3]+i[4]:
            ans += 1

print(ans)


