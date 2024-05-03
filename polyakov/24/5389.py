from tqdm import tqdm
import re

with open('./files/24-215.txt') as f:
    a = f.read().strip().lower().replace('b', 'a').replace('c', 'a').replace('2', '1').replace('3', '1')

ans = 0

sh = re.compile(r'(a11)*')

for i in range(len(a)):
    if a[i:i+3] == 'a11':
        m = re.match(sh, a[i:])
        if m is not None:
            ans = max(ans, m.span()[1])

print(ans/3)



