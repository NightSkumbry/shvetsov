
f = []

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                k = ((x or y) == (y <= z)) or w
                if not k:
                    f.append({'x': x, 'y': y, 'z': z, 'w': w})
                    
from itertools import permutations as p
for l1 in f:
    for l2 in f:
        for l3 in f:
            if l1 != l2 and l1 != l3 and l2 != l3:
                for c1, c2, c3, c4 in p('xyzw'):
                    if l1[c2] == 1:
                        if l2[c4] == 1:
                            if l3[c1] == l3[c4] == 1:
                                print(c1, c2, c3, c4)