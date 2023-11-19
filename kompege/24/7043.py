import re
with open('./files/24_7043.txt') as f:
    a = f.read().strip().lower()
pt = re.compile(r'0[^1]*1[^2]*2[^3]*3[^4]*4[^5]*5[^6]*6[^7]*7[^8]*8[^9]*9[^a]*a[^b]*b[^c]*c[^d]*d[^e]*e[^f]*f')
ans = len(a)
for i, e in enumerate(a):
    if e == '0':
        m = re.match(pt, a[i:])
        if m is None:
            break
        ans = min(ans, m.span()[1])
print(ans)