s = set()
f = '0123456789abcdef'
for y in '9abcdef':
    for x in f[:f.find(y)]:
        s.add(int(f'5{x}{y}c', 16) + int(f'8{x}{x}7', f.find(y)+1))
print(len(s))