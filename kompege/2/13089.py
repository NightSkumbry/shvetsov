from itertools import product, permutations

f = []
for x, y, z, w, u in product([1,0], repeat=5):
    k = ((z <= w) and (y == (not x))) <= (u == (y or z))
    if not k:
        f.append({'x':x, 'y':y, 'z':z, 'w':w, 'u':u})


for r1, r2, r3, r4 in permutations(f, 4):
    for c1,c2,c3,c4,c5 in permutations('xyzwu'):
        if r1[c1] == r1[c4] == r1[c3] == r1[c5] == r2[c1] == r2[c4] == r2[c5] == r3[c2] == r3[c3] == r3[c4] == r4[c1] == r4[c2] == 0:
            print(c1,c2,c3,c4,c5)







