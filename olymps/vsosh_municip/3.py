# 100

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(list(set(a)))
h = [0 for i in range(b[-1]+1)]
for i in a:
    h[i] += 1
 
p = [h[0]]
for i in h[1:]:
    p.append(p[-1]+i)
 
ans = 0
 
for i in b:
    j = 0
    i2 = min(k*i, len(p)-1)
    l = p[i2] - p[i-1] - 2
    if l <= 0:
        continue
    for j, r in enumerate(range(l, l-h[i]+1, -1), 1):
        ans += j*r
    ans += (j+1)*((l-h[i]+1)+1)/2*(l-h[i]+1)
 
print(int(ans))

