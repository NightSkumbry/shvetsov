a = 3*16**8 - 4**5 + 3

r = []
while a:
    r.append(a%4)
    a //= 4

print(r.count(3))




