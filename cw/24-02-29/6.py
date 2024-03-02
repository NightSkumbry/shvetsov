
from itertools import product, permutations

f = []
for x,y,z,w in product([0,1], repeat=4):
    k = ((w <= y) <= (x == y)) or (not z)
    if not k:
        f.append({'x':x,'y':y,'z':z,'w':w})

for r1, r2, r3 in permutations(f, 3):
    for c1,c2,c3,c4 in permutations('xyzw'):
        if r1[c2] == r1[c4] == r2[c1] == r2[c4] == 0:
            if r1[c3] == r3[c2] == r3[c3] == 1:
                print(c1,c2,c3,c4)





