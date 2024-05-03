import re
from tqdm import tqdm

with open('./files/24-224.txt') as f:
    a = f.read().strip().lower()

ans = 0
for i in tqdm(range(len(a))):
    if a[i:i+3] in ['bac', 'cab']:
        m = re.match(r'((bac)|(cab))+', a[i:])
        if m is not None:
            ans = max(ans, m.span()[1])

print(ans)


