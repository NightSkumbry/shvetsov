
with open('./files/9-183.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    m = max(i)
    if (sum([k**2 for k in i]) - 2*m**2)*m/2/i[0]/i[1]/i[2] > 0:
        ans += 1

print(ans)




