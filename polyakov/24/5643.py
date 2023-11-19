import re
with open('./files/24-228.txt') as f:
    a = f.read().lower().strip()

b = max(map(int, re.findall(r'ss(12[0-9][0-9][0-9][0-9]77[0-9][0-9]9)ss', a)))
su = 0
mu = 1
for i in str(b):
    if i in '13579':
        su += int(i)
    else:
        mu *= int(i)
print(su+mu)

## 0 = 00