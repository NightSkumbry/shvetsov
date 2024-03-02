import re

with open('./files/24_12476.txt') as f:
    a = f.read().strip().lower()

a = a.replace('ror', 'ro3')
a = a.replace('oro', '1ro')
a = a.replace('ro', '4')
print(a.count('4'))
# b = a.split('4')

for i in range(22):
    print(max(map(lambda x: len(x[1])+21+(x[0] == '4')+(x[3] == '4'), re.findall(r'([341])([proeg]*(4[proeg]*){21})([413])', a))))
    a = a[a[1:].find('4'):]




