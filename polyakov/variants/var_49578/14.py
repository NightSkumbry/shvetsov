a = 103*7**103 - 5*7**57 + 98

r = []
while a:
    r.append(a%7)
    a //= 7

print(sum(r))




