from itertools import permutations, product

t = []
f = []

for x,y,z,w in product([1,0], repeat=4):
    k = not ((((not w) <= (not y)) <= (not z)) <= x)
    if k:
        t.append({'x':x, 'y':y, 'w':w, 'z':z})
    else:
        f.append({'x':x, 'y':y, 'w':w, 'z':z})
        

for l1, l2 in permutations(t, 2):
    for l3 in f:
        for c1, c2,c3,c4 in permutations('xyzw'):
            if l1[c4] == l3[c1] == l3[c4] == 0:
                if l1[c3] == l2[c2] == l2[c4] == l3[c2] == 1:
                    print(c1,c2,c3,c4)


