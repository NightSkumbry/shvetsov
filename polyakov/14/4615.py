a = 12**34 + 7*12**26 - 3*12**16 + 2*12**5 + 552

r = []
while a:
    r.append(a%12)
    a //= 12
print(sum([i in r for i in range(12)]))

