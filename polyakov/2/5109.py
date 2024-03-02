from itertools import product as prod
from itertools import permutations as perm

t = []
for x,y,z,w in prod([1,0], repeat=4):
    k = (not (x <= z)) or (y == w) or y
    if not k:
        t.append({'x':x,'y':y,'z':z,'w':w})

for l1,l2,l3 in perm(t, 3):
    for c1,c2,c3,c4 in perm('xyzw', 4):
        if l1[c2] == l1[c1] == l3[c4] == l2[c1] == 0:
            if l3[c2] == l3[c1] == 1:
                print(c1,c2,c3,c4)







