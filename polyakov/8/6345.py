from itertools import permutations
ans = set()
for i in permutations(set('ВАРФОЛОМЕЙ'.lower()), 6):
    i = ''.join(i)
    if len(set(i)) == 6:
        s = 0
        g = 0
        for k in range(5):
            if i[k] in 'аое':
                g += 1
                if i[k+1] in 'аое':
                    break
            else:
                s += 1
        else:
            if i[-1] in 'аое':
                g += 1
            else:
                s += 1
            if s > g:
                ans.add(i)

print(len(ans))










