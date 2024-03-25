from itertools import product

ans = set()

for i in product('карс', repeat=6):
    if sum([i.count(k) for k in 'крс']) >= 3:
        ans.add(i)

print(len(ans)) # -> 3942
