import re
with open('./files/24-j5.txt') as f:
    a = f.read().strip().lower()
print(max(map(len, re.findall(r'(?:kot)+', a)))//3)