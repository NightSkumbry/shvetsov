
from itertools import product
ans = 0
for i in product('012345678', repeat=5):
    if i[0] not in '07':
        if i.count('1') == 2:
            ans = max(ans, int(''.join(i), 9))

print(ans + 1) # нечётное - ок




