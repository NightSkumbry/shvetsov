from itertools import product as prod
from itertools import permutations as perm

t = []
f = []

for x,y,z,w in prod([0,1], repeat=4):
    k = ((w <= x) != z) and y
    if k:
        t.append({'x':x, 'y': y, 'z':z,'w':w})
    else:
        f.append({'x':x, 'y': y, 'z':z,'w':w})

for l1,l2 in perm(t, 2):
    for l3 in f:
        for c1,c2,c3,c4 in perm('xyzw', 4):
            if l1[c3] == l1[c4] == l2[c1] == l3[c3] == 0:
                if l1[c1] == l3[c1] == l3[c2] == 1:
                    print(c1,c2,c3,c4)








