
from itertools import product, permutations

a = set()
for i in product('осеюгхнт', repeat=4):
    a.add(''.join(i))

ans = 0
for i, e in enumerate(sorted(a), 1):
    if i%2:
        if e[0] != 'н':
            if e.count('о') >= 2:
                if e.count('с') == 0:
                    ans = i
print(ans)


