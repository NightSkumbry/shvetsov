from itertools import product
ans = set()
for i in product('герой', repeat=4):
    if i[0] != 'й':
        if 'е' in i or 'о' in i:
            ans.add(i)
print(len(ans))