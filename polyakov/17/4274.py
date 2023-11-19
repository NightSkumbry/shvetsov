with open('./files/17-1.txt') as f:
    a = list(map(int, f.read().strip().split()))

ans = 0
m = -100000000

for i in range(1, len(a)-1):
    j = i+1
    k = i-1
    if a[k] > a[i] < a[j]:
        ans += 1
        m = max(m, a[i])

print(ans, m)
