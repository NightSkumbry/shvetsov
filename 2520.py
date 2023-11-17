import re
with open('./files/k7a-6.txt') as f:
    a = f.read().strip().lower()
print(max(map(len, re.findall(r'[bcdf]+', a))))
