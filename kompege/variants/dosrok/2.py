
from itertools import product, permutations

f = []
for x, y, z, w in product([1,0], repeat=4):
    k = (x and (not z)) or (y == z) or (not w)
    if not k:
        f.append({'x':x, 'y':y, 'z':z, 'w':w})


for l1, l2, l3 in permutations(f, 3):
    for c1,c2,c3,c4 in permutations('xyzw'):
        if l1[c3] == l1[c4] == l2[c2] == l2[c4] == l3[c2] == 0:
            if l2[c1] == l3[c1] == l3[c3] == 1:
                print(c1,c2,c3,c4)


