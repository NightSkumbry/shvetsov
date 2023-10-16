a = abs((7**160 * 7**90) - (14**150 + 2**13))
p = ''
while a > 0:
    p+=str(a%7)
    a //= 7

print(sum(map(int, p.replace('6', '0'))))
