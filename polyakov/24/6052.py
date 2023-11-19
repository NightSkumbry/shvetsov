import re
with open('./files/24-241.txt') as f:
    a = f.read().lower().strip()
print(max(map(lambda x: len(x[0]), re.findall(r'(([aeo][aeo][bcdf])+)', a)))//3)
