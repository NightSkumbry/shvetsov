
with open('./files/24-280.txt') as f:
    a = f.read().lower().strip().replace('x', '1').replace('y', '1').split('1')

ans = 30
for q in a:
    l = 0
    sc = uc = nc = 0
    for r in range(len(q)):
        if q[r] == 's': sc += 1
        if q[r] == 'u': uc += 1
        if q[r] == 'n': nc += 1
        while sc > 10 or uc > 10 or nc > 10:
            if q[l] == 's': sc -= 1
            if q[l] == 'u': uc -= 1
            if q[l] == 'n': nc -= 1
            l += 1
        ans = max(ans, r-l+1)
    
print(ans)




