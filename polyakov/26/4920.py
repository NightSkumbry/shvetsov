
with open('./files/26-73.txt') as f:
    a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[1:]))

s = [['0' for i in range(480)] for i in range(640)]

for i in a:
    s[i[0]-1][i[1]-1] = '1'

import re

j = []

for i in s:
    j.append(max(list(map(len, re.findall(r'1+', ''.join(i)))) + [0]))

j = j[::-1]

print(max(j), 640-j.index(max(j)))



