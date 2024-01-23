
with open('./files/9-170.csv') as f:
    a = [sorted(map(int, i.split(','))) for i in f]

ans = 0

for i in a:
    if len(set(i)) == 6:
        if sum(i)/6 >= (i[2] + i[3])/2:
            ans += 1

print(ans)

