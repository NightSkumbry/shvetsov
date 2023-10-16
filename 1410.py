a = abs(4**625 + 2**571 - 2**311 - 48)
p = ''
while a > 3:
    p += str(a%4)
    a //= 4

p += str(a) * (a != 0)
print(p.count('1'))
