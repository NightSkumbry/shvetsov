import re
with open('./files/24-5.txt') as f:
    a = f.read().strip()

print(max(map(len, re.findall(r'\(+', a))))