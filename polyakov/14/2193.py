a = abs(64**30 + 2**300 - 32)
p = ''
while a > 0:
    p += str(a % 4)
    a //= 4
print(p.count('3'))
