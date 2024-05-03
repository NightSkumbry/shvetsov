from math import ceil
with open('./files/26.6_13394.txt') as f:
    N = int(f.readline())
    a = [int(i) for i in f]

a.sort()
s0 = sum(filter(lambda x: x <= 350, a))
ans1 = ans = s0
a = list(filter(lambda x: x>350, a))
l = 0
r = len(a)-1
n = 1
while l < r:
    if n%3:
        ans1 += a[r]
        r -= 1
    else:
        ans1 += a[l]*0.25
        l += 1
    n += 1
ans1 = ceil(ans1)
a = a[::-1]
for i in range(0, len(a), 3):
    ans += a[i]
    if i + 1 < len(a):
        ans += a[i+1]
    if i + 2 < len(a):
        ans += ceil(a[i+2]*0.25)
print(ans, ans1)



