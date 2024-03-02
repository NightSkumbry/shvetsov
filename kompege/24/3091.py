from collections import Counter as C

with open('./files/24__3091.txt') as f:
    a = [i.strip().lower() for i in f]

def test(c, s):
    g = c.most_common()
    if g[-1][1] == 1 and all(i[1]%2==0 for i in g[:-1]):
        p = []
        for k in range(3):
            if s[k] != s[-k-1]:
                p.append((s[k], s[-k-1]))
        if g[-1][0] == s[3]:
            if len(p) == 0:
                return True
            if len(p) == 2:
                if (p[0][0] == p[1][1] and p[0][1] == p[1][0]) or (p[0][0] == p[0][1] and p[1][1] == p[1][0]):
                    return True
    return False
#  x y
#  y x
#  x x
#  y y
for s in a:
    c = C(s[:7])
    for i in range(7, len(s)):
        





