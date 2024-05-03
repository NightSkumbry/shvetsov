
from itertools import product, permutations

ans = set()

for i in product('скоемч', repeat=4):
    ans.add(''.join(i))

a = 0
for i, e in enumerate(sorted(ans), 1):
    if i%2 == 0:
        if e[0] == 'ч' and e[-1] == 'о':
            a = i
print(a)

