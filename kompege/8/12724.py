from itertools import product as p
ans = set()

for i in p(set('КАЛЕЙДОСКОП'.lower()), repeat=6):
    ans.add(''.join(i))

ans = sorted(ans)[::-1]

for i, e in enumerate(ans):
    if i%2 == 0:
        if e[0] == 'к':
            if e.count('й') >= 2:
                if 'с' not in e:
                    if 'е' not in e:
                        print(i)
                        break




