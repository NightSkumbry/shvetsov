from itertools import permutations
ans = set()

for i in permutations('ворота'):
    for k in range(5):
        if i[k] in 'оа' and i[k+1] in 'оа':
            break
    else:
        ans.add(i)

print(len(ans))







