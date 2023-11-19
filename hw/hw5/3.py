import random

a = [random.randint(1, 100) for _ in range(6)]
print(a)
d = [0 for i in range(7)]

ans = 0
for i in a:
    d[(7-i%7)%7] += 1

for i in a:
    ans += d[i%7] - (i%7 == 0)
    d[(7-i%7)%7] -= 1

print(ans)