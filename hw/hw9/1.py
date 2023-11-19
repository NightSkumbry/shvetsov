import math

# 1 строка
print(sum([((5 + ((n%7)%2==0)) * 7**int(math.log(n, 7)+1) + n) > 14500 for n in range(343, 2402)]))

# Нормальное решение
ans = 0
for n in range(343, 2402):
    r = []
    while n:
        r.append(n%7)
        n //= 7
    r.append(5 + (r[0] % 2 == 0))
    a = 0
    for i, e in enumerate(r):
        a += e* 7**i
    if a > 14500:
        ans += 1
print(ans)






