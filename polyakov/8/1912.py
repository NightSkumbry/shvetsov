from itertools import product
ans = set()
for i in product('берклий', repeat=4):
    if i[0] != 'й':
        if 'и' in i or 'е' in i:
            ans.add(i)
print(len(ans))












