a = abs(5*36**7 + 6**10 - 36)
p = ''
while a > 0:
    p += str(a%6)
    a //= 6
print(p.count('5'))
