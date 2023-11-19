a = '753x2'
b = '2x173'
for i in '0123456789ABC':
    x = int(a.replace('x', i), 13) + int(b.replace('x', i), 13)
    if x%12 == 0:
        print(x//12)
# min
    