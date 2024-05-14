
with open('./files/24-280.txt') as f:
    a = f.read().lower().strip()

ans = 0
l = xc = yc = 0
for r in range(len(a)):
    if a[r] == 'x': xc += 1
    if a[r] == 'y': yc += 1
    while max(xc, yc) > 1:
        if a[l] == 'x': xc -= 1
        if a[l] == 'y': yc -= 1
        l += 1
    if xc == yc == 1:
        ans = max(ans, r-l+1)


print(ans)





