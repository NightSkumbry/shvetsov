
with open('./files/24-280.txt') as f:
    a = f.read().lower().strip().replace('a', '1').split('1')

ans= 0
for q in a:
    l = xc = yc = 0
    for r in range(len(q)):
        if q[r] == 'x': xc += 1
        if q[r] == 'y': yc += 1
        while max(xc, yc) > 1:
            if q[l] == 'x': xc -= 1
            if q[l] == 'y': yc -= 1
            l += 1
        if xc == yc == 1:
            ans = max(ans, r-l+1)





print(ans)







