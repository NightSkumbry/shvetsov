
with open('./files/9-181.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    if i[0] * i[1] * i[2] * i[3] % max(i)**2 == 0:
        ans += 1
        
print(ans)






