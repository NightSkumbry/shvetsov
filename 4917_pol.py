import re
with open('./files/4917_pol.txt') as f:
    a = f.read().strip()

print(len(re.findall(r'A[^A^B]{18,}B', a)))

