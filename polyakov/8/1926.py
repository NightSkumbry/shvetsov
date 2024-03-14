from itertools import permutations
ans = set()

for i in permutations('крой'):
    if i[0] != 'й':
        for k in range(3):
            if i[k] == 'о' and i[k+1] == 'й':
                break
        else:
            ans.add(i)

print(len(ans))






