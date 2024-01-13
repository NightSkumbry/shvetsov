ans = 0
with open('./files/9-168.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

for r in a:
    s = sum(r)/5
    if sum([i > s for i in r]) >= 3:ans += 1
print(ans)