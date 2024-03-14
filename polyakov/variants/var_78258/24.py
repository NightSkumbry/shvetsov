with open('./polyakov/variants/var_78258/24.txt') as f:
    a = f.read().lower().strip().split('y')

ans = 0
for i in a:
    k = list(map(len, i.split('.')))
    if i.count('.') <= 5:
        ans = max(ans, len(i))
    for i in range(len(k)):
        ans = max(ans, sum(k[i:i+6])+len(k[i:i+6])-1)


print(ans)