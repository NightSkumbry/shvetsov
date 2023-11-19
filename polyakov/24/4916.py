import re
with open('./files/4917_pol.txt') as f:
    a = f.read().strip().replace('A', 'ABA')

print(len(re.findall(r'A[^A^B]{,10}A', a)))

