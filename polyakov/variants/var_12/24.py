from tqdm import tqdm
import re

with open('./polyakov/variants/var_12/24-197.txt') as f:
    a = f.read().strip().lower()
ans = 0
for i in tqdm(range(len(a))):
    if a[i] in ['x','z']:
        p = re.match(r'([xz].[y])+', a[i:])
        if p:
            t = p.span()
            ans = max(ans, t[1])
print(ans)







