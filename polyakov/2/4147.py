from itertools import product as pr
from itertools import permutations as pe
f = []
for a,b,c,d in pr([0,1], repeat=4):
    k = a and (not b) or (a or b) and c or d
    if not k:
        f.append({'a':a, 'b':b, 'c':c, 'd':d})


for l1,l2,l3 in pe(f, 3):
    for c1,c2,c3,c4 in pe('abcd', 4):
        if l1[c4] == l2[c4] == l2[c2] == l3[c1] == 1:
            print(c1,c2,c3,c4)






