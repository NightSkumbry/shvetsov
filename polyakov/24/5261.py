import re
with open('./files/24-209.txt') as f:
    a = f.read().lower().strip()
    a = a.replace('ab', 'a1b')
    a = a.replace('cb', 'c2b')
    a = a.replace('ba', '3')
    a = a.replace('bc', '4')
print(max(map(len, re.findall(r'[1-4]+', a))))

