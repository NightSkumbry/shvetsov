
from itertools import permutations as product

ans = set()
for i in product('0124567', 6):
    if i[0] != '0':
        if any([i[k] in '0246' and i[k+1] in '0246' for k in range(5)]):
            ans.add(i)
            
print(len(ans))








