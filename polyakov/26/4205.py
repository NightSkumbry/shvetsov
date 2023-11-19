with open('./files/26-57.txt') as f:
    a = list(map(int, f.read().strip().split()[2:]))
    m = 20000
    a.sort()
    a = a[::-1]
# a = list(map(int, '17 15 14 12 11 8 6 5 4 2'.split()))
# m = 30

ans = 0

while sum(a) >= m:
    s = a[0]
    a.pop(0)
    while m-s > a[0]:
        s += a[0]
        a.pop(0)
        ans+=1
    d = list(filter(lambda x: x >= m-s, a))[-1]
    if s+d-m > 0:
        a.append(s+d-m)
    ans += 1
    a.remove(d)
    a.sort()
    a = a[::-1]

print(ans, len(a))
