from itertools import product, permutations

f = []
for x, y, z, w in product([0, 1], repeat=4):
    k = ((x or y) == (y <= z)) or w
    if not k:
        f.append({'x':x, 'y':y, 'z': z, 'w':w})

for r1, r2, r3 in permutations(f, 3):
    for c1, c2, c3, c4 in permutations('xyzw'):
        if r1[c2] == r2[c4] == r3[c1] == r3[c4] == 1:
            print(c1,c2,c3,c4)




