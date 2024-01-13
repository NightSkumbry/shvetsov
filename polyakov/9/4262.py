from math import gcd

with open('./files/9-97.csv') as f:
    a = [list(map(int, i.split(','))) for i in f.readlines()]

ans = 0
for i in a:
    if gcd(*i) == 1 and sum([i[k]**2 for k in range(3)]) == 2 * max(i)**2:
        ans += 1


print(ans)


