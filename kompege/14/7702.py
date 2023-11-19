s = set()
for y in '9abcdefgh':
    for x in '0123456789abcdefgh'[:'0123456789abcdefgh'.find(y)]:
        a = int(f'5{x}{y}a', 18)
        b = int(f'18{x}7', '0123456789abcdefgh'.find(y)+1)
        s.add(a+b)
print(len(s))