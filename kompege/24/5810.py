import re
with open('./files/24_5810.txt') as f:
    a = f.read().lower().strip()
a = a.replace('xyz', 'a')
a = a.replace('yz', 'b')
a = a.replace('xy', 'c')
print(max(map(lambda x: 3*x.count('a')+2*x.count('b')+2*x.count('c'), re.findall(r'[abc]+', a))))
