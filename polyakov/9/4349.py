
with open('./files/9-130.csv') as f:
    a = [sorted(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    if i[2] - i[1] == i[1] - i[0] > 0:
        ans += 1

print(ans)



