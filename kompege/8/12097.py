
from itertools import product
a = set()
ans = 0

for i in product(set('гирлянда'), repeat=6):
    a.add(i)

a = sorted(a)
for i, e in enumerate(a, 1):
    if i%2 == 0:
        if e[0] != 'я':
            if e.count('д') == 3:
                ans = max(ans, i)

print(ans)



