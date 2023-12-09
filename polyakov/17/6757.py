
with open('./files/17-379.txt') as f:
    a = list(map(int, f.read().strip().split()))

b = list(map(lambda x: len(str(x)) == 4, a))

m = max(filter(lambda x: x%100 == 15, a))


ans = 0
ms = 0
for i in range(len(a)-2):
    if sum(b[i:i+3]) == 1 and sum(a[i:i+3]) >= m:
        ans += 1
        ms = max(ms, sum(a[i:i+3]))

print(ans, ms)


