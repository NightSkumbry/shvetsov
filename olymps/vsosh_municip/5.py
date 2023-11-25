# 68

s, t = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
a.sort()
# y = list(filter(lambda x: x >= t, a))[0]
# a.remove(y)
p = [a[0]]
for i in a[1:]:
    p.append(p[-1]+i)
x = s+t
su = 0
suk = []
while su < x:
    i = 0
    while x-su > p[i]:
        i += 1
    su += a[i]
    suk.append(a[i])

if su - suk[-1] >= s:
    print(su)
else:
    for i in suk:
        a.remove(i)
    su += list(filter(lambda x: x >= t, a))[0]
    print(su)