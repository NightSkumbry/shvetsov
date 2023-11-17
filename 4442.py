import re
with open('./files/24-180.txt') as f:
    a = f.read().lower().strip()
ans = 0
for i, e in enumerate(a):
    if e in '210':
        b = re.match(r'((([01][0-9])|(2[0-3]))[0-5][0-9])+', a[i:])
        if b:
            ans = max(ans, b.span()[1]//4)
print(ans)