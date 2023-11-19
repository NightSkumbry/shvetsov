with open('./files/24-173.txt') as f:
    a = f.read()
import re
ans = 0
pr = 0
while True:
    r = re.search(r'(?P<a>.)(?P<b>.)(?P<c>.)(?P=a)(?P=b)(?P=c)', a[pr:])
    if r is None:
        break
    i = r.span()
    ans = max(ans, i[1]-1)
    pr += i[0]+1
print(max(ans, len(a)-pr-1))
    