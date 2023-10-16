a = abs(17*16**455 + 2**67 - 4**47 + 58)
p = ''
while a > 7:
    p += str(a%8)
    a //= 8

p += str(a) * (a != 0)
print(p.count('0') + p.count('2'))
