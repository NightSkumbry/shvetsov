from itertools import permutations
t = []
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            k = c and (not b) or c and a
            if k:
                t.append({'a': a,'b': b,'c':c})

for r1 in t:
    for r2 in t:
        if r1 == r2:
            continue
        for r3 in t:
            if r1 == r3 or r2 == r3:
                continue
            for c1,c2,c3 in permutations('abc',3):
                if r1[c1] == 0 and r1[c2] == 1 and r1[c3] == 0:
                    if r2[c1] == 0 and r2[c2] == 1 and r2[c3] == 1:
                        if r3[c1] == 1 and r3[c2] == 1 and r3[c3] == 1:
                            print(c1,c2,c3)








