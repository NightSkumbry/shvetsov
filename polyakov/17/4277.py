with open('./files/17-1.txt') as f:
    a = list(map(int, f.read().strip().split()))


ans = 0
m = 0
d = 1
for i in range(len(a)-1):
    j = i+1
    if a[j] < a[i]:
        d += 1
    else:
        m = max(d, m)
        d = 1

for i in range(len(a)-1):
    j = i+1
    if a[j] < a[i]:
        d += 1
    else:
        d = 1
    if d == m:
        ans += 1

print(m, ans)
