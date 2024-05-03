from tqdm import tqdm
import re

with open('./files/24-215.txt') as f:
    a = f.read().strip().lower().replace('b', 'a').replace('c', 'a').replace('2', '1').replace('3', '1')

ans = 0

sh = re.compile(r'(a1a)*')

for i in range(len(a)):
    if a[i:i+3] == 'a1a':
        m = re.match(sh, a[i:])
        if m is not None:
            ans = max(ans, m.span()[1])

print(ans/3)



