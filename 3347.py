import re
with open('./files/24-j2.txt') as f:
    a = f.read().strip().lower()
print(max(map(len, [*re.findall(r'f+', a), *re.findall(r'a+', a), *re.findall(r'i+', a), *re.findall(r'l+', a)])))
