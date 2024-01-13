
with open('./files/9-159.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    if sum(i)/5 < (max(i) + min(i))/2:
        ans += 1

print(ans)



