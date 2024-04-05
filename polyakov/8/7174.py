
from itertools import permutations

ans = set()
for i in permutations('ГЛУБИНА'):
    if i.index('Г') > i.index('А') and i.index('Г') > i.index('И'):
        ans.add(i)

print(len(ans))



