
from itertools import product

ans = set()

for i in product('012345678', repeat=5):
    if i[0] != '0':
        if i[0] in '2468':
            if i[-1] not in '18':
                if i.count('3') <= 1:
                    ans.add(i)

print(len(ans))
