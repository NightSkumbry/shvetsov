from itertools import permutations
ans = set()
for i in permutations('просто'):
    if all([i[k] != i[k+1] for k in range(5)]):
        ans.add(i)



print(len(ans))


