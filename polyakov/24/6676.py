import re
with open('./files/24-264.txt') as f:
    a = f.read().lower().strip()

print(max(map(len, re.findall(r'[^0-9^a-f][1-9a-f][0-9a-f]*', a)))-1)