import re
with open('./files/24_4555.txt') as f:
    a = f.read().lower().strip()
a = a.replace('zzxy', 'zzx_xy')
a = a.replace('zzx', 'aaa')
a = a.replace('xy', 'bb')

print(max(map(len, re.findall(r'[ab]+', a))))
