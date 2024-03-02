a = 3*15**1140 + 2*15**1025 + 15**923 - 3*15**85 + 2*15**74 + 3

r = []
while a:
    r.append(a%15)
    a//=15

f = r[0]
ans = 0
h = 1
for i in r[1:]:
    if i == f:
        h += 1
    else:
        print(h)
        ans = max(ans, h)
        h = 1
        f = i

print('ans: ',max(ans, h))

