a = 4**1503 + 3*4**244 - 2*4**1444 - 96

r = []
while a:
    r.append(a%4)
    a //= 4

print(sum(r))






