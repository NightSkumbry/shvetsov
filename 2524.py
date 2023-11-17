import re
with open('./files/24-1.txt') as f:
    a = f.read().strip().lower()
print(min(map(lambda x: int(x[1:-1]), re.findall(r'[a-z][1-9][0-9]*[13579][a-z]', a))))