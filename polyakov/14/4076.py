a = 7**1003 + 6*7**1104 - 3*7**57 + 294


r = []
while a:
    r.append(a%7)
    a //= 7

print(sum(r))



