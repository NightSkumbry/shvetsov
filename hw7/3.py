import re
with open('./files/24-j1.txt') as f:
    a = f.read().lower()
print(max(map(lambda x: len(x[0]), re.findall(r'((kot)+)'))))