import re
with open('./kompege/variants/dosrok/24.txt') as f:
    a = f.read().strip().lower().replace('b', 'a').replace('c', 'a').replace('6', '2').replace('7', '2').replace('8', '2').replace('9', '2')

a = re.sub(r'a{2,}', 'a a', re.sub(r'2{2,}', '2 2', a))

a = a.split()
print(max(map(len, a)))

