from itertools import product
ans = set()

for i in product('удача', repeat=5):
    if i[0] in 'уа':
        ans.add(''.join(i))

print(sorted(ans).index('удача') + 1)

