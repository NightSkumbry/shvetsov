from itertools import product, permutations

t = []
for x,y,z,w in product([1,0], repeat=4):
    k = (not (x == (w and (not z)))) and (y == (x and (not w)))
    if k:
        t.append({'x':x, 'y':y, 'z':z, 'w':w})


for r1, r2, r3 in permutations(t, 3):
    for c1, c2,c3,c4 in permutations('xyzw'):
        if r1[c3] == r2[c2] == r2[c4] == r3[c1] == r3[c4] == 0:
            if r3[c3] == 1:
                print(c1,c2,c3,c4)



