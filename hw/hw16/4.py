from itertools import product

ans = set()

for i in product('арсений', repeat=4):
    if i[0] != 'й':
        if any([k in i for k in 'аеи']):
            ans.add(i)

print(len(ans)) # -> 1866
