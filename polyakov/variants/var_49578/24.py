import re


with open('./some_files/var/24-263.txt') as f:
    a = f.read().strip().lower()

ans = 0
i = 0

while True:
    # print(i)
    g = re.search(r'(?P<a>.)(?P=a)', a[i:])
    if g is None:
        ans = max(ans ,len(a)-i)
        break
    f = g.span()[1]
    ans = max(ans, f)
    i += f

print(ans)




