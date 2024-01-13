import re
with open('./files/24-278.txt') as f:
    a = f.read().strip().upper()
print(max(map(lambda x: len(x[1]), (re.findall(r'(?P<n>[02468])([KNLF]+)(?P=n)', a)))))