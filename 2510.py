with open('./files/k7a-1.txt') as f:
    a = f.read().strip().lower()
import re
print(max(map(len, re.findall(r'[abc]+', a))))
