from itertools import permutations

ans = set()
for i in permutations(range(16), 4):
    if i[0] != 0:
        if all([i[k]%2 != i[k+1]%2 for k in range(3)]):
            ans.add(i)

print(len(ans)) # -> 5880
