from collections import Counter as C

with open('./files/24-280.txt') as f:
    a = f.read().strip().lower()


l = r = 0
ans = 0

c = C(a[:1])

while r+1 < len(a):
    if c[a[r+1]] == 1:
        c[a[l]] -= 1
        l += 1
    else:
        r += 1
        c[a[r]] += 1
        ans = max(ans, r-l+1)

print(ans)
