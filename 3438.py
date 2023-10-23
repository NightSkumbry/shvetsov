import re
with open('./files/24-j9.txt') as f:
    a = f.read().strip()
pat = re.compile(r'(?P<a>.)(?P<b>.).(?P=b)(?P=a)')
ans = 0
for i in range(len(a)-4):
    if re.fullmatch(pat, a[i: i+5]):
        ans += 1
print(ans)

