from itertools import product, permutations

f = []
for x, y, z, w in product([0, 1], repeat=4):
    k = (((y and (x == (not z)))) <= w) and (z <= y)
    if not k:
        f.append({'x':x, 'y':y, 'z': z, 'w':w})

for r1, r2, r3 in permutations(f, 3):
    for c1, c2, c3, c4 in permutations('xyzw'):
        if r3[c1] == r3[c4] == 1:
            if r1[c1] == r1[c2] == r2[c1] == r2[c3] == r2[c4] == 0:
                print(c1,c2,c3,c4)




