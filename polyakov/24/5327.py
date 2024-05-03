from tqdm import tqdm
import re

with open('./files/24-212.txt') as f:
    a = f.read().strip().lower().replace('d', 'b').replace('c', 'b').replace('o', 'a')

ans = 0

sh = re.compile(r'(ba)*')

for i in range(len(a)):
    if a[i:i+2] == 'ba':
        m = re.match(sh, a[i:])
        if m is not None:
            ans = max(ans, m.span()[1])

print(ans/2)



