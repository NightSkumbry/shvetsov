from itertools import product, permutations

t = []

for x,y,z,w in product([1,0], repeat=4):
    k = ((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))
    if k:
        t.append({'x':x, 'y':y, 'w':w, 'z':z})


for l1, l2, l3 in permutations(t, 3):
    for c1,c2,c3,c4 in permutations('xyzw'):
        if l1[c2] == l1[c3] == l1[c4] == l2[c3] == l3[c2] == 0:
            if l1[c1] == l2[c2] == l3[c1] == 1:
                print(c1,c2,c3,c4)



