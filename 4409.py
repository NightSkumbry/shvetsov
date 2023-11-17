import re
from collections import Counter as c
with open('./files/24-179.txt') as f:
    a = f.read().lower().strip()

b = []
for i, e in enumerate(a):
    if e == 'c':
        if re.fullmatch(r'cb[^a^b^f]bc', a[i:i+5]):
            b.append(a[i+2])
mc = c(b).most_common(1)[0][0]
print(mc, len(b))