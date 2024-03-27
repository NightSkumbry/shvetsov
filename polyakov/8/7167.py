from itertools import product
ans = set()
for i in product('ЖЮЯУЗЧДОФ', repeat=6):
    ans.add(''.join(i))

ans = sorted(ans)

for i, e in enumerate(ans, 1):
    if i%2 == 0:
        continue
    if e[0] != 'У' and e[-1] != 'У':
        if any([e[k] == e[k+1] == 'Ю' for k in range(5)]):
            print(i)
            break
