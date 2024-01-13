
ans = 0
with open('./files/9-154.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]
    
for r in a:
    if (max(r)*min(r))**2 > 3 * r[0]*r[1]*r[2]*r[3]*r[4]/max(r)/min(r):
        ans += 1
    

print(ans)

