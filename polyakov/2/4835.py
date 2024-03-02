from itertools import product as prod
from itertools import permutations as perm
t = []
for x, y, z, w in prod([0,1], repeat=4):
    k = ((w <= y) and ((not x) <= z)) <= ((z == w) or (y and (not x)))
    if not k:
        t.append({'x':x,'y':y,'z':z,'w':w})


for l1, l2, l3 in perm(t, 3):
    for c1,c2,c3,c4 in perm('xyzw'):
        if l1[c1] == l1[c2] == l1[c4] == 1:
            if l2[c2] == l2[c1] == l2[c3] == l3[c1] == 0:
                print(c1,c2,c3,c4)



