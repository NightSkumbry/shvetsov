
ans = 1110
for n in range(11, 10000):
    a = []
    while n:
        a.append(n%3)
        n //= 3
    if a.count(0) + a.count(2) > a.count(1):
        a.append(2)
        a.append(2)
    else:
        a.append(1)
        a.append(1)
    a = int(''.join(map(str, a[::-1])), 3)
    if a > 100:
        ans = min(ans, a)

print(ans)




