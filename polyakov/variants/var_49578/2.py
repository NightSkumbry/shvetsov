from itertools import permutations

true = []
false = []

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = not ( (((not w) <= (not y)) <= (not z)) <= x )
                if F:
                    true.append({'x': x, 'y': y, 'z': z, 'w': w})
                else:
                    false.append({'x': x, 'y': y, 'z': z, 'w': w})

# print('True:', *true, sep='\n', end='\n\n')
# print('False:', *false, sep='\n')

for l1 in true:
    for l2 in true:
        if l1 == l2:
            continue
        for l3 in false:
            for c1, c2, c3, c4 in permutations('xyzw'):
                if l1[c3] == 1 and l1[c4] == 0:
                    if l2[c2] == l2[c4] == 1:
                        if l3[c1] == l3[c4] == 0 and l3[c2] == 1:
                            print(c1, c2, c3 ,c4)




