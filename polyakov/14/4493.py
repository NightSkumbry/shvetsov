a = 3**37 + 2*3**23 + 3*3**20 + 4*3**4 + 5*3**3 + 4 + 5

r = []
while a:
    r.append(a%9)
    a //= 9
print(r.count(0))

