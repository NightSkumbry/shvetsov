import re
from tqdm import tqdm

with open('./files/24-197.txt') as f:
    a = f.read().strip().lower()

ans = 0
sh = re.compile(r'((x[xyz]y)|(z[xyz]y))*')

for i in tqdm(range(len(a))):
    if a[i] != 'y':
        m = re.match(sh, a[i:])
        if m is not None:
            ans = max(ans, m.span()[1])

print(ans/3)
