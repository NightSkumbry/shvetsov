with open('./files/17-1.txt') as f:
    a = list(map(int, f.read().strip().split()))
    b = [False for _ in range(len(a))]

ans = 0
m = 10000000

for i in range(1, len(a)-1):
    j = i+1
    k = i-1
    if a[k] < a[i] > a[j]:
        ans += 1
        b[i] = True
c = list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(b))))
for i in range(len(c)-1):
    m = min(m, c[i+1]-c[i])
    


print(ans, m)
