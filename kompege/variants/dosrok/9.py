from collections import Counter as C

with open('./kompege/variants/dosrok/9.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    c = C(i)
    mc = c.most_common()
    if 2*mc[0][0] < sum(i):
        if any([i[0]+i[1] == i[2]+i[3], i[0]+i[2] == i[1]+i[3], i[0]+i[3] == i[2]+i[1]]):
            ans += 1
print(ans)







