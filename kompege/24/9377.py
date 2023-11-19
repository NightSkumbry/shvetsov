import re
with open('./files/24_9377.txt') as f:
    a = 'a' + f.read().lower() + 'a'
a = re.sub(r'[a-z]0[0-9]+', 'a+', a)
print(max(map(lambda x: len(x[0]), re.findall(r'([0-9]*[02468]([a-z]*[0-9]*[02468][a-z])+)', a)))-1)
