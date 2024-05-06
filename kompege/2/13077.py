from itertools import product, permutations

t = []
f = []

for x,y,z,w in product([1,0], repeat=4):
    f1 = (w == x) and (y <= z)
    f2 = (x <= x) <= (y == z)
    if f1:
        t.append({'x':x, 'y':y, 'z':z, 'w':w, 'f2':f2})
    else:
        f.append({'x':x, 'y':y, 'z':z, 'w':w, 'f2':f2})


for l1, l2 in permutations(t, 2):
    for l3 in f:
        for c1,c2,c3,c4 in permutations('xyzw'):
            if l1['f2'] == l2[c3] == l2[c4] == l3[c2] == l3[c3] == l3['f2'] == 0:
                if l1[c1] == l1[c3] == l1[c4] == l2[c2] == 1:
                    print(c1,c2,c3,c4)





