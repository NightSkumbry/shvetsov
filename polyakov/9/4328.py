
with open('./files/9-107.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    if max(i) > 90:
        if sum(i) == 180:
            ans += 1

print(ans)





