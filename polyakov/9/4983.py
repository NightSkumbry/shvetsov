ans = 0
with open('./files/9-154.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

for i in a:
    if (max(i) + min(i))**2 > sum([i[k]**2 for k in range(5)]) - max(i)**2 - min(i)**2:
        ans += 1
print(ans)

