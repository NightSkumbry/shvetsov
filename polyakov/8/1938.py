from itertools import permutations

ans = set()

for i in permutations('нигрол'):
    if i[0] != 'о':
        i = ''.join(i)
        if 'оиг' not in i:
            ans.add(i)

print(len(ans))




