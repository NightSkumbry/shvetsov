
with open('./files/17-381.txt') as f:
    a = list(map(int, f.read().strip().split('\n')))

b = list(map(lambda x: len(str(abs(x))) == 4, a))

m = max(filter(lambda x: len(str(abs(x))) == 4 and abs(x)%100 == 39, a))**2

ans = 0
ms = 0
for i in range(len(a) - 1):
    if b[i] != b[i+1] and (a[i]+a[i+1])**2 <= m:
        ans += 1
        ms = max(ms, a[i]+a[i+1])

print(ans, ms)
