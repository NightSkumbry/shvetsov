import re
with open('./files/24-1.txt') as f:
    a = f.read().strip().lower()
print(max(map(lambda x: int(x[1:-1]), re.findall(r'[a-z][2468][24680]*[a-z]', a))))